# Application-Architecture-and-Deployment-Project
# Patient Readmission Prediction API

## Problem Statement
Hospitals and healthcare providers strive to minimize patient readmissions, as frequent readmissions can indicate ineffective treatment and lead to increased healthcare costs. Identifying high-risk patients at the time of discharge enables hospitals to optimize resource allocation and improve patient care. 

This project aims to build a **Patient Readmission Prediction API** that leverages machine learning to classify whether a patient is likely to be readmitted within **30 days** based on their medical data. 

## Data Source
The dataset used for this project is an open-source healthcare dataset or a synthetic dataset that includes:
- **Patient demographics** (e.g., age, gender)
- **Medical history** (e.g., previous diagnoses, lab test results)
- **Hospitalization details** (e.g., length of stay, number of procedures, medications prescribed)
- **Previous readmission records**

## Data Description
1. **time_in_hospital (Integer)** - Number of days the patient stayed in the hospital.
2. **n_lab_procedures (Integer)** - Total number of lab tests conducted during the hospital stay.
3. **n_procedures (Integer)** - Total number of medical procedures performed on the patient.
4. **n_medications (Integer)** - Number of different medications prescribed.
5. **n_outpatient (Integer)** - Number of outpatient visits before hospitalization.
6. **n_inpatient (Integer)** - Number of previous inpatient admissions.
7. **n_emergency (Integer)** - Number of emergency visits before hospitalization.
8. **medical_specialty (Hashed Integer)** - Encodes the specialty of the doctor/department.
9. **diag_1 (Hashed Integer)** - Primary diagnosis code, encoded using hashing.
10. **diag_2 (Hashed Integer)** - Secondary diagnosis code, hashed.
11. **diag_3 (Hashed Integer)** - Tertiary diagnosis code, hashed.
12. **glucose_test (Binary: 0 or 1)** - Indicates whether a glucose test was performed.
13. **A1Ctest (Binary: 0 or 1)** - Indicates whether an A1C test was performed.
14. **change (Binary: 0 or 1)** - Indicates whether medication was changed.
15. **diabetes_med (Binary: 0 or 1)** - Indicates whether diabetes medication was prescribed.

## Model and Explanation
For predicting patient readmission, we use the **Random Forest Classifier**.

### Why Random Forest?
Random Forest is an ensemble learning technique that combines multiple decision trees to improve accuracy and robustness. Here’s why we chose it:

- **Handles Non-Linearity:** Unlike logistic regression, Random Forest can capture complex patterns in the data.
- **Feature Importance:** It provides insights into which factors influence readmission most.
- **Handles Missing Data:** Unlike decision trees, it is less prone to overfitting and performs well with missing values.
- **Scalability:** Works efficiently with large datasets.

### Comparison with Logistic Regression
| Feature               | Random Forest                     | Logistic Regression             |
|----------------------|--------------------------------|--------------------------------|
| **Non-Linearity**   | Can capture complex relationships | Assumes a linear relationship  |
| **Overfitting**     | Less prone due to multiple trees  | More prone to overfitting      |
| **Feature Selection** | Provides feature importance ranking | Needs manual feature selection |
| **Handling Missing Data** | Handles missing values well | Requires imputation            |
| **Interpretability** | Less interpretable, but powerful | More interpretable, but limited |

Since patient readmission is influenced by multiple non-linear factors, **Random Forest** is preferred over **Logistic Regression** for better accuracy and robustness.

## Project Workflow
This project follows a structured pipeline for development and deployment:

1️⃣ **Develop the Flask API (`app.py`)**
2️⃣ **Dockerize the Application**
3️⃣ **Deploy the API using Docker Hub**
4️⃣ **Deploy the API on AWS EC2**

## Features
✅ Accepts patient data via a JSON request.
✅ Preprocesses input features.
✅ Predicts hospital readmission using a trained ML model.
✅ Returns both the prediction outcome and probability score.
✅ Deployed as a **REST API**.

## Project Structure
```
/your_project_directory
│── app.py                      # Flask application
│── Application_Architecture_Project.ipynb  # Jupyter Notebook for model training
│── Dockerfile                   # Docker configuration
│── hospital_readmissions.csv     # Dataset for model training
│── project-key.pem               # Security key for AWS
│── readmission_model.pkl         # Trained ML model
│── requirements.txt              # Dependencies
│── train_test_data.pkl           # Preprocessed train-test split data
```

## Installation
### Prerequisites
Ensure you have **Python 3** installed on your system.

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Running the API Locally
```bash
python app.py
```
API will be available at `http://127.0.0.1:5000/`.

### API Endpoints
#### 1️⃣ Home Page
- **Endpoint**: `/`
- **Method**: `GET`
- **Response**: Renders the home page

#### 2️⃣ Prediction Endpoint
- **Endpoint**: `/predict`
- **Method**: `POST`
- **Request Body (JSON)**:
  ```json
  {
    "age": 65,
    "time_in_hospital": 5,
    "n_lab_procedures": 50,
    "n_procedures": 1,
    "n_medications": 12,
    "n_outpatient": 0,
    "n_inpatient": 1,
    "n_emergency": 0,
    "medical_specialty": "Cardiology",
    "diag_1": "250.02",
    "diag_2": "401.9",
    "diag_3": "272.4",
    "glucose_test": 1,
    "A1Ctest": 0,
    "change": "Yes",
    "diabetes_med": "Yes"
  }
  ```
- **Response (JSON)**:
  ```json
  {
    "readmitted": "Yes",
    "probability": 0.85
  }
  ```

## Docker Setup
To containerize and run the API using Docker:
```bash
docker build -t readmission-api .
docker run -p 5000:5000 readmission-api
```

## Deployment
### Deploying to Docker Hub
```bash
docker tag readmission-api <your-dockerhub-username>/readmission-api
docker push <your-dockerhub-username>/readmission-api
```

### Deploying on AWS EC2
```bash
ssh -i project-key.pem ec2-user@<EC2-Public-IP>
docker pull <your-dockerhub-username>/readmission-api
docker run -p 5000:5000 <your-dockerhub-username>/readmission-api
```

## Technologies Used
🚀 **Flask**  📊 **NumPy & Pandas**  🧠 **Scikit-learn**  🐳 **Docker**  ☁️ **AWS EC2**

## Contributors
👨‍💻 **Smit Shah, Ajwad Ansari, Bhavyam Ramani, Swarangi**

## License
This project is licensed under the MIT License.
