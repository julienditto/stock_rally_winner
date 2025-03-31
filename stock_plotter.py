import json
import matplotlib.pyplot as plt
from datetime import datetime

#loads a given file
with open("message (1).txt", "r") as f:
    data = json.load(f)

#sorts data by date, and extracts the close prices
data.sort(key=lambda x: x["date"])
dates = [datetime.fromisoformat(entry["date"]).date() for entry in data]
close_prices = [entry["close"] for entry in data]

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
plt.scatter([max_date], [max_price], color='green', label='Max Close')
plt.scatter([min_date], [min_price], color='red', label='Min Close')

plt.title("Stock closing prices over a year")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()