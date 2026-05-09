# Rice Yield Prediction System

A Machine Learning powered Flask web application that predicts rice yield levels based on agricultural parameters such as state, season, and cultivated land area.

This project combines Machine Learning, Flask backend development, and a modern responsive frontend to provide real-time yield predictions with confidence analysis.

---

## Features

✅ Predict rice yield levels instantly  
✅ Machine Learning powered predictions  
✅ User-friendly responsive interface  
✅ Confidence probability visualization  
✅ Flask backend integration  
✅ Clean modern UI design  
✅ Error handling and validation  
✅ Real-time prediction analysis  

---

##  Machine Learning Model

The system uses a trained Machine Learning classification model to predict rice yield categories:

- 🟢 High Yield
- 🟡 Medium Yield
- 🔴 Low Yield

The prediction is generated using:

- State
- Season
- Cultivated Area (hectares)

---

##  Technologies Used

### Backend
- Python
- Flask
- Scikit-learn
- Pandas
- Joblib

### Frontend
- HTML5
- CSS3
- Responsive Design

### Machine Learning
- Classification Model
- Feature Scaling
- Label Encoding

---

##  Project Structure

```bash
rice-yield-prediction-system/
│
├── app.py
├── requirements.txt
├── rice_model.pkl
├── scaler.pkl
├── state_encoder.pkl
├── season_encoder.pkl
├── yield_encoder.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

##  Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/selva-ram/rice-yield-prediction-system.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd rice-yield-prediction-system
```

### 3️⃣ Create Virtual Environment (Optional but Recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

The Flask server will start at:

```bash
http://127.0.0.1:5000/
```

Open the link in your browser.

---

## 📸 Application Preview

### Home Page
- Select State
- Select Season
- Enter Area
- Predict Yield

### Prediction Result
- Yield Category
- Confidence Breakdown
- Visual Indicators

---

##  Example Prediction

| State | Season | Area |
|-------|--------|------|
| Tamil Nadu | Kharif | 250 |

### Output
```bash
Predicted Yield: High
```

---

##  Requirements

```txt
Flask
scikit-learn
pandas
joblib
```

---

##  How It Works

1. User enters agricultural details
2. Input data is encoded and scaled
3. ML model processes the input
4. Prediction is generated
5. Confidence probabilities are displayed

---

##  Future Improvements

- Add crop recommendation system
- Add weather API integration
- Deploy using Render/Heroku
- Add database support
- Add graphical analytics dashboard
- Improve prediction accuracy
- Add multilingual support

---

##  Deployment

This project can be deployed on:

- Render
- Railway
- Heroku
- PythonAnywhere

---

##  Author

### Selvaram MS

- BE Computer Science Engineering
- Sathyabama Institute of Science and Technology

LinkedIn:
https://www.linkedin.com/in/selvaram-m-s-a93b4b291/

GitHub:
https://github.com/selva-ram

---

##  License

This project is licensed under the MIT License.

---

##  Support

If you like this project:

 Star this repository  
 Fork this repository  
 Share it on LinkedIn  

---

##  Keywords

Machine Learning, Flask, Python, Rice Yield Prediction, Agriculture AI, Scikit-learn, Web Development, AI Project, Student Project, ML Web App

