# stock_rally_winner

Julien Ditto and Jake Johnson
The program will scrape Yahoo Finance Top trending stocks page for the day’s trending stock tickers. There will be API calls to Alpha Vantage Stock Market Data API to get stock data for each ticker and the data will be saved in JSON format to JSON files eg. AAPL.json for Apple Inc.’s stock data. Basic technical analysis will be performed on each company's stock data. The technical analysis results will help the user understand when the stock started trending and the momentum of the trend. The stock price data and technical analysis results will be saved in a visual format to be downloaded by the user. 

# Project Outline/Plan
Interface Plan: widgets/buttons will be made using HTML CSS, rendered with Flask. Ideally users should be able to select whether they are an investor or trader which will signify to the system to do either long term or short term technical analysis. Next they should be able to select to analyze the day's trending stocks. Finally they should have the option to download the results.
Data Collection and Storage Plan (written by Julien Ditto): For Data collection we will use Selenium and Beautifulsoup. The data will simply be stored in JSON format in JSON files.
