"""API endpoint definitions for /trade namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource

from stock_trader.models.trade import Trade

from stock_trader.api.trade.dto import (
    trade_model,
    buy_reqparser,
)

from stock_trader.api.trade.business import (
    buy
)

trade_ns = Namespace(name="trade", validate=True)
trade_ns.models[trade_model.name] = trade_model

@trade_ns.route("/buy", endpoint="trade_buy")
@trade_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@trade_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@trade_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class CreateAccount(Resource):
    """Handles HTTP requests to URL: /accounts."""

    @trade_ns.doc(security="Bearer")
    @trade_ns.response(int(HTTPStatus.CREATED), "Trade Executed.")
    @trade_ns.expect(buy_reqparser)
    def post(self):
        """Create a trade."""
        trade_dict = buy_reqparser.parse_args()
        return buy(trade_dict)

@trade_ns.route("/sell", endpoint="trade_sell")
@trade_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@trade_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@trade_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class CreateAccount(Resource):
    """Handles HTTP requests to URL: /accounts."""

    @trade_ns.doc(security="Bearer")
    @trade_ns.response(int(HTTPStatus.OK), "Trade Executed.")
    @trade_ns.expect(sell_reqparser)
    def post(self):
        """Sell a trade."""
        sell_dict = sell_reqparser.parse_args()
        return sell(sell_dict)