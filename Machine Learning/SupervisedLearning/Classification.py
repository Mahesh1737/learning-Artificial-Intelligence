from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Step 1: Sample actual and predicted values
#1 - Positive class, Negative class
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1] # actual
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1] # predicted
#Step 2: Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)
FP = cm[0][1]
TP = cm[1][1]
TN = cm[0][0]
FN = cm[1][0]

print("Confusion Matrix:")
print(cm)


print("TP-(TP), TN-(TN), ΓΡ-(FP), TN-{FN}")


#Step 3: Manual calculation
accuracy = (TP + TN) / (TP + TN + FP + FN)
print("\n--- Manual Calculation---")
print(f"Accuracy: {accuracy:.2f}")

precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

#Step 4: Sklearn calculation
print("\n Sklearn Metrics---")
print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Pred 0", "Pred 1"], yticklabels=["Act 0", "Act 1"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()