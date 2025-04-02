# stock_rally_winner
### by Julien Ditto and Jake Johnson

The program scrapes Yahoo Finance [Top Trending Stocks](https://finance.yahoo.com/markets/stocks/trending/) page for the day’s trending stock tickers. We use a third party API Market Stack Stock API to get stock data for each ticker. Basic technical analysis is performed on each company's stock data. The technical analysis results help the user understand when the stock started trending and the momentum of the trend. The stock price data and technical analysis results get plotted to images which are accessbile to the user by a drop down list. 

# Project Outline
## Interface (written by Julien Ditto): 
Widgets/buttons are made using HTML, CSS, and rendered with Flask. The user needs to select to fetch trending stock. The GUI displays a message to the user to wait while program fetches the trending tickers. The waiting process can take up to a minute because the program needs to scrape the yahoo webpage and make api calls for stock data. Onces all the data is ready, the user is forwarded to a page where they can select from a dropdown menu of the trending tickers, which one they want to analyze and the type of analysis they want done (MACD or SMA). Once the selection is complete they are forwarded to a page for the plotted image of the analysis.
## Data Collection and Storage (written by Julien Ditto): 
We use Selenium and Beautifulsoup to scrape the yahoo webpage for the trending tickers. For each ticker a call to the Market Stack API is made for 2 years of historical daily data. For each ticker the stock data is stored in JSON format in a JSON file (eg. AAPL.json would be for Apple Inc.’s stock data). All JSON files get saved under directory the program makes called companies.
## Data Analysis and Visualization (written by Jake Johnson): 
The technical analysis indicators we will using are Simple Moving Average (SMA) and Moving Average Convergence Divergence (MACD). For the SMA option, we plot the relationship between the 200-day and 50-day looking for crossovers which are called death cross and golden cross that indicate buy and sell signals. We use the MACD indicator to analyze short term trading trends looking out for crossovers between the signal line and the MACD line indicating buy and sell signals. Matplotlib are used to plot the price action, SMAs, and MACDs and the plotted images get stored under static/images.
## More Information
For detailed infomration about the technical analysis indicators we use check out our google doc [moving averages](https://docs.google.com/document/d/1Zqj9vs-x7bcIaqzzTuPL9yHF1vUcGfuj/edit?usp=sharing&ouid=112221543553095764423&rtpof=true&sd=true).
## Installation Instructions:
pip install Flask
pip install selenium
pip install beautifulsoup4
pip install matplotlib
pip install python-dateutil
pip install requests
You need to download a Google Chrome web driver and supply the path for selenium in the program. The driver should match the version of your Google Chrome installed on your device.
Check your version on Google Chome About. Download chrome driver [here](https://developer.chrome.com/docs/chromedriver/downloads). Copy the link for the correct web driver download and paste it into your url to download.
## Future Project Updates
If we were to continue working on the project, we would provide analysis and visualization options for more technical analysis indicators such as the Releative Strength Index (RSI), Bollinger Bands, Stochastic Osillators, and Average Directional Index (ADX).


