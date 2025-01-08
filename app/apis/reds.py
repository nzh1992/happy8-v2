from flask import Blueprint, request

from app.data import HistoryData
from app.extensions import db
from app.utils.response import make_response
from app.utils.log import logger
from app.models.reds import RedsModel
from app.utils.transfer.red import RedsTransfer


reds_bp = Blueprint('reds', __name__, url_prefix='/reds')


@reds_bp.route('/update', methods=['post'])
def update_reds():
    """
    更新开奖号码

    :return:
    """
    # 数据库中的期数
    current_count = RedsModel.query.count()

    # 官网期数
    hd = HistoryData()
    total_count = hd.get_history_count()

    if current_count == 0:
        # 初次更新，拉取全部数据

        his_df = hd.get_reds_df(total_count, True)
        reds_model_list = RedsTransfer(his_df).to_reds_model_list()

    else:
        # 追加更新，拉取后续数据
        pass

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
        logger.info(f"第{code}期更新，成功")

    db.session.add_all(reds_model_list)
    db.session.commit()
    logger.info(f"全部更新完成，共{update_count}期")
    return make_response(200, 'ok'), 200


@reds_bp.route('/list', methods=['post'])
def list_reds():
    df = RedsModel.get_df('2024100', '2024110')
    print(df)

    return make_response(200, 'ok', df), 200