import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(f"{symbol}.NS")
        info = stock.info

        return {
            "symbol": symbol.upper(),
            "current_price": info.get("currentPrice", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "day_high": info.get("dayHigh", "N/A"),
            "day_low": info.get("dayLow", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "roe": info.get("returnOnEquity", "N/A"),
            "debt_to_equity": info.get("debtToEquity", "N/A"),
            "fifty_dma": info.get("fiftyDayAverage", "N/A"),
            "two_hundred_dma": info.get("twoHundredDayAverage", "N/A"),
            "promoter_holding": info.get("heldPercentInsiders", "N/A"),
            "fii_holding": info.get("heldPercentInstitutions", "N/A"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow", "N/A"),
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
