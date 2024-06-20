


#Imports
from flask import Flask, request, jsonify
import numpy as np
import joblib
from flask_cors import CORS

#Flask course config
app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})  

# Load the model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

#post method
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input']).reshape(1, -1)
    input_data_std = scaler.transform(input_data)
    prediction = model.predict(input_data_std)
    prediction_label = int(prediction[0])
    return jsonify({'prediction': prediction_label})

if __name__ == '__main__':
    app.run(debug=True)


#TODO: Fix model call in baackend