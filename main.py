from data import access_web_data, data_organization, data_analysis
from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/find_trending', methods=['GET'])
def find_trending():
    #gets list of trending tickers from yahoo finance
    tickers = access_web_data()
    #uses api that provides limited free calls to get
    #historical stock prices for each tickers
    #and stores them in json files under /companies
    #due to limitation of free api, this function 
    #requires an api key.
    data_organization(tickers)
    return render_template('tickers.html', tickers=tickers)

@app.route('/submit_ticker', methods=['POST'])
def submit_ticker():
    selected_ticker = request.form['ticker']
    analysis_type = request.form['analysis_type']
    data_analysis(selected_ticker, analysis_type)
    
    # Generate the correct image filename
    if analysis_type == "SMA":
        image_filename = f"{selected_ticker.lower()}_sma.jpeg"
    elif analysis_type == "MACD":
        image_filename = f"{selected_ticker.lower()}_macd.jpeg"
    else:
        return "Invalid selection", 400  # Return error if no valid analysis type

    # Redirect to the image URL
    return redirect(url_for('static', filename=f'images/{image_filename}'))

if __name__ == '__main__':
    app.run(debug=True)


        


            



