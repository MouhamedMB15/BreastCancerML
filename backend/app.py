


#Imports
from flask import Flask, request, jsonify
import numpy as np
import joblib
from flask_cors import CORS

# utlizing flask app
app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})  

# Load the model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

# Define the predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json(force=True)
        input_data = np.array(data['input']).reshape(1, -1)
        
        
        # # Log the input data
        # app.logger.debug(f"Input data: {input_data}")
        
        #standarize input data
        input_data_std = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_data_std)
        prediction_label = int(prediction[0])
        
        # Return the prediction result
        return jsonify({'prediction': prediction_label})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
