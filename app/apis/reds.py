from flask import Blueprint, request

from app.data import HistoryData
from app.extensions import db
from app.utils.response import make_response


reds_bp = Blueprint('reds', __name__)


@reds_bp.route('/update', methods=['post'])
def update():
    """
        更新数据：
            1. 如果请求体body没有任何参数，表示全部更新
            2. 如果body中出现了reds，表示需要更新开奖号码
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