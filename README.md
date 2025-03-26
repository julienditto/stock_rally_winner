# stock_rally_winner
### by Julien Ditto and Jake Johnson

The program will scrape Yahoo Finance Top trending stocks page for the day’s trending stock tickers. There will be API calls to Alpha Vantage Stock Market Data API to get stock data for each ticker and the data will be saved in JSON format to JSON files. Basic technical analysis will be performed on each company's stock data. The technical analysis results will help the user understand when the stock started trending and the momentum of the trend. The stock price data and technical analysis results will be saved in a visual format to be downloaded by the user. 

# Project Outline/Plan
## Interface Plan: 
Widgets/buttons will be made using HTML CSS, rendered with Flask. Ideally users should be able to select whether they are an investor or trader which will signify to the system to do either long term or short term technical analysis. Next they should be able to select to analyze the day's trending stocks. Finally they should have the option to download the results.
## Data Collection and Storage Plan (written by Julien Ditto): 
Data Collection and Storage Plan (written by Julien Ditto): For Data collection we will use Selenium and Beautifulsoup to scrape the webpage [Yahoo Finance Top Trending Stocks](https://finance.yahoo.com/markets/stocks/trending/) for the trending tickers. The stock data will simply be stored in JSON format in a directory of JSON files (eg. AAPL.json for Apple Inc.’s stock data).
## Data Analysis and Visualization Plan (written by Jake Johnson): 
Technical analysis will be done using the Pandas package. The technical analysis indicators we will be looking for are the death cross and golden cross crossovers using long term Simple Moving Averages (SMA). If time permits, we will use the Moving Average Convergence Divergence (MACD) indicator to analyze short term trading trends. Matplotlib would be used to visualize the SMAs and potentially the MACDs.

