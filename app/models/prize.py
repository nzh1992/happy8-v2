from app import db


class PrizeX10Model(db.Model):
    __tablename__ = 'prize_x10'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选10
    x10z10_money = db.Column(db.Float)
    x10z10_num = db.Column(db.Integer)
    x10z10_total = db.Column(db.Float)

    x10z9_money = db.Column(db.Float)
    x10z9_num = db.Column(db.Integer)
    x10z9_total = db.Column(db.Float)

    x10z8_money = db.Column(db.Float)
    x10z8_num = db.Column(db.Integer)
    x10z8_total = db.Column(db.Float)

    x10z7_money = db.Column(db.Float)
    x10z7_num = db.Column(db.Integer)
    x10z7_total = db.Column(db.Float)

    x10z6_money = db.Column(db.Float)
    x10z6_num = db.Column(db.Integer)
    x10z6_total = db.Column(db.Float)

    x10z5_money = db.Column(db.Float)
    x10z5_num = db.Column(db.Integer)
    x10z5_total = db.Column(db.Float)

    x10z0_money = db.Column(db.Float)
    x10z0_num = db.Column(db.Integer)
    x10z0_total = db.Column(db.Float)


class PrizeX9Model(db.Model):
    __tablename__ = 'prize_x9'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))

    # 选9
    x9z9_money = db.Column(db.Float)
    x9z9_num = db.Column(db.Integer)
    x9z9_total = db.Column(db.Float)

    x9z8_money = db.Column(db.Float)
    x9z8_num = db.Column(db.Integer)
    x9z8_total = db.Column(db.Float)

    x9z7_money = db.Column(db.Float)
    x9z7_num = db.Column(db.Integer)
    x9z7_total = db.Column(db.Float)

    x9z6_money = db.Column(db.Float)
    x9z6_num = db.Column(db.Integer)
    x9z6_total = db.Column(db.Float)

    x9z5_money = db.Column(db.Float)
    x9z5_num = db.Column(db.Integer)
    x9z5_total = db.Column(db.Float)

    x9z4_money = db.Column(db.Float)
    x9z4_num = db.Column(db.Integer)
    x9z4_total = db.Column(db.Float)

    x9z0_money = db.Column(db.Float)
    x9z0_num = db.Column(db.Integer)
    x9z0_total = db.Column(db.Float)


class PrizeX8Model(db.Model):
    __tablename__ = 'prize_x8'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))

    # 选8
    x8z8_money = db.Column(db.Float)
    x8z8_num = db.Column(db.Integer)
    x8z8_total = db.Column(db.Float)

    x8z7_money = db.Column(db.Float)
    x8z7_num = db.Column(db.Integer)
    x8z7_total = db.Column(db.Float)

    x8z6_money = db.Column(db.Float)
    x8z6_num = db.Column(db.Integer)
    x8z6_total = db.Column(db.Float)

    x8z5_money = db.Column(db.Float)
    x8z5_num = db.Column(db.Integer)
    x8z5_total = db.Column(db.Float)

    x8z4_money = db.Column(db.Float)
    x8z4_num = db.Column(db.Integer)
    x8z4_total = db.Column(db.Float)

    x8z0_money = db.Column(db.Float)
    x8z0_num = db.Column(db.Integer)
    x8z0_total = db.Column(db.Float)


class PrizeX7Model(db.Model):
    __tablename__ = 'prize_x7'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选7
    x7z7_money = db.Column(db.Float)
    x7z7_num = db.Column(db.Integer)
    x7z7_total = db.Column(db.Float)

    x7z6_money = db.Column(db.Float)
    x7z6_num = db.Column(db.Integer)
    x7z6_total = db.Column(db.Float)

    x7z5_money = db.Column(db.Float)
    x7z5_num = db.Column(db.Integer)
    x7z5_total = db.Column(db.Float)

    x7z4_money = db.Column(db.Float)
    x7z4_num = db.Column(db.Integer)
    x7z4_total = db.Column(db.Float)

    x7z0_money = db.Column(db.Float)
    x7z0_num = db.Column(db.Integer)
    x7z0_total = db.Column(db.Float)


class PrizeX6Model(db.Model):
    __tablename__ = 'prize_x6'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选6
    x6z6_money = db.Column(db.Float)
    x6z6_num = db.Column(db.Integer)
    x6z6_total = db.Column(db.Float)

    x6z5_money = db.Column(db.Float)
    x6z5_num = db.Column(db.Integer)
    x6z5_total = db.Column(db.Float)

    x6z4_money = db.Column(db.Float)
    x6z4_num = db.Column(db.Integer)
    x6z4_total = db.Column(db.Float)

    x6z3_money = db.Column(db.Float)
    x6z3_num = db.Column(db.Integer)
    x6z3_total = db.Column(db.Float)


class PrizeX5Model(db.Model):
    __tablename__ = 'prize_x5'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选5
    x5z5_money = db.Column(db.Float)
    x5z5_num = db.Column(db.Integer)
    x5z5_total = db.Column(db.Float)

    x5z4_money = db.Column(db.Float)
    x5z4_num = db.Column(db.Integer)
    x5z4_total = db.Column(db.Float)

    x5z3_money = db.Column(db.Float)
    x5z3_num = db.Column(db.Integer)
    x5z3_total = db.Column(db.Float)


class PrizeX4Model(db.Model):
    __tablename__ = 'prize_x4'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选4
    x4z4_money = db.Column(db.Float)
    x4z4_num = db.Column(db.Integer)
    x4z4_total = db.Column(db.Float)

    x4z3_money = db.Column(db.Float)
    x4z3_num = db.Column(db.Integer)
    x4z3_total = db.Column(db.Float)

    x4z2_money = db.Column(db.Float)
    x4z2_num = db.Column(db.Integer)
    x4z2_total = db.Column(db.Float)


class PrizeX3Model(db.Model):
    __tablename__ = 'prize_x3'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选3
    x3z3_money = db.Column(db.Float)
    x3z3_num = db.Column(db.Integer)
    x3z3_total = db.Column(db.Float)

    x3z2_money = db.Column(db.Float)
    x3z2_num = db.Column(db.Integer)
    x3z2_total = db.Column(db.Float)


class PrizeX2Model(db.Model):
    __tablename__ = 'prize_x2'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选2
    x2z2_money = db.Column(db.Float)
    x2z2_num = db.Column(db.Integer)
    x2z2_total = db.Column(db.Float)


class PrizeX1Model(db.Model):
    __tablename__ = 'prize_x1'

    id = db.Column(db.Integer, primary_key=True)
    reds_id = db.Column(db.Integer, db.ForeignKey('reds.id'))
    reds_code = db.Column(db.String(20))
    date = db.Column(db.Date)
    pool_money = db.Column(db.Float)
    sales = db.Column(db.Float)
    week = db.Column(db.String(20))
    # 选1
    x1z1_money = db.Column(db.Float)
    x1z1_num = db.Column(db.Integer)
    x1z1_total = db.Column(db.Float)