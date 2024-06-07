import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import numpy as np

data = pd.read_csv('/Users/liyinqiao/Desktop/CSCI933 ML/Assignment02/Dataset-pima-indians-diabetes.csv', comment='#', header=None)
data.columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
    'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
]

# Preprocessing
min_glucose = data['Glucose'][data['Glucose'] > 0].min()
data['Glucose'] = data['Glucose'].replace(0, min_glucose)

min_insulin = data['Insulin'][data['Insulin'] > 0].min()
data['Insulin'] = data['Insulin'].replace(0, min_insulin)

# Feature Creation
data['Insulin_to_Glucose_Ratio'] = data['Insulin'] / data['Glucose']
data['Age_Pregnancy_Interaction'] = data['Age'] * data['Pregnancies']
data['BloodPressure_BMI_Interaction'] = data['BloodPressure'] * data['BMI']


# Scaler
scaler = StandardScaler()
X = scaler.fit_transform(data.drop('Outcome', axis=1))
y = data['Outcome'].values

# Train and Test Set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=99, stratify=y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=99, stratify=y)
# 41


# Find the best K value
best_k = 1
best_score = 0

for k in range(1, 26):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    mean_score = scores.mean()
    if mean_score > best_score:
        best_score = mean_score
        best_k = k

print(f"Best K Value: {best_k} with accuracy: {best_score}")

# Train KNN
knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train, y_train)
knn_predictions = knn_best.predict(X_test)
print("KNN classification report:")
print(classification_report(y_test, knn_predictions))

# Train LR
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_predictions = lr.predict(X_test)
print("Logistic Regression classification report:")
print(classification_report(y_test, lr_predictions))

# Train SVM
svc = SVC(probability=True)  # 设置probability=True以便后续使用.predict_proba
svc.fit(X_train, y_train)
svc_predictions = svc.predict(X_test)
print("Support Vector Machine classification report:")
print(classification_report(y_test, svc_predictions))

from sklearn.metrics import confusion_matrix, accuracy_score

# KNN
knn_accuracy = accuracy_score(y_test, knn_predictions)
print(f"KNN Accuracy: {knn_accuracy}")
knn_confusion_matrix = confusion_matrix(y_test, knn_predictions)
print("KNN Confusion Matrix:")
print(knn_confusion_matrix)

# Store KNN result
pd.DataFrame(knn_confusion_matrix).to_csv('knn_confusion_matrix.csv', index=False)

# LR
lr_accuracy = accuracy_score(y_test, lr_predictions)
print(f"Logistic Regression Accuracy: {lr_accuracy}")
lr_confusion_matrix = confusion_matrix(y_test, lr_predictions)
print("Logistic Regression Confusion Matrix:")
print(lr_confusion_matrix)

# Store LR result
pd.DataFrame(lr_confusion_matrix).to_csv('logistic_regression_confusion_matrix.csv', index=False)

# SVM
svc_accuracy = accuracy_score(y_test, svc_predictions)
print(f"SVM Accuracy: {svc_accuracy}")
svc_confusion_matrix = confusion_matrix(y_test, svc_predictions)
print("SVM Confusion Matrix:")
print(svc_confusion_matrix)

# Store SVM result
pd.DataFrame(svc_confusion_matrix).to_csv('svm_confusion_matrix.csv', index=False)

# Store All result in One CSV
accuracies = {
    'KNN': knn_accuracy,
    'Logistic_Regression': lr_accuracy,
    'SVM': svc_accuracy
}
pd.DataFrame.from_dict(accuracies, orient='index', columns=['Accuracy']).to_csv('model_accuracies(improved).csv')