from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import shutil
import requests
import json
import os
from datetime import datetime, timedelta
from moving_averages import simple_moving_average, macd
import matplotlib.pyplot as plt
import matplotlib
from dateutil import parser

yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
two_years_ago = (datetime.today() - timedelta(days=2 * 365)).strftime("%Y-%m-%d")

def access_web_data():
    # Path to the manually downloaded ChromeDriver
    # chrome driver version needs to match the version of google chrome installed on device
    chrome_driver_path = '/Users/julienditto/Downloads/chromedriver-mac-x64/chromedriver'
    # Set up the WebDriver with your manually downloaded chromedriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    # Initialize the driver with the specified ChromeDriver path
    driver_service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    # URL of the Yahoo Finance page for stock gainers
    url = "https://finance.yahoo.com/markets/stocks/trending/"
    # Open the page using Selenium
    driver.get(url)
    # Get the page source and pass it to BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tickers = list()
    # Find the table (You can adjust this selector if you need to target a specific table)
    table = soup.find('table')
    # Find the table body (tbody)
    tbody = table.find('tbody')
    # Loop through each row in the table body
    for row in tbody.find_all('tr'):
        # Get all columns (td) in the current row
        columns = row.find_all('td')
        # Check if there are any columns in this row
        if columns:
            # col 0 in table is ticker
            tickers.append(columns[0].text.strip())

    print("""TEST CONSOLE OUTPUT""")
    print(f"Top {len(tickers)} trending stock tickers for today!")
    print(tickers)

    return tickers

#for each trending ticker write their stock data to a json file
#api key has already used max amount of free calls. needs a new key or new api
def data_organization(tickers):
    #need at least 450 trading days of stock data
    # to plot one year of SMA
    REQUIRED_NUMBER_DAYS = 450
    print(f"Now fetching stock data for the tickers:")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    two_years_ago = (datetime.today() - timedelta(days=2 * 365)).strftime("%Y-%m-%d")
    directory_name = "companies"
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
    os.mkdir(directory_name)
    processable_tickers = []
    for i in range(len(tickers)):
        #api call for each ticker requires access key
        base_url = "https://api.marketstack.com/v2/eod"
        params = {
            "access_key": "224568fb4db9c4a463cfb067117e088a",
            "symbols": tickers[i],
            "date_from": two_years_ago,
            "date_to": yesterday,
            "limit": "1000"
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            response_json = response.json()
            number_days_hist_data = len(response_json['data'])
            if  number_days_hist_data < REQUIRED_NUMBER_DAYS:
                #not enough days of historical data for ticker
                continue
            processable_tickers.append(tickers[i])
            filename = f"./companies/{tickers[i]}.json"
            with open(filename, 'w') as file:
                json.dump(response_json['data'], file, indent=4)
        elif response.status_code == 422:
            print(f"api call for ticker {tickers[i]} returned with status code {response.status_code}")
        else:
            print(f"api call for ticker {tickers[i]} returned with status code {response.status_code}")
            break
    return processable_tickers

def data_analysis(selected_ticker, analysis_type):
    TRADING_DAYS_YEAR = 251
    filename = f"./companies/{selected_ticker}.json"
    with open(filename, 'r') as file:
        company_stock_days = json.load(file)
    #sorts data by date, and extracts the close prices
    company_stock_days.sort(key=lambda x: x["date"])
    all_dates = [parser.parse(entry["date"]).date() for entry in company_stock_days]
    dates_one_year = all_dates[-TRADING_DAYS_YEAR:]
    all_close_prices = [entry["close"] for entry in company_stock_days]
    close_prices_one_year = all_close_prices[-TRADING_DAYS_YEAR:]
    if analysis_type == "SMA":
        #sma needs more that a year of stock data to make averages
        sma_50 = simple_moving_average(all_close_prices, 50)
        sma_200 = simple_moving_average(all_close_prices, 200)
        return (dates_one_year, close_prices_one_year, sma_50, sma_200)
    elif analysis_type == "MACD":
        #macd needs more than a year of stock data to make averages
        macd_line, signal_line = macd(all_close_prices)
        return (dates_one_year, close_prices_one_year, macd_line, signal_line)
    
def data_visualization(ticker, analysis_type, dates, close_prices, **kwargs):
    matplotlib.use('Agg')
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

    if analysis_type == "SMA":
        sma_50 = kwargs.get("sma_50")
        sma_200 = kwargs.get("sma_200") 
        plt.plot(dates, sma_50, label="50-Day SMA", linewidth=1.2)
        plt.plot(dates, sma_200, label="200-Day SMA", linewidth=1.2)
    elif analysis_type == "MACD":
        macd_line = kwargs.get("macd_line")
        signal_line = kwargs.get("signal_line")
        offset = signal_line[0] - macd_line[0]
        macd_line_offset = [value + offset for value in macd_line]
        plt.plot(dates, macd_line_offset, label="MACD", linewidth=1.2)
        plt.plot(dates, signal_line, label="Signal Line", linewidth=1.2)
    else:
        raise ValueError("imporoper analysis type")

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
    lower_case_analysis_type = analysis_type.lower()
    plt.savefig(os.path.join(output_dir, f"{ticker}_{lower_case_analysis_type}.png"))
