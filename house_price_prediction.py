import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("house_data.csv")

# Features and Target
X = df[["Rooms", "Size"]]
y = df["Price"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", mae)

# User Prediction
rooms = int(input("Enter number of rooms: "))
size = int(input("Enter house size (sq ft): "))

predicted_price = model.predict([[rooms, size]])

print(f"Predicted House Price: ₹{predicted_price[0]:,.0f}")

# Visualization
plt.scatter(df["Size"], df["Price"])
plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("House Size vs Price")
plt.show()
