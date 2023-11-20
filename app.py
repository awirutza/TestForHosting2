# app.py
import yfinance as yf
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    msft = yf.Ticker("MSFT")
    hist = msft.history(period="1mo")

    return render_template('index.html', name='World',data=hist)

if __name__ == '__main__':
    app.run(debug=True)
