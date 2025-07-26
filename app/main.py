from flask import Flask, jsonify
from app.scraper.screener import get_screener_data

def create_app():
    app = Flask(__name__)

    @app.route("/ping")
    def ping():
        return "pong", 200

    @app.route("/screener/<symbol>")
    def screener_by_symbol(symbol):
        data = get_screener_data(symbol)
        return jsonify(data)

    return app
