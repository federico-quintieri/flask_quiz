from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, default=0)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer_a = db.Column(db.String(255), nullable=False)
    answer_b = db.Column(db.String(255), nullable=False)
    answer_c = db.Column(db.String(255), nullable=False)
    answer_d = db.Column(db.String(255), nullable=False) 
    correct = db.Column(db.Integer, nullable=False)
