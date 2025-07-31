from flask import Flask

def create_app():
    stock_options = Flask(__name__)

    from .routes import register_routes
    register_routes(stock_options)

    return stock_options