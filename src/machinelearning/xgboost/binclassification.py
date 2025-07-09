import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create small dataset
data = {
    'study_hours': [1, 2, 4, 5, 3, 6],
    'sleep_hours': [5, 4, 6, 7, 3, 8],
    'pass': [0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Features and target
X = df[['study_hours', 'sleep_hours']]
y = df['pass']

# Split data (use 2 samples for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Predict for new student (3 study hours, 6 sleep hours)
new_student = [[3, 6]]
print(f"New student prediction (pass=1, fail=0): {model.predict(new_student)[0]}")