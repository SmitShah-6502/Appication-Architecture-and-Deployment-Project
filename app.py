# from flask import Flask, render_template, request, jsonify
# import pickle
# import numpy as np

# app = Flask(__name__)

# # Load the trained model (including preprocessing if available)
# with open("readmission_model (1).pkl", "rb") as file:
#     model = pickle.load(file)

# # Extract the scaler from the model pipeline (if the model is a pipeline)
# scaler = None
# if hasattr(model, "named_steps"):  # If using a Pipeline
#     scaler = model.named_steps.get("scaler")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.get_json()

#         # Prepare feature values
#         age = np.array([[int(data["age"])]])
        
#         # Scale the age value if the model contains a scaler
#         if scaler:
#             age_scaled = scaler.transform(age).flatten()[0]
#         else:
#             age_scaled = age[0][0]  # Use the original value if no scaler exists

#         # Extract and transform other values
#         features = [
#             age_scaled,  # Use scaled age if available
#             int(data["time_in_hospital"]),
#             int(data["n_lab_procedures"]),
#             int(data["n_procedures"]),
#             int(data["n_medications"]),
#             int(data["n_outpatient"]),
#             int(data["n_inpatient"]),
#             int(data["n_emergency"]),
#             hash(data["medical_specialty"]) % 1000,
#             hash(data["diag_1"]) % 1000,
#             hash(data["diag_2"]) % 1000,
#             hash(data["diag_3"]) % 1000,
#             int(data["glucose_test"]),
#             int(data["A1Ctest"]),
#             1 if data["change"] == "Yes" else 0,
#             1 if data["diabetes_med"] == "Yes" else 0
#         ]

#         # Convert to NumPy array and reshape
#         features = np.array(features).reshape(1, -1)

#         # Make prediction
#         prediction = model.predict(features)[0]
#         result = "Yes" if prediction == 1 else "No"

#         return jsonify({"readmitted": result})
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

# # AWS Link http://107.21.82.110:5000/

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model (including preprocessing if available)
with open("readmission_model (1).pkl", "rb") as file:
    model = pickle.load(file)

# Extract the scaler from the model pipeline (if the model is a pipeline)
scaler = None
if hasattr(model, "named_steps"):  # If using a Pipeline
    scaler = model.named_steps.get("scaler")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Prepare feature values
        age = np.array([[int(data["age"])]])
        age_scaled = scaler.transform(age).flatten()[0] if scaler else age[0][0]

        features = [
            age_scaled,  
            int(data["time_in_hospital"]),
            int(data["n_lab_procedures"]),
            int(data["n_procedures"]),
            int(data["n_medications"]),
            int(data["n_outpatient"]),
            int(data["n_inpatient"]),
            int(data["n_emergency"]),
            hash(data["medical_specialty"]) % 1000,
            hash(data["diag_1"]) % 1000,
            hash(data["diag_2"]) % 1000,
            hash(data["diag_3"]) % 1000,
            int(data["glucose_test"]),
            int(data["A1Ctest"]),
            1 if data["change"] == "Yes" else 0,
            1 if data["diabetes_med"] == "Yes" else 0
        ]

        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]
        result = "Yes" if prediction == 1 else "No"

        # Get probability between 0 and 1
        if hasattr(model, "predict_proba"):
            proba_values = model.predict_proba(features)
            probability = round(proba_values[0][1]*100, 2)  # Keep probability in range [0,1]
        else:
            probability = "Not Available"

        return jsonify({
            "readmitted": result,
            "probability": probability
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
