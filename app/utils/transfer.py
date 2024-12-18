from datetime import datetime

from app.models.prize import (PrizeX1Model, PrizeX2Model, PrizeX3Model, PrizeX4Model, PrizeX5Model, PrizeX6Model,
                              PrizeX7Model, PrizeX8Model, PrizeX9Model, PrizeX10Model)


def get_model(type_name):
    model_mapping = {
        'x10': PrizeX10Model,
        'x9': PrizeX9Model,
        'x8': PrizeX8Model,
        'x7': PrizeX7Model,
        'x6': PrizeX6Model,
        'x5': PrizeX5Model,
        'x4': PrizeX4Model,
        'x3': PrizeX3Model,
        'x2': PrizeX2Model,
        'x1': PrizeX1Model
    }

    short_type_name = type_name[:2] if len(type_name) <= 4 else type_name[:3]

    model_class = model_mapping.get(short_type_name)

    return model_class


def make_model_obj(reds_id, item, start, end):
    item_date = datetime.strptime(item.get('date')[:10], "%Y-%m-%d").date()

    base_info = {
        "reds_id": reds_id,
        "reds_code": item.get('code'),
        "date": item_date,
        "pool_money": float(item.get('poolmoney')),
        "sales": int(item.get('sales')),
        "week": item.get('week'),
    }

    for grade in item.get("prizegrades")[start: end]:
        type_name = grade.get("type")
        typemoney = float(grade.get("typemoney") if grade.get("typemoney") else 5000000)
        typenum = int(grade.get("typenum"))

        type_money_name = f"{type_name}_money"
        type_num_name = f"{type_name}_num"
        type_total_name = f"{type_name}_total"

        base_info[type_money_name] = typemoney
        base_info[type_num_name] = typenum
        base_info[type_total_name] = typenum * typemoney

    model_obj = make_model(type_name, base_info)

    return model_obj


def make_model(type_name, base_info):
    model = get_model(type_name)
    return model(**base_info)


def wrap_to_model(reds_id, item):
    """
    将数据接口中返回的奖金相关字段，按照玩法拆解成构造model

    :param prizegrades: list. 中奖信息
    :return:
    """


    model_obj_list = []

    # 选10
    model_obj = make_model_obj(reds_id, item, 0, 7)
    model_obj_list.append(model_obj)

    # 选9
    model_obj = make_model_obj(reds_id, item, 7, 14)
    model_obj_list.append(model_obj)

    # 选8
    model_obj = make_model_obj(reds_id, item, 14, 20)
    model_obj_list.append(model_obj)

    # 选7
    model_obj = make_model_obj(reds_id, item, 20, 25)
    model_obj_list.append(model_obj)

    # 选6
    model_obj = make_model_obj(reds_id, item, 25, 29)
    model_obj_list.append(model_obj)

    # 选5
    model_obj = make_model_obj(reds_id, item, 29, 32)
    model_obj_list.append(model_obj)

    # 选4
    model_obj = make_model_obj(reds_id, item, 32, 35)
    model_obj_list.append(model_obj)

    # 选3
    model_obj = make_model_obj(reds_id, item, 35, 37)
    model_obj_list.append(model_obj)

    # 选2
    model_obj = make_model_obj(reds_id, item, 37, 38)
    model_obj_list.append(model_obj)

    # 选1
    model_obj = make_model_obj(reds_id, item, 38, 39)
    model_obj_list.append(model_obj)

    return model_obj_list