# CHD (Coronary Heart Disease) Prediction Project

<img src="https://raw.githubusercontent.com/Rajivjha003/Cardiovascular-Risk-Prediction/feature/cardiovasculardisease/Coronary-Heart-DiseaseImg.png" alt="CHD Img">

## Overview
This project aims to develop an advanced predictive model for detecting Coronary Heart Disease (CHD) using machine learning techniques. CHD is a critical health condition affecting millions worldwide, and accurate early detection is crucial for timely intervention and improved patient outcomes.

## Project Structure
- **data**
  - *chd_data.csv*
- **Project Root**
  - *data_analysis*
  - *data_preprocessing*
  - *feature_engineering*
  - *model_training*
  - *model_evaluation*
  - *prediction*
  - *saving_model.pkl*
  - *model.py*
  - *requirements.txt*
  - *app.py*
  - *docker*
  - *deployment*
  - *README.md*

## Dataset
The dataset used in this project consists of a diverse set of features related to patients' health profiles, lifestyle habits, and medical history. It is collected from reputable medical sources and preprocessed to handle missing values and ensure data integrity.

## Software and Tools Requirement
1. [GitHub Account](https://github.com)
2. [Render Account](https://render.com)
3. [VSCode IDE](https://code.visualstudio.com)
4. [Git CLI](https://git-scm.com/docs/gitcli)
5. Python
6. NumPy
7. Pandas
8. Scikit-learn
9. TensorFlow
10. Keras

## Methods
The CHD prediction model employs a combination of machine learning algorithms, including logistic regression, decision trees, random forests, and neural networks. It involves the following steps:
1. Data Preprocessing: Handle missing values, scale numerical features, and encode categorical variables.
2. Model Development: Utilize logistic regression, decision trees, and random forests for initial predictions.
3. Ensemble Learning: Implement model stacking and/or gradient boosting to combine individual model predictions.
4. Hyperparameter Tuning: Conduct an extensive search for optimal hyperparameters to improve model accuracy.
5. Model Evaluation: Assess the model's performance using evaluation metrics such as accuracy, precision, recall, and F1-score.

## Flask API and Dockerization
To make the CHD prediction model accessible as an API, I created a Flask application. The Flask API allows users to interact with the model and obtain predictions through simple HTTP requests. Additionally, I containerized the Flask application using Docker, ensuring easy deployment and scalability across different platforms and environments.

## Continuous Integration and Continuous Deployment (CI/CD)
For a streamlined development process, I set up a CI/CD pipeline using YAML configuration files. The CI/CD pipeline automates the build, testing, and deployment processes, ensuring that the application is thoroughly tested and deployed efficiently.

## Deployment on Render Server
The CHD prediction model was successfully deployed on the Render server, providing a live and accessible endpoint for users to access the Flask API.
# Link to Result- 
https://cardiovascular-risk-prediction.onrender.com/

## Screenshot

<img src="https://raw.githubusercontent.com/Rajivjha003/Cardiovascular-Risk-Prediction/feature/cardiovasculardisease/Screenshot%20CHD2.png" alt="Screenshot of Deployed Result">
<img src="https://raw.githubusercontent.com/Rajivjha003/Cardiovascular-Risk-Prediction/feature/cardiovasculardisease/Screenshot%20CHD1.png" alt="Screenshot of Deployed Result 2">

## Results
The CHD prediction model demonstrates remarkable accuracy, achieving an impressive 86% in detecting the likelihood of CHD. The ensemble of machine learning algorithms and data preprocessing techniques ensures robustness and generalizability of the model on diverse datasets.

## Conclusion
The CHD prediction project showcases the power of machine learning in early detection of critical health conditions like Coronary Heart Disease. The accurate predictive model has the potential to revolutionize healthcare by enabling timely interventions and personalized treatment strategies for patients at risk of CHD.

Step into the heart of the CHD Prediction Project, where innovation and compassion collide to empower hearts and transform lives. Together, let us revolutionize healthcare with the gift of early detection and a brighter future. 🌟🚀

---
