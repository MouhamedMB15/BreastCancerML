
//Import
import React, { useState } from 'react';
import axios from 'axios';
import './predictFormCSS.css'; //styles


//Prediction Form
const PredictForm = () => {
    //form data state
    const [formData, setFormData] = useState({
        mean_radius: '',
        mean_texture: '',
        mean_perimeter: '',
        mean_area: '',
        mean_smoothness: '',
        mean_compactness: '',
        mean_concavity: '',
        mean_concave_points: '',
        mean_symmetry: '',
        mean_fractal_dimension: '',
        radius_error: '',
        texture_error: '',
        perimeter_error: '',
        area_error: '',
        smoothness_error: '',
        compactness_error: '',
        concavity_error: '',
        concave_points_error: '',
        symmetry_error: '',
        fractal_dimension_error: '',
        worst_radius: '',
        worst_texture: '',
        worst_perimeter: '',
        worst_area: '',
        worst_smoothness: '',
        worst_compactness: '',
        worst_concavity: '',
        worst_concave_points: '',
        worst_symmetry: '',
        worst_fractal_dimension: '',
    });

    //Prediction state
    const [prediction, setPrediction] = useState(null);
    //Submit button text state
    const [buttonText, setButtonText] = useState('Submit');
    
    //retrieve values
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    //Submit function
    const handleSubmit = (e) => {
        e.preventDefault();
        const input = Object.values(formData).map(value => parseFloat(value));
        axios.post('http://127.0.0.1:5000/predict', { input })
            .then(response => {
                setPrediction(response.data.prediction);
                setButtonText('Prediction Completed!');
            })
            .catch(error => console.error('Error:', error));
    };

    return (
        <div className="predict-form-container">
            <h1>Breast Cancer Prediction</h1>
            <form onSubmit={handleSubmit} className="predict-form">
                {Object.keys(formData).map(key => (
                    <div key={key} className="form-group">
                        <label>{key.replace(/_/g, ' ')}</label>
                        <input
                            type="text"
                            name={key}
                            value={formData[key]}
                            onChange={handleChange}
                        />
                    </div>
                ))}
                <button type="submit" className="submit-button">{buttonText}</button>
            </form>
            {prediction !== null && (
                <div className="prediction-result">
                    <h2>Breast Cancer Disease Prediction: {prediction === 0 ? 'Malignant' : 'Benign'}</h2>
                </div>
            )}
        </div>
    );
};

//export 
export default PredictForm;