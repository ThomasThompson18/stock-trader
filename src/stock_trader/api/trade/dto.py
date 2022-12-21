"""Parsers and serializers for the /trade API endpoints."""
import re

from flask_restx import Model
from flask_restx.fields import Boolean, DateTime, Integer, List, Nested, String
from flask_restx.inputs import URL, regex, boolean, positive, email
from flask_restx.reqparse import RequestParser

buy_reqparser = RequestParser(bundle_errors=True)
buy_reqparser.add_argument(
    "ticker", type=str, location="form", required=True, nullable=False
)
buy_reqparser.add_argument(
    "buy_price", type=int, location="form", required=True, nullable=False
)

sell_reqparser = RequestParser(bundle_errors=True)
sell_reqparser.add_argument(
    "ticker", type=str, location="form", required=True, nullable=False
)
sell_reqparser.add_argument(
    "sell_price", type=int, location="form", required=True, nullable=False
)

trade_model = Model(
    "Trade",
    {
        "id": Integer,
        "ticker": String,
        "buy_price": Integer,
        "sell_price": Integer,
        "is_profit": Boolean,
        "executed_buy_at": DateTime,
        "executed_sell_at": DateTime,
        "profit": Integer,
    },
)