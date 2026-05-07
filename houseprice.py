import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset (simple example)
data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "price": [50, 75, 100, 125, 150]
}

df = pd.DataFrame(data)

# Input (X) and Output (Y)
X = df[["area"]]
y = df["price"]

# Model training
model = LinearRegression()
model.fit(X, y)

print("🏠 House Price Predictor Ready!")

# User input
area = float(input("Enter house area (sq ft): "))
predicted_price = model.predict([[area]])

print("💰 Predicted Price:", predicted_price[0])