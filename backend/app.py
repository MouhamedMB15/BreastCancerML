
#Imports
from flask import Flask, request, jsonify
import numpy as np
import joblib
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow all origins for testing

# Load the model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_data = np.array(data['input']).reshape(1, -1)
        
        input_data_std = scaler.transform(input_data)
        
        prediction = model.predict(input_data_std)
        prediction_label = int(prediction[0])
        
        return jsonify({'prediction': prediction_label})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
