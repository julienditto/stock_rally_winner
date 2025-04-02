#calculates simple moving average
def simple_moving_average(prices, window):
    TRADING_DAYS_YEAR = 251
    count = TRADING_DAYS_YEAR
    averages = []
    while count > 1:
        window_slice = prices[-(count + (window - 1)) : -(count-1)]
        window_avg = sum(window_slice) / window
        averages.append(window_avg)
        count -= 1
    #final average count = 1
    window_slice = prices[-(count + (window - 1)) :]
    window_avg = sum(window_slice) / window
    averages.append(window_avg)
    return averages

#calculates Moving average convergence/divergence using EMA
def exponential_moving_average(prices, window):
    averages = []
    TRADING_DAYS_YEAR = 251
    count = TRADING_DAYS_YEAR
    multiplier = 2 / (window + 1)
    window_slice = prices[-(count + (window - 1)) : -(count-1)]
    #first EMA value (oldest) is the SMA of the widow at that date
    sma = sum(window_slice) / window
    averages.append(sma)
    count -= 1
    while count > 0:
        print(count)
        curr_day_value = prices[-count]
        ema_prev_day = averages[-1]
        ema_value = (curr_day_value * multiplier) + ema_prev_day * (1 - multiplier)
        averages.append(ema_value)
        count -= 1
    return averages

def macd(prices):
    ema_12 = exponential_moving_average(prices, 12)
    ema_26 = exponential_moving_average(prices, 26)
    signal_line = exponential_moving_average(prices, 9)
    macd_line = [a - b for a, b in zip(ema_12, ema_26)]
    return (macd_line, signal_line)

