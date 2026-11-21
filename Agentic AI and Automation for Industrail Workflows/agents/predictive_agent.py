import os 
import joblib

class PredictiveAgent:

    def __init__(self, name):
        self.name = name
        self.model = None

    def train_model(self):
        print("[Predictive Agent] Loading trained ML model...")
        
        # Load your trained model
        model_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "machine_model.pkl"))

        print("Model path:", model_path)

        self.model = joblib.load(model_path)

        print("[Predictive Agent] Model loaded successfully!")

    def predict_next(self, temperature, vibration, usage_hours):
        
        if self.model is None:
            raise Exception("Model not loaded. Call train_model() first.")

        # Prepare input for prediction
        data = [[temperature, vibration, usage_hours]]

        prediction = self.model.predict(data)[0]

        # Convert output to meaningful result
        if prediction == 1:
            decision = "Maintenance Required"
        else:
            decision = "No Maintenance Needed"

        return {
            "decision": decision,
            "reasons": [
                f"Temperature: {temperature}",
                f"Vibration: {vibration}",
                f"Usage Hours: {usage_hours}",
                "Prediction based on ML model"
            ]
        }
