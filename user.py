from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class user(db.Model):
  __tablename__ = 'koncentracja'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  plec = db.Column(db.String(250), nullable=False)
  wiek = db.Column(db.String(250), nullable=False)
  miejsce = db.Column(db.String(250), nullable=False)
  godzina = db.Column(db.String(250), nullable=False)
  samopoczucie = db.Column(db.String(250), nullable=False)
  koncentracja = db.Column(db.String(250), nullable=False)
  problemy = db.Column(db.String(250), nullable=False)
  pora_dnia = db.Column(db.String(250), nullable=False)
  miejsce_koncentracja = db.Column(db.String(250), nullable=False)

#to przeklejone z results
class results(db.Model):
  __tablename__ = 'koncentracja_wyniki'

  id = db.Column(db.Integer, primary_key=True)
  koncentracja_id = db.Column(db.Integer, db.ForeignKey('koncentracja_wyniki.koncentracja_id'), nullable=False) #tu zmiana tego 'koncentracja_wyniki.koncentracja_id'
  score1 = db.Column(db.Text)
