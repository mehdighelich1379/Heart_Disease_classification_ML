### Heart Disease Prediction Project using heart.csv Dataset

# Heart Disease Prediction App

This is a machine learning web app to predict heart disease based on patient input data.

🔗 Live Demo: [Click here to use the app]([https://heart-disease-ml-mehdighelich.streamlit.app](https://heart-disease-classification-ml-mehdighelich.streamlit.app))

📷 App Preview:

![App Screenshot](images/heart_app_screenshot.jpg)  <!-- این مسیر باید با اسم فایلت یکی باشه -->

Try the Live App https://heart-disease-classification-ml-mehdighelich.streamlit.app


# Heart Disease Prediction
This is a machine learning model to predict heart disease based on patient data. You can interact with the app directly here:






#### Dataset Overview:
The heart.csv dataset contains a variety of medical attributes that are used to predict whether a person has heart disease. The dataset consists of the following columns:

1. age: The age of the patient.
2. sex: Gender of the patient (male or female).
3. cp: Chest pain type experienced by the patient.
4. trestbps: Resting blood pressure (in mm Hg).
5. chol: Serum cholesterol level.
6. fbs: Fasting blood sugar level (1 if greater than 120 mg/dl, else 0).
7. restecg: Resting electrocardiographic results.
8. thalach: Maximum heart rate achieved during exercise.
9. exang: Whether the patient experienced exercise-induced angina (1 if yes, 0 if no).
10. oldpeak: Depression induced by exercise relative to rest.
11. slope: The slope of the peak exercise ST segment.
12. ca: Number of major vessels colored by fluoroscopy.
13. thal: A blood disorder associated with heart disease (3 = normal; 6 = fixed defect; 7 = reversible defect).
14. target: The target variable indicating whether the patient has heart disease (1 = heart disease, 0 = no heart disease).

---

### Project Steps:

1. Exploratory Data Analysis (EDA):
   - I started by performing EDA to analyze the structure of the dataset and the relationships between the features. This helped identify patterns and detect any issues such as missing data.
   - After examining the dataset, I found that there were no missing values in the features.

2. Data Visualization:
   - I visualized the features to gain insights into the distribution and relationships between them:
     - The fbs (Fasting Blood Sugar) column was visualized using a displacement plot to understand its distribution.
     - The chol (Cholesterol) column was also visualized using a similar displacement plot to understand the distribution of cholesterol levels.

3. Data Scaling:
   - I applied StandardScaler to scale the data so that the features were on the same scale, which is important for models like SVM and others that rely on distance calculations.

4. Data Splitting:
   - The dataset was split into training and testing sets using a 75-25 split (75% for training and 25% for testing).

5. Noise Removal using LOF (Local Outlier Factor):
   - To improve the quality of the data, I used the LOF (Local Outlier Factor) technique to remove noisy data points. This helps in eliminating outliers that could distort the model's learning process.

6. Balancing the Data with SMOTETomek:
   - The dataset was imbalanced (more healthy patients than those with heart disease). To address this, I applied SMOTETomek, which combines the SMOTE technique (oversampling the minority class) with Tomek Links (removing redundant samples from the majority class) to balance the dataset.

7. Hyperparameter Tuning using Grid Search:
   - I performed Grid Search on the SVC (Support Vector Classifier) algorithm to find the best hyperparameters.
   - After tuning the parameters, the model achieved 93% accuracy on the test data.
   - I then plotted the Confusion Matrix, which showed the following:
     - 24 instances were correctly predicted as non-diseased (healthy).
     - 4 healthy instances were wrongly predicted as diseased.
     - 27 diseased instances were correctly predicted as diseased.

8. ROC Curve:
   - I plotted the ROC Curve, which showed an AUC of 93%, indicating that the SVC model performed well in distinguishing between healthy and diseased patients.

9. CatBoost Algorithm:
   - To explore whether another algorithm would improve accuracy, I used CatBoost, a gradient boosting algorithm.
   - The model was configured with the following parameters:

- Learning rate: 0.05
     - Max Depth: 8
     - Metric: Recall
     - Bagging temperature: 0.2
     - OD type: Iter
     - Metric period: 75
     - OD wait: 100
     - Random state: 42
   - The CatBoost model achieved 100% accuracy on the training data and 96% accuracy on the test data.

10. Confusion Matrix (CatBoost):
    - For the CatBoost model, the Confusion Matrix showed:
      - 26 healthy instances were correctly predicted as healthy.
      - 0 diseased patients were predicted as healthy (no false negatives).
      - 2 healthy patients were wrongly predicted as diseased.
      - 27 diseased patients were correctly predicted as diseased.

11. Cross-Validation:
    - I performed cross-validation to ensure the robustness of the CatBoost model. The results were consistent with the performance on the test data.

12. Feature Importance (CatBoost):
    - I plotted the Feature Importance to identify which features were the most influential in predicting heart disease. Features such as age, thalach (maximum heart rate), and chol (cholesterol) were identified as the most important.

13. ROC Curve (CatBoost):
    - I also plotted the ROC Curve for the CatBoost model, which showed an AUC of 96%, indicating excellent model performance.

14. Model Saving:
    - Finally, I saved both the SVC and CatBoost models along with the StandardScaler used for scaling the data, so that they can be reused in the future.

---

### Conclusion:

This project demonstrates how machine learning techniques can be applied to predict heart disease based on medical features. The SVC algorithm performed well with a 93% accuracy on the test data, and the CatBoost model outperformed it with 96% accuracy. Techniques like SMOTETomek for balancing the data, LOF for noise removal, and Grid Search for hyperparameter tuning helped improve the overall performance. The final models, SVC and CatBoost, are both robust and ready for deployment in healthcare applications for heart disease prediction.

---

### Skills Demonstrated:
1. Data Preprocessing: Handling missing data, scaling features, and encoding categorical variables.
2. Feature Engineering: Balancing the dataset using SMOTETomek and feature importance analysis.
3. Model Building: Implementing and tuning models like SVC and CatBoost for classification tasks.
4. Hyperparameter Tuning: Using Grid Search to find the optimal hyperparameters for models.
5. Model Evaluation: Evaluating models using metrics like accuracy, confusion matrix, ROC curve, and AUC.
6. Model Deployment: Saving models and scalers for future use.

This project showcases a solid understanding of the machine learning pipeline, from data preprocessing to model evaluation, and provides a good foundation for applying machine learning in real-world healthcare scenarios.
