import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(f"{symbol}.NS")
        info = stock.info

        return {
            "symbol": symbol.upper(),
            "current_price": info.get("currentPrice", None),
            "market_cap": info.get("marketCap", None),
            "day_high": info.get("dayHigh", None),
            "day_low": info.get("dayLow", None),
            "pe_ratio": info.get("trailingPE", None),
            "dividend_yield": info.get("dividendYield", None),
            "roe": info.get("returNonequity", None),
            "debt_to_equity": info.get("debtToEquity", None),
            "fifty_dma": info.get("fiftyDayAverage", None),
            "two_hundred_dma": info.get("twoHundredDayAverage", None),
            "promoter_holding": info.get("heldPercentInsiders", None),
            "fii_holding": info.get("heldPercentInstitutions", None),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh", None),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow", None),
            "message": "Data from Yahoo Finance"
        }
    except Exception as e:
        return {"symbol": symbol, "error": str(e)}

def get_nifty50_data():
    nifty_50_symbols = [
        "RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "HINDUNILVR", "SBIN",
        "KOTAKBANK", "ITC", "LT", "BHARTIARTL", "ASIANPAINT", "HCLTECH", "MARUTI",
        "AXISBANK", "SUNPHARMA", "BAJFINANCE", "WIPRO", "ULTRACEMCO", "NTPC",
        "TITAN", "TATAMOTORS", "POWERGRID", "NESTLEIND", "GRASIM", "HINDALCO",
        "ONGC", "ADANIPORTS", "JSWSTEEL", "TATASTEEL", "TECHM", "CIPLA", "DIVISLAB",
        "SBILIFE", "BAJAJ-AUTO", "EICHERMOT", "BAJAJFINSV", "HEROMOTOCO", "BPCL",
        "COALINDIA", "UPL", "BRITANNIA", "DRREDDY", "APOLLOHOSP", "INDUSINDBK",
        "HDFCLIFE", "ICICIPRULI", "SHREECEM", "M&M", "ADANIENT"
    ]

    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_symbol = {executor.submit(get_stock_data, symbol): symbol for symbol in nifty_50_symbols}

        for future in as_completed(future_to_symbol):
            data = future.result()
            results.append(data)

    return results
