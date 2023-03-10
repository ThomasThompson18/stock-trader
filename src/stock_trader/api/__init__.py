"""API blueprint configuration."""
import flask.scaffold
from flask import Blueprint

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restx import Api  # noqa: E402

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_bp,
    version="1.0",
    title="Stock Trader Appication",
    description="Automated Trading of da Stonks",
    doc="/ui",
    authorizations=authorizations,
)