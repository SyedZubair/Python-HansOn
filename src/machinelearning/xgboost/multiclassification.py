import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create small dataset
data = {
    'weight_g': [120, 130, 200, 180, 140, 170],
    'size_cm': [5, 5.5, 8, 7, 6, 6.5],
    'fruit': [0, 0, 1, 1, 2, 2]  # 0=Apple, 1=Banana, 2=Orange
}
df = pd.DataFrame(data)

# Features and target
X = df[['weight_g', 'size_cm']]
y = df['fruit']

# Split data with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, stratify=y)

# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Predict for new fruit (150g, 6cm)
new_fruit = [[150, 6]]
fruit_names = {0: 'Apple', 1: 'Banana', 2: 'Orange'}
predicted_fruit = model.predict(new_fruit)[0]
print(f"Predicted fruit: {fruit_names[predicted_fruit]}")