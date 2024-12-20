from flask import Blueprint, request

from app.data import HistoryData
from app.extensions import db
from app.utils.response import make_response
from app.utils.transfer import wrap_to_model
from app.models.reds import RedsModel
from app.models.prize import PrizeX10Model
from app.utils.log import logger


prize_bp = Blueprint('prize', __name__, url_prefix='/prize')


@prize_bp.route('/update', methods=['post'])
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

    for period in his_data.get("result"):
        item_code = period["code"]
        reds_obj = RedsModel.query.filter_by(code=item_code).first()
        if not reds_obj:
            logger.warning(f"reds缺少第{item_code}期，跳过更新")
            continue

        reds_id = reds_obj.id
        model_objs = wrap_to_model(reds_id, period)
        db.session.add_all(model_objs)
        logger.info(f"第{item_code}期奖金更新，成功")

    db.session.commit()

    logger.info(f"全部更新完成，共{update_count}期")

    return make_response(200, 'ok'), 200