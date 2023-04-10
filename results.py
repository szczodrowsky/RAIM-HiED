from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class results(db.Model):
  __tablename__ = 'testy'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('koncentracja.id'), nullable=False)
  score1 = db.Column(db.Text, nullable=False)
  score2 = db.Column(db.Text, nullable=False)


