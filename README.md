# stock_rally_winner
### by Julien Ditto and Jake Johnson

The program will scrape Yahoo Finance [Top Trending Stocks](https://finance.yahoo.com/markets/stocks/trending/) page for the day’s trending stock tickers. There will be API calls to Alpha Vantage Stock Market Data API to get stock data for each ticker and the data will be saved in JSON format to JSON files. Basic technical analysis will be performed on each company's stock data. The technical analysis results will help the user understand when the stock started trending and the momentum of the trend. The stock price data and technical analysis results will be saved in a visual format to be downloaded by the user. 

# Project Outline/Plan
## Interface Plan: 
Widgets/buttons will be made using HTML, CSS, and rendered with Flask. Ideally users should be able to select whether they are an investor or trader which will signify to the system to do either long term or short term technical analysis. Next, the user should be able to select to analyze the day's trending stocks. Finally, they should have the option to download the results.
## Data Collection and Storage Plan (written by Julien Ditto): 
We will use Selenium and Beautifulsoup to scrape the webpage Yahoo Finance Top Trending Stocks for the day's trending tickers. The stock data will be stored in JSON format in a directory of JSON files (eg. AAPL.json for Apple Inc.’s stock data).
## Data Analysis and Visualization Plan (written by Jake Johnson): 
The technical analysis indicators we will using are Simple Moving Average (SMA) and Moving Average Convergence Divergence. For SMA we will be looking out for the death cross and golden cross crossovers using long 200-day SMA and 50-day SMA. We will use the MACD  indicator to analyze short term trading trends. Matplotlib would be used to visualize the SMAs and the MACDs.

