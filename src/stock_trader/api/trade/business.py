 """Business logic for /accounts API endpoints."""
from http import HTTPStatus

from flask import jsonify, url_for
from flask_restx import abort, marshal

from datetime import timezone

from stock_trader.util import utc_now

from stock_trader.models.trade import Trade

def buy(trade_dict):
    trade = Trade(**trade_dict)
    trade.executed_buy_at = utc_now()
    db.session.add(trade)
    db.session.commit()
    response = jsonify(
        status="success", message=f"New trade executed: {trade.id}"
    )
    response.status_code = HTTPStatus.CREATED

def sell(sell_dict):
    ticker = sell_dict["ticker"]
    trade = Trade.query.filter_by(id=id).first()
    if trade:
        trade.sell_price = sell_dict["sell_price"]
        trade.executed_sell_at = utc_now()
        trade.profit = trade.sell_price - trade.buy_price
        if trade.profit > 0:
            trade.is_profit = True
        else:
            trade.is_profit = False
    db.session.commit()
    response = jsonify(
        status="success", message=f"Trade executed: {trade.id}"
    )
    response.status_code = HTTPStatus.OK
