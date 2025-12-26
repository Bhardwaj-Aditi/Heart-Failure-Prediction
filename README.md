# Heart Failure Risk Prediction Web Application

A web-based Machine Learning application that predicts the risk of heart failure using patient clinical data.  
The system is built using **Logistic Regression** and deployed through a **Flask** web framework to support early risk assessment.

## Project Objective

To design and implement a Machine Learning–based web application that estimates the probability of heart failure based on relevant medical parameters, enabling data-driven decision support.


## Technology Stack

| Component | Description |

| Python | Core programming language |
| Flask | Web application framework |
| Scikit-learn | Machine Learning (Logistic Regression) |
| Pandas, NumPy | Data preprocessing and manipulation |
| HTML, CSS | Frontend user interface |
| Pickle | Model serialization |


## Key Features

- Logistic Regression model trained on clinical patient data  
- Predicts heart failure risk as a binary outcome  
- Web-based input form for medical attributes:
  - Age
  - Anaemia
  - High Blood Pressure
  - Ejection Fraction
  - Serum Creatinine
  - Serum Sodium
  - Diabetes
  - Smoking
  - Sex
  - Follow-up Time
- Feature scaling using `StandardScaler`
- Lightweight and user-friendly Flask interface
- Pre-trained model loaded for fast predictions


## Dataset Information

Dataset used: **Heart Failure Clinical Records Dataset**  
(Source: Kaggle)

- Total records: 299
- Clinical features: 13
- Target variable:
  - `0` → No heart failure
  - `1` → Risk of heart failure

The dataset contains real-world clinical data and is widely used for academic research and experimentation.


