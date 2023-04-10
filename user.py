from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class user(db.Model):
  __tablename__ = 'koncentracja'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  plec = db.Column(db.String(250))
  wiek = db.Column(db.String(250))
  miejsce = db.Column(db.String(250))
  godzina = db.Column(db.String(250))
  samopoczucie = db.Column(db.String(250))
  koncentracja = db.Column(db.String(250))
  problemy = db.Column(db.String(250))
  pora_dnia = db.Column(db.String(250))
  miejsce_koncentracja = db.Column(db.String(250))
