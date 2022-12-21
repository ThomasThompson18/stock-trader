"""Class definition for Trade model."""
from datetime import timezone
from uuid import uuid4

from sqlalchemy.ext.hybrid import hybrid_property

from project_estimator import db
from project_estimator.util.datetime_util import (
    get_local_utcoffset,
    localized_dt_string,
    make_tzaware,
    utc_now,
)

class Trade(db.Model):
    """Trade Model for Executing Trades"""

    __tablename__= "trade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String, nullable=False, default="SPY")
    buy_price = db.Column(db.Integer, nullable=False, default = 0)
    sell_price = db.Column(db.Integer, nullable=True)
    is_profit = db.column(db.Boolean, nullable=True)
    executed_buy_at = db.Column(db.DateTime, nullable=False, default=utc_now)
    executed_sell_at = db.Column(db.DateTime, nullable=True)
    profit = db.Column(db.Integer, nullable=True)