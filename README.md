# BreastCancerML

# Breast Cancer Tumor Prediction Model
Breast Cancer Analysis utilizing machine learning in python.  

## Overview

This project is a machine learning application designed to predict whether a breast cancer tumor is malignant or benign based on numerous distinct various input features. The model is built using Logistic Regression and is trained on a dataset of breast cancer cases.

Cases and dataset utilized from the Kaggle Dataset from the Breast Cancer Wisconsin Diagnostics. A full view of this dataset documentation can be found here: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data 

The application consists of a backend server implemented with Flask and a frontend web application built with React JS. Additionally built upon python Jupyter libraries.

## Paramters

Mean Radius: This measures the average distance from the center to the perimeter of the cells. Larger values can indicate larger cells, which are often seen in malignant tumors.

Mean Texture: This represents the standard deviation of grayscale values in the cells. Higher variability in texture can be associated with malignancy.

Mean Perimeter: This is the average length around the boundary of the cells. Similar to radius, a larger perimeter can suggest larger, potentially cancerous cells.

Mean Area: This measures the average area covered by the cells. Larger cell areas can be indicative of malignant tumors.

Mean Smoothness: This captures the local variation in the radius lengths. Less smooth (more jagged) contours are often seen in malignant cells.

Mean Compactness: This is calculated as the perimeter squared divided by the area minus 1.0. It measures the compactness of the cell's shape, with higher values possibly indicating malignancy.

Mean Concavity: This measures the severity of concave portions of the cell contour. More pronounced concavities can be a sign of cancerous cells.

Mean Concave Points: This counts the number of concave portions of the cell contour. A higher number of concave points can be associated with malignancy.

Mean Symmetry: This measures how symmetrical the cells are. Asymmetry in cells can be a characteristic of cancer.

Mean Fractal Dimension: This describes the complexity of the cell boundary, with higher values indicating more complexity, which can be seen in cancerous cells.

Radius Error: This is the standard error of the radius. It provides insight into the variability of cell size.

Texture Error: This measures the standard error of the texture. Variability in texture can be indicative of malignancy.

Perimeter Error: This measures the standard error of the perimeter. It shows how much the perimeter measurement varies.

Area Error: This measures the standard error of the area. It reflects the variability in the size of the cells.

Smoothness Error: This is the standard error of the smoothness. It indicates how much the smoothness measurement varies.

Compactness Error: This is the standard error of the compactness. It shows the variability in the compactness measurement.

Concavity Error: This measures the standard error of the concavity. It indicates the variability in the concavity measurement.

Concave Points Error: This measures the standard error of the number of concave portions. It reflects the variability in this feature.

Symmetry Error: This is the standard error of the symmetry. It indicates how much the symmetry measurement varies.

Fractal Dimension Error: This measures the standard error of the fractal dimension. It shows the variability in the complexity of the cell boundary.

Worst Radius: This represents the largest mean value of radius among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Texture: This measures the largest mean value of texture among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Perimeter: This measures the largest mean value of the perimeter among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Area: This measures the largest mean value of the area among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Smoothness: This measures the largest mean value of smoothness among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Compactness: This measures the largest mean value of compactness among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Concavity: This measures the largest mean value of concavity among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Concave Points: This measures the largest mean value of the number of concave portions among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Symmetry: This measures the largest mean value of symmetry among the three largest cell measurements. It helps in identifying the most abnormal cells.

Worst Fractal Dimension: This measures the largest mean value of the fractal dimension among the three largest cell measurements. It helps in identifying the most abnormal cells.

## Features

- **Model Training**: Uses Logistic Regression with hyperparameter tuning via RandomizedSearchCV to find the best model for the user.
- **Scalability**: The model and scaler are saved and loaded using Joblib for efficient predictions.
- **Responsive Frontend**: A responsive web application built on React Java Script which allows for responsive design for mobile, tablet, and desktop platforms.
- **REST API**: A simple RESTful API is provided to handle prediction requests.


### Prerequisites

- Python 3.7+
- Node.js
- npm (Node Package Manager)


Mouhamed Mbengue

