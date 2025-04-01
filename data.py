from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import shutil
import requests
import json
import os
from datetime import date, datetime, timedelta

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
    print(f"Now fetching stock data for the tickers:")
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    two_years_ago = (datetime.today() - timedelta(days=2 * 365)).strftime("%Y-%m-%d")
    directory_name = "companies"
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
    os.mkdir(directory_name)
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
            filename = f"./companies/{tickers[i]}.json"
            with open(filename, 'w') as file:
                json.dump(response_json['data'], file, indent=4)
        elif response.status_code == 422:
            print(f"api call for ticker {tickers[i]} returned with status code {response.status_code}")
        else:
            print(f"api call for ticker {tickers[i]} returned with status code {response.status_code}")
            break

def data_analysis():
    directory = './companies'  # '.' refers to the current working directory

    # List all files that end with '.json' in the specified directory
    companies_json_files = [f for f in os.listdir(directory) if f.endswith('.json') and os.path.isfile(os.path.join(directory, f))]
    for i in range(len(companies_json_files)):
        filename = "./companies/"
        filename += companies_json_files[i]
        with open(filename, 'r') as file:
            company_stock_days = json.load(file)
        simple_moving_average(company_stock_days)
    
def simple_moving_average(company_stock_days):
    pass
