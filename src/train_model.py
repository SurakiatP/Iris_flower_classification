import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

#Load Data
df = pd.read_csv("../data/processed/iris_cleaned.csv")

#select feature, labels
X = df.drop(columns=["Species"])
y = df["Species"]

#spilt data for test, train model
X_test, X_train, y_test, y_train = train_test_split(X, y ,test_size=0.2, random_state=42)

#train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Evaluate the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

#save model
joblib.dump(model, "../models/iris_model.pkl")