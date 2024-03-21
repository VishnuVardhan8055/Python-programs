import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Assuming you have a CSV file with historical stock data
# Replace 'your_stock_data.csv' with the actual file path or URL
data = pd.read_csv('GOOGL.csv')

# Assuming the CSV file has columns like 'Date', 'Open', 'High', 'Low', 'Close', etc.
# Adjust the column names based on your data

# Feature selection
features = data[['Open', 'Close', 'Volume']]

# Target variables
high_prices = data['High']
low_prices = data['Low']

# Split the data into training and testing sets
X_train, X_test, y_high_train, y_high_test, y_low_train, y_low_test = train_test_split(
    features, high_prices, low_prices, test_size=0.2, random_state=42
)

# Linear Regression model for predicting high prices
model_high = LinearRegression()
model_high.fit(X_train, y_high_train)

# Linear Regression model for predicting low prices
model_low = LinearRegression()
model_low.fit(X_train, y_low_train)

# Predictions on the test set
high_predictions = model_high.predict(X_test)
low_predictions = model_low.predict(X_test)

# Evaluation metrics (optional)
mse_high = mean_squared_error(y_high_test, high_predictions)
mse_low = mean_squared_error(y_low_test, low_predictions)

print(f'Mean Squared Error (High): {mse_high}')
print(f'Mean Squared Error (Low): {mse_low}')

# Visualize predictions
plt.scatter(y_high_test, high_predictions, label='High Price Predictions')
plt.scatter(y_low_test, low_predictions, label='Low Price Predictions')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.legend()
plt.show()
