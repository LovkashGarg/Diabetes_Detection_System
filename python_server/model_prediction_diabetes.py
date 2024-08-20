from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

import os
model_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')
print(model_path)
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/')
def HelloWorld():
    return "Hello World"


@app.route('/', methods=['POST'])
def predict():
    data = request.json
    print(data)
    features = np.array(data['features']).reshape(1, -1)

    # Assuming the original training data had the same feature order and names
    feature_names = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    
    # Convert input features to a DataFrame with appropriate feature names
    features_df = pd.DataFrame(features, columns=feature_names)
    
    # Use the loaded scaler to transform the input data
    input_data_standardized = scaler.transform(features_df)
    
    prediction = model.predict(input_data_standardized)
    print(prediction)
    
    if prediction[0] == 0:
        return jsonify({'prediction': "Non Diabetic"})
    else:
        return jsonify({'prediction': "Diabetic"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

