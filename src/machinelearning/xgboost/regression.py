import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create small dataset
data = {
    'size_sqft': [800, 1000, 1200, 1500, 900],
    'bedrooms': [2, 3, 3, 4, 2],
    'price': [200, 250, 300, 400, 220]
}

df = pd.DataFrame(data)

# Features and target
X = df[['size_sqft', 'bedrooms']]
y = df['price']

# Split data (use 2 samples for testing)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
model = XGBRegressor(objective='reg:squarederror', num_class=None)
model.fit(X_train, y_train)

#prediction
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

new_house = pd.DataFrame([[4900, 4]], columns=['size_sqft', 'bedrooms'])
print(f"Predicted price for new house: {model.predict(new_house)[0]:.2f} thousand")