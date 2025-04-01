import json
import matplotlib.pyplot as plt
from datetime import datetime
import os

#loads a given file
with open("companies/BIAF.json", "r") as f:
    data = json.load(f)

#sorts data by date, and extracts the close prices
data.sort(key=lambda x: x["date"])
dates = [datetime.fromisoformat(entry["date"]).date() for entry in data]
close_prices = [entry["close"] for entry in data]

#calculates simple moving average
def simple_moving_average(prices, window):
    averages = []
    for i in range(len(prices)):
        if i >= window - 1:
            window_slice = prices[i - window + 1:i + 1]
            window_avg = sum(window_slice) / window
            averages.append(window_avg)
        else:
            averages.append(None) #not enough data yet
    return averages

#calculates Moving average convergence/divergence using EMA
def exponential_moving_average(prices, window):
    averages = []
    multiplier = 2 / (window + 1)
    for i, price in enumerate(prices):
        if i == 0:
            averages.append(price)  #start EMA with first price
        else:
            ema_value = (price - averages[-1]) * multiplier + averages[-1]
            averages.append(ema_value)
    return averages

def macd(prices):
    ema_12 = exponential_moving_average(prices, 12)
    ema_26 = exponential_moving_average(prices, 26)
    macd_line = [a - b for a, b in zip(ema_12, ema_26)]
    return macd_line

#sma_50 = simple_moving_average(close_prices, 50)
#sma_200 = simple_moving_average(close_prices, 200)
macd_line = macd(close_prices)

#analysis of stock prices through console output
max_price = max(close_prices)
min_price = min(close_prices)
avg_price = sum(close_prices) / len(close_prices)

max_date = dates[close_prices.index(max_price)]
min_date = dates[close_prices.index(min_price)]

print("Stock Price Analysis:")
print(f"- Highest Close: ${max_price:.2f} on {max_date}")
print(f"- Lowest Close: ${min_price:.2f} on {min_date}")
print(f"- Average Close: ${avg_price:.2f}")
print(f"- Date Range: {dates[0]} to {dates[-1]}")

#plotting the prices
plt.figure(figsize=(12, 6))
plt.plot(dates, close_prices, label="Close Price", linewidth=1)
#plt.plot(dates, sma_50, label="50-Day SMA", linewidth=1.2)
#plt.plot(dates, sma_200, label="200-Day SMA", linewidth=1.2)
plt.plot(dates, macd_line, label="MACD", linewidth=1.2)

plt.scatter([max_date], [max_price], color='green', label='Max Close', zorder=5)
plt.scatter([min_date], [min_price], color='red', label='Min Close', zorder=5)

#details about the graph including legend
plt.title("Stock closing prices over a year")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)

#code to save the plot to a directory
output_dir = "./static/images"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "plot.png"))

plt.show()