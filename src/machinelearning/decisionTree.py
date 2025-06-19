import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import seaborn as sns


#Feature: [hours, attendance %]
#Target: (P (1), F(0))

X = np.array([
        [2,70], #fail 0
        [3,85], #pass 1
        [1,60], #fail 0
        [4,90], #pass 1
        [2,65], #fail 0
        [5,95], #pass 1
        [3,80], #pass 1
        [4,88], #pass 1
        [2,75], #fail 0
        [3,86], #pass 1
])

y = np.array([0,1,0,1,0,1,1,1,0,1])

X_train  = X[:8]
X_test  = X[8:]
y_train  = y[:8]
y_test  = y[8:]

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

model = DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(x_train_scaled, y_train)

#prediction
y_pred = model.predict(x_test_scaled)

#accuracy
accuracy = accuracy_score(y_test, y_pred)

confMatrix = metrics.confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(confMatrix, annot=True, fmt='d', cmap='Purples', cbar=False,
            xticklabels= ['Fail', 'Pass'], yticklabels=['Fail', 'Pass'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

#Decision Tree
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=['Hours','Attendance %'], 
          class_names=['Fail', 'Pass'], filled=True, rounded=True, fontsize=10)
plt.title('Decision Tree')
plt.show()