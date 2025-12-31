import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("city_day.csv")

# Select useful columns
data = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'AQI']]

# Remove rows with missing values
data = data.dropna()

# Split input and output
X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']]
y = data['AQI']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict AQI
y_pred = model.predict(X_test)

# Evaluate model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
# Show sample predictions
results = pd.DataFrame({
    "Actual AQI": y_test.values[:10],
    "Predicted AQI": y_pred[:10]
})

print("\nSample AQI Predictions:")
print(results)
