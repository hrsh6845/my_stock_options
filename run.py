from stock_options import create_app

stock_options = create_app()

if __name__ == '__main__':
    stock_options.run(debug=True)