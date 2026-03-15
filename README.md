# end-to-end-data-science-project
End-to-end data science project including data preprocessing, machine learning model training, and deployment using a Flask API for prediction.
# Task 3 – End-to-End Data Science Project

## Internship Details

**Company:** CODTECH IT Solutions
**Intern Name:** Arun Dharwad
**Intern ID:** CTIS6102
**Domain:** Data Science
**Duration:** 6 Weeks
**Mentor:** Neela Santosh

---

## Objective

The objective of this task is to develop a **complete data science project**, starting from data collection and preprocessing to training a machine learning model and deploying it using a **Flask API**.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* Pickle

---

## Project Description

**Student Performance Prediction System**

This project predicts whether a student will **Pass or Fail** based on the following features:

* Study Hours
* Attendance
* Previous Score

The trained machine learning model is deployed using a **Flask API**, allowing users to send input data and receive predictions.

---

## Workflow

1. Data collection and preparation
2. Data preprocessing using Pandas
3. Train machine learning model using Scikit-learn
4. Save trained model using Pickle
5. Build Flask API for prediction
6. Deploy and test the API locally

---

## Project Structure

```
end-to-end-data-science-project
│
├── dataset.csv
├── train_model.py
├── app.py
├── model.pkl
└── README.md
```

---

## How to Run the Project

### 1. Train the Model

```bash
python train_model.py
```

This will generate the trained model file:

```
model.pkl
```

### 2. Run the Flask Application

```bash
python app.py
```

The API will start running at:

```
http://127.0.0.1:5000/
```

---

## API Usage Example

Send a POST request to:

```
/predict
```

Example JSON input:

```json
{
 "hours": 6,
 "attendance": 85,
 "previous_score": 70
}
```

Example response:

```json
{
 "Prediction": "Pass"
}
```

---

## Conclusion

This project demonstrates a **complete machine learning lifecycle**, including data preprocessing, model training, and deployment using a Flask API. It shows how machine learning models can be integrated into real-world applications.

---

## Author

**Arun Dharwad**
MCA Student | Aspiring Data Scientist

#OUTPUT

<img width="525" height="313" alt="Image" src="https://github.com/user-attachments/assets/9b214cdc-1094-4bc9-b6ad-64e214bcae22" />
<img width="727" height="203" alt="Image" src="https://github.com/user-attachments/assets/c3df3777-deb4-4bb3-8130-1fffb1fdc538" />
