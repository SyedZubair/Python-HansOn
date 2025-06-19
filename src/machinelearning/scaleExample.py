import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#1. Generates some sample data
np.random.seed(2)
X = np.random.normal(3, 1,(100,2)) #100 samples, 20 features
y = (X[:,0] + X[:,1] > 6).astype(int) # Binary lables on features

#2. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

#3. Initialize the scaler
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=2)
model.fit(X_train_scaled, y_train)

#4. Prediction
y_pred = model.predict(X_test_scaled)

#5. Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the model is: ",accuracy)


plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.scatter(X_train[:,0], X_train[:,1],c=y_train, cmap='bwr', alpha=0.6)
plt.title('Original Training Data')
plt.xlabel('Feature 1')
plt.xlabel('Feature 2')


plt.subplot(1,2,2)
plt.scatter(X_train_scaled[:,0], X_train_scaled[:,1],c=y_train, cmap='bwr', alpha=0.6)
plt.title('Scaled Training Data')
plt.xlabel('Feature 1')
plt.xlabel('Feature 2')

plt.tight_layout()
plt.show()