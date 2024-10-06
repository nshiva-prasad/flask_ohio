from . import db

class WellData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_well_number = db.Column(db.String, nullable=False)
    oil = db.Column(db.Integer, nullable=False)
    gas = db.Column(db.Integer, nullable=False)
    brine = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<WellData {self.api_well_number}>"
