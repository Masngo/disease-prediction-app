# Disease Prediction System 🩺🤖
This is a comprehensive, end-to-end machine learning-based application for disease prediction. It leverages Python and Flask to create a web-based interface that utilizes a trained machine learning model to predict diseases based on a patient's symptoms. The project demonstrates a full MLOps pipeline, from data preparation and model training to robust evaluation and final deployment.

A Flask-based web application that predicts possible diseases based on symptoms entered by the user.
It uses Python and a rule-based logic engine to match symptoms with potential conditions.
This project is designed for educational purposes and as a demonstration of building and deploying a web-based medical tool.

📸 Screenshots

Homepage

 
 
 
 

 
Prediction Result
 
 
 

 

🧠 Workflow Diagram
flowchart LR

    A[User Inputs Symptoms] --> B[Flask Web App]
    B --> C[Rule-Based Logic]
    C --> D[Possible Disease Prediction]
    D --> E[Display on Web UI]

🚀 Getting Started
Follow these steps to run the application locally.

Prerequisites
•	Python 3.9+
•	pip (Python package manager)

Installation
1.	Clone the repository
git clone https://github.com/Masngo/disease-prediction-app.git
cd disease-prediction-app
2.	Create and activate a virtual environment
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Windows:
python -m venv venv
venv\Scripts\activate
3.	Install dependencies
pip install -r requirements.txt

Usage
Run the application:
flask run
Visit the app in your browser:
http://127.0.0.1:5000/

🛠️ Deployment
This app is ready for deployment on platforms like Render or Heroku.
Build Command:
pip install -r requirements.txt
Start Command:
gunicorn app:app

📂 Project Structure
disease-prediction-app/
│
├── app.py                 # Flask application
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
├── requirements.txt       # Dependencies
├── assets/                # Screenshots
└── README.md              # Documentation

✍️ Author
Masango Dewheretsoko

•	GitHub

•	LinkedIn


