from app import db


class RedsModel(db.Model):
    __tablename__ = 'reds'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    red1 = db.Column(db.Integer, nullable=False)
    red2 = db.Column(db.Integer, nullable=False)
    red3 = db.Column(db.Integer, nullable=False)
    red4 = db.Column(db.Integer, nullable=False)
    red5 = db.Column(db.Integer, nullable=False)
    red6 = db.Column(db.Integer, nullable=False)
    red7 = db.Column(db.Integer, nullable=False)
    red8 = db.Column(db.Integer, nullable=False)
    red9 = db.Column(db.Integer, nullable=False)
    red10 = db.Column(db.Integer, nullable=False)
    red11 = db.Column(db.Integer, nullable=False)
    red12 = db.Column(db.Integer, nullable=False)
    red13 = db.Column(db.Integer, nullable=False)
    red14 = db.Column(db.Integer, nullable=False)
    red15 = db.Column(db.Integer, nullable=False)
    red16 = db.Column(db.Integer, nullable=False)
    red17 = db.Column(db.Integer, nullable=False)
    red18 = db.Column(db.Integer, nullable=False)
    red19 = db.Column(db.Integer, nullable=False)
    red20 = db.Column(db.Integer, nullable=False)
    
    def __init__(self, code, reds):
        super().__init__()
        self.code = code
        self._reds = reds

        for idx, red in enumerate(reds):
            attr_name = f"red{idx + 1}"
            setattr(self, attr_name, red)

    def get_sum(self):
        """获取本期和值"""
        return sum(self._reds)

    def __repr__(self):
        return f"<RedsModel id:{self.id} code:{self.code}>"
        