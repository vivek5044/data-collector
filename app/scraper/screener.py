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
