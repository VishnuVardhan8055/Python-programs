import MetaTrader5 as mt5
import pandas as pd
import time


# Function to calculate RSI
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gains = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    losses = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gains / losses
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]


# Initialize MetaTrader5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    mt5.shutdown()
    exit()
print("MT5 initialized successfully")

# Parameters
account_number = 115732981
password = 'Test12345@'
server = 'Exness-MT5Trial6'
symbol = "XAUUSDm"
lot_size = 0.01
rsi_period = 4
overbought_threshold = 70
oversold_threshold = 30
sl_points = 300
tp_points = 600
deviation = 20

# Attempt to login to MT5
if not mt5.login(account_number, password=password, server=server):
    print("Login failed, error code =", mt5.last_error())
    mt5.shutdown()
    exit()
print(f"Logged in to account #{account_number}")

# Ensure the symbol is available
if not mt5.symbol_select(symbol, True):
    print(f"Failed to select {symbol}, error code =", mt5.last_error())
    mt5.shutdown()
    exit()

try:
    while True:
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, rsi_period + 1)
        if rates is None or len(rates) < rsi_period + 1:
            print(f"Unable to get rates for {symbol}")
            continue

        df = pd.DataFrame(rates)
        rsi_value = calculate_rsi(df['close'], rsi_period)
        print(f"Current RSI({rsi_period}) value: {rsi_value}")

        trade_action = None
        if rsi_value > overbought_threshold:
            print(f"{symbol} is overbought. Considering a SELL.")
            trade_action = mt5.ORDER_TYPE_SELL
        elif rsi_value < oversold_threshold:
            print(f"{symbol} is oversold. Considering a BUY.")
            trade_action = mt5.ORDER_TYPE_BUY

        if trade_action is not None:
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                print(f"{symbol} not found")
                continue

            point = symbol_info.point
            price = mt5.symbol_info_tick(symbol).ask if trade_action == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(
                symbol).bid
            sl = price - sl_points * point if trade_action == mt5.ORDER_TYPE_BUY else price + sl_points * point
            tp = price + tp_points * point if trade_action == mt5.ORDER_TYPE_BUY else price - tp_points * point

            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": lot_size,
                "type": trade_action,
                "price": price,
                "sl": sl,
                "tp": tp,
                "deviation": deviation,
                "magic": 234000,
                "comment": "ai&ml",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }

            # Send the trade request
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print(f"Trade failed: {result}")
            else:
                print(f"Trade successful: {result}")

        time.sleep(60)  # Sleep for 1 minute before the next check

except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    mt5.shutdown()
    print("MT5 connection shut down.")
import pandas as pd
import pandas_ta as ta
import mt5

# Assuming 'data' is a Pandas DataFrame with columns: 'open', 'high', 'low', 'close', 'volume'
# Make sure your datetime data is set as the DataFrame index if it's not already

# Calculate RSI
data.ta.rsi(close='close', length=14, append=True)

# Calculate SMA
data.ta.sma(close='close', length=30, append=True)

# Calculate MACD
data.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)

# You can add as many indicators as needed for your strategy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Example: Assuming `features` are your input features and `target` is what you're predicting
X = data[features]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train your model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
score = model.score(X_test, y_test)
print(f"Model accuracy: {score}")