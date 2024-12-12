from flask import Blueprint, request


index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return "首页"