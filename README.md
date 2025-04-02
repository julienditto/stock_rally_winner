# stock_rally_winner
### by Julien Ditto and Jake Johnson

The program scrapes Yahoo Finance [Top Trending Stocks](https://finance.yahoo.com/markets/stocks/trending/) page for the day’s trending stock tickers. There will be API calls to Market Stack Stock API to get stock data for each ticker and the data is saved in JSON format to JSON files. Basic technical analysis is performed on each company's stock data. The technical analysis results help the user understand when the stock started trending and the momentum of the trend. The stock price data and technical analysis results get plotted to images which are accessbile to the user by a drop down list. 

# Project Outline/Plan
## Interface (written by Julien Ditto): 
Widgets/buttons will be made using HTML, CSS, and rendered with Flask. The user needs to select to fetch trending stock. The GUI displays a message to the user to wait while program fetches the trending tickers. The waiting process can take up to a minute because the program needs to scrape the yahoo page and make api calls for stock data. Onces all the data is ready, the user is forwarded to a page where they can select within a dropdown menu which ticker to analyze and the type of analysis they want done (MACD or SMA).
## Data Collection and Storage (written by Julien Ditto): 
We use Selenium and Beautifulsoup to scrape the webpage Yahoo Finance Top Trending Stocks for the day's trending tickers. The stock data gets stored in JSON format in a directory of JSON files (eg. AAPL.json for Apple Inc.’s stock data) called companies.
## Data Analysis and Visualization (written by Jake Johnson): 
The technical analysis indicators we will using are Simple Moving Average (SMA) and Moving Average Convergence Divergence. For the SMA option, we plot the relationship between the 200-day and 50-day looking for crossovers (which are called death cross and golden cross) indicating buy and sell signals. We use the MACD indicator to analyze short term trading trends looking out for crossovers between the signal line and the MACD line indicating buy and sell signals. Matplotlib are used to plot the price action, SMAs, and MACDs.

