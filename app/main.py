from flask import Flask, jsonify
from app.scraper.screener import get_stock_data, get_nifty50_data

def create_app():
    app = Flask(__name__)

    @app.route('/api/stock/<symbol>')
    def fetch_stock(symbol):
        return jsonify(get_stock_data(symbol))

    @app.route('/api/nifty50')
    def fetch_nifty50():
        return jsonify(get_nifty50_data())

    return app
