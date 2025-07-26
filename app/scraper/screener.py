import yfinance as yf

def get_screener_data(symbol):
    stock = yf.Ticker(f"{symbol}.NS")
    info = stock.info

    return {
        "symbol": symbol.upper(),
        "current_price": info.get("currentPrice", "N/A"),
        "market_cap": info.get("marketCap", "N/A"),
        "day_high": info.get("dayHigh", "N/A"),
        "day_low": info.get("dayLow", "N/A"),
        "message": "Data from Yahoo Finance"
    }
