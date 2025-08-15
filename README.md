# disease-prediction-app
This is a comprehensive, end-to-end machine learning-based application for disease prediction. It leverages Python and Flask to create a web-based interface that utilizes a trained machine learning model to predict diseases based on a patient's symptoms. The project demonstrates a full MLOps pipeline, from data preparation and model training to robust evaluation and final deployment.

Disease Prediction System

🚀 Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You'll need to have Python 3.9 and above, pip installed on your system.
Installation
Clone the repository from GitHub to your local machine:

git clone https://github.com/Masngo/disease-prediction-app.git
cd https://github.com/Masngo/disease-prediction-app

Create and activate a virtual environment. This is a best practice to manage project dependencies.

On macOS and Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
venv\Scripts\activate


Install the required packages using the requirements.txt file:

pip install -r requirements.txt


Usage
To run the application locally, use the following command:

flask run

The application should now be running at http://127.0.0.1:5000/.

🛠️ Deployment
This application is ready to be deployed on platforms like Render. The required gunicorn dependency is included in requirements.txt.

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

✍️ Author
Masango Dewheretsoko - GitHub | LinkedIn

