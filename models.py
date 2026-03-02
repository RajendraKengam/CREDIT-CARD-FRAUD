from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Prediction(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    prediction = db.Column(db.Integer, nullable=False)
    fraud_probability = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Prediction id={self.id} pred={self.prediction} prob={self.fraud_probability:.4f}>"
