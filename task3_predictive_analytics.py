"""
Task 3: Predictive Analytics for Resource Allocation
=====================================================
Breast Cancer Classification using Machine Learning
Analyze and predict cancer classification using Random Forest algorithm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, f1_score, classification_report, 
    confusion_matrix, precision_score, recall_score, 
    roc_auc_score, roc_curve
)
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
plt.style.use('default')
sns.set_palette("husl")

print("="*80)
print("TASK 3: PREDICTIVE ANALYTICS - BREAST CANCER CLASSIFICATION")
print("="*80)


# ============================================================================
# 1. LOAD AND EXPLORE THE DATASET
# ============================================================================

print("\n1. Loading and exploring dataset...")

data = load_breast_cancer()

# Create a DataFrame for easier manipulation
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print(f"Dataset Shape: {df.shape}")
print(f"\nTarget Distribution:")
print(df['target'].value_counts())
print(f"\nTarget Mapping: {data.target_names}")
print(f"  0 = Malignant (Bad)")
print(f"  1 = Benign (Good)")


# ============================================================================
# 2. DATA PREPROCESSING
# ============================================================================

print("\n2. Preprocessing data...")

# Check for missing values
missing_values = df.isnull().sum()
print(f"Missing Values: {missing_values.sum()}")
print(f"Duplicate Rows: {df.duplicated().sum()}")

# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split the data into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nSplit completed:")
print(f"  Training set: {X_train.shape}")
print(f"  Testing set:  {X_test.shape}")

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✓ Features scaled successfully")


# ============================================================================
# 3. VISUALIZATIONS
# ============================================================================

print("\n3. Creating visualizations...")

# Visualize target distribution
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
y.value_counts().sort_index().plot(kind='bar', color=['lightcoral', 'lightgreen'])
plt.title('Target Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Target Class', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks([0, 1], ['Malignant', 'Benign'], rotation=0)
plt.grid(axis='y', alpha=0.3)

plt.subplot(1, 2, 2)
y.value_counts().plot(kind='pie', autopct='%1.1f%%', 
                      colors=['lightcoral', 'lightgreen'],
                      labels=['Malignant', 'Benign'])
plt.title('Target Distribution Percentage', fontsize=14, fontweight='bold')
plt.ylabel('')

plt.tight_layout()
plt.savefig('task3_target_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: task3_target_distribution.png")

# Feature correlation heatmap
correlation_matrix = X_train.corr()
plt.figure(figsize=(14, 12))
# Use iloc to slice pandas DataFrame correctly
sns.heatmap(correlation_matrix.iloc[:20, :20], annot=False, cmap='coolwarm', center=0,
            square=True, linewidths=0.5)
plt.title('Feature Correlation Matrix (Top 20x20)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('task3_correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: task3_correlation_heatmap.png")


# ============================================================================
# 4. MODEL TRAINING - RANDOM FOREST CLASSIFIER
# ============================================================================

print("\n4. Training Random Forest model...")

rf_classifier = RandomForestClassifier(
    n_estimators=100,      # Number of trees
    max_depth=10,          # Maximum depth
    min_samples_split=5,   # Minimum samples to split
    min_samples_leaf=2,    # Minimum samples in leaf
    random_state=42,       # For reproducibility
    n_jobs=-1              # Use all CPUs
)

print("Random Forest Parameters:")
print(f"  - Number of trees: {rf_classifier.n_estimators}")
print(f"  - Max depth: {rf_classifier.max_depth}")
print(f"  - Min samples split: {rf_classifier.min_samples_split}")

# Train the model
rf_classifier.fit(X_train_scaled, y_train)
print("✓ Model training completed")


# ============================================================================
# 5. MODEL EVALUATION
# ============================================================================

print("\n5. Evaluating model performance...")

# Make predictions
y_train_pred = rf_classifier.predict(X_train_scaled)
y_test_pred = rf_classifier.predict(X_test_scaled)

# Calculate accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("\nAccuracy Scores:")
print(f"  Training Accuracy: {train_accuracy:.4f} ({train_accuracy*100:.2f}%)")
print(f"  Test Accuracy:     {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# Calculate F1-score
train_f1 = f1_score(y_train, y_train_pred)
test_f1 = f1_score(y_test, y_test_pred)

print("\nF1 Scores:")
print(f"  Training F1-score: {train_f1:.4f}")
print(f"  Test F1-score:     {test_f1:.4f}")

# Additional metrics
test_precision = precision_score(y_test, y_test_pred)
test_recall = recall_score(y_test, y_test_pred)

print("\nAdditional Metrics:")
print(f"  Precision: {test_precision:.4f}")
print(f"  Recall:    {test_recall:.4f}")

# Detailed classification report
print("\n" + "="*80)
print("DETAILED CLASSIFICATION REPORT")
print("="*80)
print(classification_report(y_test, y_test_pred, 
                          target_names=['Malignant', 'Benign'],
                          digits=4))


# Confusion Matrix
cm = confusion_matrix(y_test, y_test_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Malignant', 'Benign'], 
            yticklabels=['Malignant', 'Benign'],
            cbar_kws={'label': 'Count'})
plt.title('Confusion Matrix', fontsize=14, fontweight='bold')
plt.ylabel('True Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('task3_confusion_matrix.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: task3_confusion_matrix.png")

print("\nConfusion Matrix Breakdown:")
print(f"  True Negatives:  {cm[0][0]} (Correctly predicted Malignant)")
print(f"  False Positives: {cm[0][1]} (Wrongly predicted Benign, actually Malignant)")
print(f"  False Negatives: {cm[1][0]} (Wrongly predicted Malignant, actually Benign)")
print(f"  True Positives:  {cm[1][1]} (Correctly predicted Benign)")


# ============================================================================
# 6. FEATURE IMPORTANCE ANALYSIS
# ============================================================================

print("\n6. Analyzing feature importance...")

feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_classifier.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 10 Most Important Features:")
print(feature_importance.head(10))

# Visualize feature importance
plt.figure(figsize=(12, 8))
top_features = feature_importance.head(15)
plt.barh(range(len(top_features)), top_features['importance'], color='steelblue')
plt.yticks(range(len(top_features)), top_features['feature'])
plt.xlabel('Importance Score', fontsize=12)
plt.title('Top 15 Most Important Features', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('task3_feature_importance.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: task3_feature_importance.png")


# ============================================================================
# 7. ROC CURVE ANALYSIS
# ============================================================================

print("\n7. Creating ROC curve...")

y_test_proba = rf_classifier.predict_proba(X_test_scaled)[:, 1]
roc_auc = roc_auc_score(y_test, y_test_proba)

print(f"ROC AUC Score: {roc_auc:.4f}")

# Plot ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_test_proba)

plt.figure(figsize=(9, 7))
plt.plot(fpr, tpr, linewidth=2, label=f'Random Forest (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate', fontsize=12)
plt.title('ROC Curve - Breast Cancer Classification', fontsize=14, fontweight='bold')
plt.legend(loc='lower right', fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('task3_roc_curve.png', dpi=300, bbox_inches='tight')
print("✓ Saved: task3_roc_curve.png")


# ============================================================================
# 8. SUMMARY AND CONCLUSIONS
# ============================================================================

print("\n" + "="*80)
print("MODEL PERFORMANCE SUMMARY")
print("="*80)
print(f"\nTest Accuracy:     {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
print(f"Test F1-Score:     {test_f1:.4f}")
print(f"Test Precision:    {test_precision:.4f}")
print(f"Test Recall:       {test_recall:.4f}")
print(f"ROC AUC Score:     {roc_auc:.4f}")

print("\nMetric Interpretations:")
print("  Accuracy: Overall percentage of correct predictions")
print("  Precision: Of predicted benign cases, how many are actually benign")
print("  Recall: Of actual benign cases, how many were correctly identified")
print("  F1-Score: Harmonic mean of precision and recall")
print("  ROC AUC: Model's ability to distinguish between malignant and benign")

print("\n" + "="*80)
print("KEY TAKEAWAYS")
print("="*80)
print("1. Data Quality: Dataset was clean with no missing values")
print("2. Model Performance: Random Forest achieved excellent accuracy and F1-scores")
print("3. Feature Importance: Certain features contribute more to predictions")
print("4. Generalization: Test performance indicates good generalization")
print("5. Deployment Ready: Model shows strong predictive capability")

print("\n✓ Analysis completed successfully!")
print("="*80)


# Save results to CSV
results_df = pd.DataFrame({
    'Metric': ['Test Accuracy', 'Test F1-Score', 'Test Precision', 
               'Test Recall', 'ROC AUC Score'],
    'Value': [test_accuracy, test_f1, test_precision, test_recall, roc_auc]
})

results_df.to_csv('task3_performance_metrics.csv', index=False)
print("\n✓ Saved: task3_performance_metrics.csv")

