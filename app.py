# Import necessary libraries from Flask to create a web application
# render_template is added to serve HTML files from the backend
from flask import Flask, request, jsonify, render_template
# Import CORS to handle cross-origin requests, allowing your frontend to communicate with this backend
from flask_cors import CORS
# Python's built-in 'random' library for generating random numbers
import random

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, which is essential for local development where the frontend and backend run on different ports
CORS(app)

# -----------------------------------------------------------
# Simulated Disease Prediction "Model"
# -----------------------------------------------------------
# This dictionary serves as our simplified, hard-coded machine learning model.
# In a real-world scenario, this would be a trained model (e.g., a pickled scikit-learn model)
# loaded into memory.
# The keys are diseases, and the values are lists of symptoms associated with them.
DISEASE_SYMPTOM_MAP = {
    "Heart Disease": ["chest_pain", "shortness_of_breath", "dizziness", "fatigue"],
    "Diabetes": ["frequent_urination", "increased_thirst", "unexplained_weight_loss", "blurred_vision"],
    "Parkinson's Disease": ["tremor_in_hands", "slowed_movement", "rigid_muscles"],
    "Liver Disease": ["yellowing_of_skin", "abdominal_swelling", "fatigue", "nausea_or_vomiting"]
}

# -----------------------------------------------------------
# Frontend Serving Endpoint
# -----------------------------------------------------------
# This route now serves the index.html file directly.
# When a user visits the root URL '/', Flask will render and send the HTML file.
@app.route('/')
def home():
    """
    Renders the index.html file to serve the frontend of the application.
    The HTML file must be located in a folder named 'templates' inside your project directory.
    """
    return render_template('index.html')


# -----------------------------------------------------------
# Prediction Endpoint
# -----------------------------------------------------------
# Define the '/predict' route. It only accepts POST requests.
# This is the main API endpoint your frontend will call to get a prediction.
@app.route('/predict', methods=['POST'])
def predict_disease():
    """
    Handles a POST request with a list of symptoms and returns a simulated disease prediction.

    The function performs the following steps:
    1.  Parses the incoming JSON data from the request body to get the list of symptoms.
    2.  Iterates through the pre-defined `DISEASE_SYMPTOM_MAP`.
    3.  For each disease, it calculates a "match count" by comparing the user's symptoms with the disease's symptoms.
    4.  It identifies the disease with the highest number of matching symptoms.
    5.  Calculates a confidence score based on the match count.
    6.  Constructs a JSON response with the predicted disease and confidence, and returns it.
    """
    try:
        # Get the JSON data from the request body. The frontend sends this.
        data = request.get_json(force=True)
        # Extract the list of symptoms from the data.
        user_symptoms = data.get('symptoms', [])

        # Initialize variables to store the best prediction result
        highest_match = 0
        predicted_disease = "No clear match"
        confidence = 0.0

        # Check if the user has provided any symptoms
        if not user_symptoms:
            # If no symptoms are provided, return a specific response
            return jsonify({
                "predicted_disease": "Undetermined",
                "confidence": 0
            })

        # Iterate through our "model" to find the best-matching disease
        for disease, symptoms_list in DISEASE_SYMPTOM_MAP.items():
            # Calculate how many of the user's symptoms match the current disease's symptoms
            match_count = sum(1 for symptom in user_symptoms if symptom in symptoms_list)

            # Check if this disease has a better match than the current best
            if match_count > highest_match:
                highest_match = match_count
                predicted_disease = disease

        # If a match was found, calculate the confidence score
        if highest_match > 0:
            # Simple confidence calculation: (number of matching symptoms / total symptoms for that disease) * a small randomization factor for realism
            total_symptoms_for_disease = len(DISEASE_SYMPTOM_MAP[predicted_disease])
            # Ensure we don't divide by zero
            if total_symptoms_for_disease > 0:
                base_confidence = (highest_match / total_symptoms_for_disease) * 100
                # Add a little randomness to make the result feel less static
                confidence = round(min(100, base_confidence + random.uniform(-10, 10)), 2)
            else:
                confidence = 0.0

        # Return the final prediction result as a JSON response
        return jsonify({
            "predicted_disease": predicted_disease,
            "confidence": confidence
        })

    except Exception as e:
        # In case of any error, return a 500 server error response with a clear message
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------
# Main execution block
# -----------------------------------------------------------
# This block ensures that the app runs only when the script is executed directly.
if __name__ == '__main__':
    # Run the Flask development server on host '0.0.0.0' and port 5000.
    # '0.0.0.0' makes it accessible from your local network, and debugging is enabled.
    app.run(host='0.0.0.0', port=5000, debug=True)
