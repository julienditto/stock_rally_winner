from data import access_web_data, data_organization, data_analysis, data_visualization
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/find_trending', methods=['GET'])
def find_trending():
    #gets list of trending tickers from yahoo finance
    yahoo_tickers = access_web_data()
    #uses api that provides limited free calls to get
    #historical stock prices for each tickers
    #and stores them in json files under /companies
    #due to limitation of free api, this function 
    #requires an api key.
    proccesable_tickers = data_organization(yahoo_tickers)
    return render_template('tickers.html', tickers=proccesable_tickers)

@app.route('/submit_ticker', methods=['POST'])
def submit_ticker():
    selected_ticker = request.form['ticker']
    analysis_type = request.form['analysis_type']
    analyzed_data = data_analysis(selected_ticker, analysis_type)
    dates = analyzed_data[0]
    close_prices = analyzed_data[1]
    # Generate the correct image filename
    if analysis_type == "SMA":
        sma_50 = analyzed_data[2]
        sma_200 = analyzed_data[3]
        data_visualization(selected_ticker, analysis_type, dates,
                           close_prices, sma_50=sma_50, sma_200=sma_200)
        image_filename = f"{selected_ticker.lower()}_sma.png"
    elif analysis_type == "MACD":
        macd_line = analyzed_data[2]
        signal_line = analyzed_data[3]
        data_visualization(selected_ticker, analysis_type, dates, 
                           close_prices, macd_line=macd_line, signal_line=signal_line)
        image_filename = f"{selected_ticker.lower()}_macd.png"
    else:
        return "Invalid selection", 400  # Return error if no valid analysis type

    # Redirect to the image URL
    return redirect(url_for('static', filename=f'images/{image_filename}'))

if __name__ == '__main__':
    app.run(debug=True)


        


            



