import os
import pickle
import numpy as np

# Compute the absolute path to the model file.
# Assumes the model is located in the "model" directory at the project root.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model', 'heart_disease_model.pkl')

# Load the model once when the module is imported.
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def make_prediction(features):
    """
    Accepts a list of features and returns a prediction.
    The list should be in the order expected by the model.
    """
    # Convert the list to a numpy array and reshape for one sample.
    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)
    
    # Assuming binary classification: 1 indicates high risk, 0 indicates low risk.
    if prediction[0] == 1:
        result = "The Person has Heart Disease."
    else:
        result = "The Person does not have a Heart Disease."
    return result
