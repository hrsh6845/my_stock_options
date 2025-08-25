from flask import Blueprint, request, jsonify
from .services.monday_options import MondayCalculator

bp = Blueprint("main", __name__)

def register_routes(app):
    app.register_blueprint(bp)

@bp.route('/get-monday-options', methods=['GET'])
def get_monday_options():
    symbol = request.args.get('symbol', 'AAPL')
    calculator = MondayCalculator(symbol)
    return jsonify(calculator.get_monday_options())

#@bp.route('/my-test-history', methods=['GET'])
#def get_my_test_history():
