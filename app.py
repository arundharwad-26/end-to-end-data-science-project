from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Student Performance Prediction API is running"

@app.route("/predict")
def predict():
    hours = float(request.args.get("hours"))
    attendance = float(request.args.get("attendance"))
    previous_score = float(request.args.get("previous_score"))

    features = np.array([[hours, attendance, previous_score]])
    prediction = model.predict(features)[0]

    return jsonify({"predicted_score": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True)