import yfinance as yf


def get_last_stock_price(stock):
    stock = yf.Ticker(stock)
    return stock.history(period="1d")["Close"][0]

def get_edo_stock_price(stock, date_start, date_end):
    stock = yf.Ticker(stock)
    return stock.history(start=date_start, end=date_end)["Close"]