# Appication-Architecture-and-Deployment-Project
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

## Project Workflow
This project follows a structured pipeline for development and deployment:

1️⃣ **Develop the Flask API (`app.py`)**: 
   - The API accepts patient details (e.g., age, diagnosis, hospital stay duration, and test results).
   - It processes the input and returns a prediction on whether the patient is likely to be readmitted within 30 days.
   
2️⃣ **Dockerize the Application**:
   - Containerize the Flask API using Docker.
   - Test the container locally to ensure smooth execution.
   
3️⃣ **Deploy the API using Docker Hub**:
   - Push the Docker image to Docker Hub.
   - Pull and run the container from Docker Hub on a new machine.
   
4️⃣ **Deploy the API on AWS EC2**:
   - Configure an AWS EC2 instance.
   - Pull the Docker image and run the API, making it accessible via the cloud.

## Features
✅ Accepts patient data via a JSON request.
✅ Preprocesses input features (e.g., encoding categorical values, scaling numerical data).
✅ Predicts hospital readmission using a trained machine learning model.
✅ Returns both the prediction outcome and probability score (if available).
✅ Deployed as a **REST API** for seamless integration.

## Project Structure
```
/your_project_directory
│── app.py                      # Flask application
│── Application_Architecture_Project.ipynb  # Jupyter Notebook for model training & exploration
│── Dockerfile                   # Docker configuration
│── hospital_readmissions.csv     # Dataset for model training
│── project-key.pem               # Security key (for AWS deployment)
│── readmission_model.pkl         # Trained ML model
│── requirements.txt              # Dependencies
│── train_test_data.pkl           # Preprocessed train-test split data
```

## Installation
### Prerequisites
Ensure you have **Python 3** installed on your system.

### Install Dependencies
Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
### Running the API Locally
To start the Flask API locally, run:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/`.

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
1. **Build the Docker image**:
   ```bash
   docker build -t readmission-api .
   ```
2. **Run the container locally**:
   ```bash
   docker run -p 5000:5000 readmission-api
   ```

## Deployment
### Deploying to Docker Hub
1. **Tag the Docker image**:
   ```bash
   docker tag readmission-api <your-dockerhub-username>/readmission-api
   ```
2. **Push the image to Docker Hub**:
   ```bash
   docker push <your-dockerhub-username>/readmission-api
   ```

### Deploying on AWS EC2
1. **SSH into your EC2 instance**:
   ```bash
   ssh -i project-key.pem ec2-user@<EC2-Public-IP>
   ```
2. **Pull the Docker image from Docker Hub**:
   ```bash
   docker pull <your-dockerhub-username>/readmission-api
   ```
3. **Run the container on EC2**:
   ```bash
   docker run -p 5000:5000 <your-dockerhub-username>/readmission-api
   ```

## Technologies Used
🚀 **Flask**: Web framework for building the API.
📊 **NumPy & Pandas**: Data handling and preprocessing.
🧠 **Scikit-learn**: Machine learning model training and inference.
🐳 **Docker**: Containerization for scalable deployment.
☁️ **AWS EC2**: Cloud hosting for making the API accessible globally.

## Contributors
👨‍💻 **Smit Shah , Ajwad Ansari , Bhavyam Ramani , Swarangi**

## License
This project is licensed under the MIT License.

