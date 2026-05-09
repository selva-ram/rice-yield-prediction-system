from flask import Flask, render_template, request
import joblib
import pandas as pd
import warnings
import os

# Suppress sklearn version mismatch warnings (model was pickled with older sklearn)
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

# ── Load model artifacts ─────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model          = joblib.load(os.path.join(BASE_DIR, "rice_model.pkl"))
scaler         = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
state_encoder  = joblib.load(os.path.join(BASE_DIR, "state_encoder.pkl"))
season_encoder = joblib.load(os.path.join(BASE_DIR, "season_encoder.pkl"))
yield_encoder  = joblib.load(os.path.join(BASE_DIR, "yield_encoder.pkl"))

# ── BUG FIX #1 & #2: Season and State encoder classes have trailing whitespace.
# The HTML form sends clean (stripped) values, so we must strip the classes
# before displaying them, and map back to the original (spaced) value at
# prediction time so the encoder doesn't crash with "unseen label".
# ─────────────────────────────────────────────────────────────────────────────
_raw_seasons = list(season_encoder.classes_)       # ['Kharif     ', ...]
_raw_states  = list(state_encoder.classes_)        # ['Telangana ', ...]

# Clean display names → raw encoder values
season_map = {s.strip(): s for s in _raw_seasons}  # {'Kharif': 'Kharif     '}
state_map  = {s.strip(): s for s in _raw_states}   # {'Telangana': 'Telangana '}

# What we show in the dropdowns (clean, no trailing spaces)
STATES  = sorted(state_map.keys())
SEASONS = sorted(season_map.keys())


@app.route('/')
def home():
    return render_template("index.html", states=STATES, seasons=SEASONS)


@app.route('/predict', methods=['POST'])
def predict():
    # ── BUG FIX #3: Wrap in try/except so bad input shows a friendly message
    # instead of a raw 500 traceback.
    try:
        state_input  = request.form['state'].strip()
        season_input = request.form['season'].strip()
        area_input   = request.form['area'].strip()

        if not area_input:
            raise ValueError("Area field is empty.")

        area = float(area_input)
        if area <= 0:
            raise ValueError("Area must be a positive number.")

        # Map clean display name → raw encoder value (fixes trailing-space bug)
        state_raw  = state_map.get(state_input)
        season_raw = season_map.get(season_input)

        if state_raw is None:
            raise ValueError(f"Unknown state: {state_input!r}")
        if season_raw is None:
            raise ValueError(f"Unknown season: {season_input!r}")

        # Encode inputs
        state_encoded  = state_encoder.transform([state_raw])[0]
        season_encoded = season_encoder.transform([season_raw])[0]

        input_data = pd.DataFrame(
            [[state_encoded, season_encoded, area]],
            columns=["State_Name", "Season", "Area"]
        )

        input_scaled = scaler.transform(input_data)
        prediction   = model.predict(input_scaled)[0]

        # Decode output label
        result = yield_encoder.inverse_transform([prediction])[0]

        # Show confidence probabilities
        proba       = model.predict_proba(input_scaled)[0]
        classes     = yield_encoder.inverse_transform(model.classes_)
        confidence  = {cls: f"{prob*100:.1f}%" for cls, prob in zip(classes, proba)}
        best_prob   = f"{max(proba)*100:.1f}%"

        return render_template(
            "index.html",
            states=STATES,
            seasons=SEASONS,
            prediction_text=f"Predicted Yield: {result}",
            confidence=confidence,
            best_prob=best_prob,
            selected_state=state_input,
            selected_season=season_input,
            selected_area=area,
        )

    except ValueError as e:
        return render_template(
            "index.html",
            states=STATES,
            seasons=SEASONS,
            error_text=str(e),
        )
    except Exception as e:
        return render_template(
            "index.html",
            states=STATES,
            seasons=SEASONS,
            error_text="Prediction failed. Please check your inputs and try again.",
        )


# ── BUG FIX #4: debug=True must never be used in production.
# Use the DEBUG environment variable to control it.
if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=5000)
