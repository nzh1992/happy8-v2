from flask import Blueprint, request

from app.data import HistoryData
from app.extensions import db
from app.utils.response import make_response
from app.utils.transfer import prizegrades_to_model
from app.models.reds import RedsModel
from app.models.prize import PrizeX10Model


reds_bp = Blueprint('reds', __name__)


@reds_bp.route('/update/reds', methods=['post'])
def update_reds():
    """
    更新开奖号码

    :return:
    """
    data = request.get_json(force=True)

    from app.models.reds import RedsModel

    # 数据库中的期数
    current_count = RedsModel.query.count()

    hd = HistoryData()
    # 总共的期数
    total_count = hd.get_history_count()

    update_count = total_count - current_count
    if update_count <= 0:
        return make_response(200, '已是最新，无需更新'), 200

    his_df = hd.get_reds_df(update_count)

    reds_model_list = []

    # 写入数据库
    for row in his_df.iterrows():
        code = row[0]
        red_numbers = [item for item in row[1]]
        red_model = RedsModel(code, red_numbers)
        reds_model_list.append(red_model)

    db.session.add_all(reds_model_list)
    db.session.commit()
    return make_response(200, 'ok'), 200


@reds_bp.route('/update/prize', methods=['post'])
def update_prize():
    """
    更新奖池、中奖等信息

    :return:
    """
    data = request.get_json(force=True)

    # 数据库中的期数
    current_count = PrizeX10Model.query.count()

    hd = HistoryData()
    # 总共的期数
    total_count = hd.get_history_count()

    update_count = total_count - current_count
    if update_count <= 0:
        return make_response(200, '已是最新，无需更新'), 200

    his_data = hd.get_data(update_count)

    prize_model_list = []
    for item in his_data.get("result"):
        item_code = item["code"]
        reds_id = RedsModel.query.filter_by(code=item_code).first().id
        prizegrades = item.get('prizegrades')

        result = prizegrades_to_model(prizegrades)


    return make_response(200, 'ok'), 200