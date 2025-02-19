from sklearn.metrics import classification_report
import joblib
import pandas as pd

# Load model
model = joblib.load("../models/iris_model.pkl")

# Load Spacific Cleaned Data
df = pd.read_csv("../data/processed/iris_cleaned.csv")
X = df.drop("Species", axis=1)
y = df["Species"]

# predict
y_pred = model.predict(X)

# report result
print(classification_report(y, y_pred))
