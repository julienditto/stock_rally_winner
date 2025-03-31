from data import access_web_data, data_organization, data_analysis

#gets list of trending tickers from yahoo finance
tickers = access_web_data()
#uses api that provides limited free calls to get
#historical stock prices for each tickers
#and stores them in json files under /companies
#due to limitation of free api, this function 
#requires an api key.
data_organization(tickers)
#data_analysis()


        


            



