import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("machine_training_data.csv")

X = df[["temperature", "vibration", "usage_hours"]]
y = df["failure"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "machine_failure_model.pkl")
print("ML model trained and saved")
