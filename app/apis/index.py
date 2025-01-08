from flask import Blueprint, request, render_template

from app.models.statistic import ValueStatisticModel

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    # 期数
    period_count = 100

    values = ValueStatisticModel.query.limit(period_count).all()
    code_list = []
    # 和值列表
    sum_list = []
    # 平均值列表
    ave_list = []
    # 奇偶列表
    odd_list = []
    even_list = []

    for value in values:
        code_list.append(value.code)
        sum_list.append(value.sum)
        ave_list.append(value.ave)
        odd_list.append(value.odd_count)
        even_list.append(value.even_count)

    resp_data = {
        'code_list': code_list,
        'sum_list': sum_list,
        'ave_list': ave_list,
        'odd_list': odd_list,
        'even_list': even_list
    }

    return render_template("index.html", resp_data=resp_data)