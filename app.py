import joblib
from flask import Flask, request, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
naive_bayes_chd = joblib.load('naive_bayes_chd.pkl')
scaler = joblib.load('scaling_chd.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json  # Access the JSON data directly
    features = [
        data['age'],
        data['sex'],
        data['is_smoking'],
        data['BPMeds'],
        data['prevalentStroke'],
        data['prevalentHyp'],
        data['diabetes'],
        data['totChol'],
        data['sysBP'],
        data['diaBP'],
        data['BMI'],
        data['heartRate'],
        data['glucose'],
        data['BP_Label'],
        data['Smoking_Category']
    ]
    features = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(features)
    prediction = naive_bayes_chd.predict(scaled_features)[0]

    return jsonify(int(prediction))  # Convert prediction to an integer

if __name__ == "__main__":
    app.run(debug=True)


