import joblib
import numpy as np

# load model
model = joblib.load("../models/iris_model.pkl")

# test model by new data(ideal)
new_sample = np.array([[6.0,3.4,4.5,1.6]])

# prediction
prediction = model.predict(new_sample)
print(f"Predicted species: {prediction[0]}")
