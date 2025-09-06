# Machine Learning 

# Credit-card-fraud-detection
To develop a machine learning model capable of detecting fraudulent credit card transactions based on transaction data. The goal is to build a reliable classifier that can identify fraudulent activity with high precision and recall, even with imbalanced datasets.

# Dataset :

The dataset used is the Credit Card Fraud Detection dataset from Kaggle. It contains 284,807
transactions made by European cardholders in September 2013. Among these, only 492 are
fraudulent, making the dataset highly imbalanced. The features are anonymized using PCA

# Challenges :

 Imbalanced Data: Very few fraud cases compared to non-fraudulent ones. 
 
 High Dimensionality: Many features may be redundant or less important.
 
 Real-time Detection Need: Fraud needs to be caught as early as possible.
 
 Data Sensitivity: Financial data must be handled securely

# Methodology :

1. Preprocessing
• Loaded the dataset using pandas

• Checked for null values and data types

• Normalized the Amount and Time features using StandardScaler

• Split the data into training and test sets using train_test_split

• Addressed class imbalance using under-sampling or other techniques (if applied)

2. Model Training
• Logistic Regression

• Random Forest Classifier

3. Model Evaluation
• Confusion Matrix: to analyze true positives, false positives, etc.

• Classification Report: recall, and F1-score

• ROC-AUC Score: to evaluate the quality of predictions across thresholds

• Accuracy Score: overall prediction accuracy

# Results :

• Best-performing model: [0.9152218782249741]

• High recall and precision indicate effective fraud detection

• False positive rate was minimized, preserving customer experience

# Conclusion :

This project successfully demonstrates the application of machine learning for fraud detection
in highly imbalanced datasets. The results indicate that with proper preprocessing and model
selection, fraud can be detected with high accuracy.

# Future work :

• Applying advanced techniques like SMOTE or ensemble learning

• Real-time fraud detection pipeline integration

• Cost-sensitive learning to penalize false negatives
