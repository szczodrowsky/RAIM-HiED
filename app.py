from flask import Flask, render_template, jsonify, request, redirect, session
import random
import os
from flask_sqlalchemy import SQLAlchemy
from user import user, results, kolka  #zmiana importu
#from results import results

db = SQLAlchemy()

#Data Base

app = Flask(__name__)
app.secret_key = "ksemwetipg"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('db_conn')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def page0():
  return render_template('ankieta.html')


@app.route("/page2")
def page2():
  session.clear()
  return render_template('ankieta.html')


@app.route('/page3', methods=['GET', 'POST'])
def data_to_db():
  try:
    if request.method == 'POST':
      plec = request.form['plec'],
      wiek = request.form['wiek'],
      godzina = request.form['godzina'],
      miejsce = request.form['miejsce'],
      samopoczucie = request.form['samopoczucie'],
      koncentracja = request.form['koncentracja'],
      problemy = request.form['problemy'],
      pora_dnia = request.form['pora_dnia'],
      miejsce_koncentracja = request.form['miejsce_koncentracja'],
      techniki  = request.form['techniki'],
      przerwanie  = request.form['przerwanie'],
      telefon = request.form['telefon']

    new_user = user(plec=plec,
                    wiek=wiek,
                    godzina=godzina,
                    miejsce=miejsce,
                    samopoczucie=samopoczucie,
                    koncentracja=koncentracja,
                    problemy=problemy,
                    pora_dnia=pora_dnia,
                    miejsce_koncentracja=miejsce_koncentracja,
                    techniki=techniki,
                    przerwanie=przerwanie,
                    telefon = telefon
                   )
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id

    return redirect('/page4')
  except Exception as e:
    db.session.rollback()
    print(str(e))
    return redirect('/erorr')


@app.route('/page4')
def page4():
  return render_template('opis1.html')


@app.route('/page5')
def page5():
  return render_template('colors.html')


@app.route('/page6', methods=['GET', 'POST'])
def results_to_db():
  try:
    if request.method == 'POST':
      score1 = request.json['score1']

    new_test = results(koncentracja_id=session['user_id'], score1=score1)
    db.session.add(new_test)
    db.session.commit()

    return jsonify({'success': True})

  except Exception as e:
    db.session.rollback()
    print(str(e))
    return redirect('/erorr')


@app.route("/page7")
def page7():
  return render_template('opis2.html')


@app.route('/get_color')
def get_color():
  colors = ['red', 'blue', 'green']
  color = random.choice(colors)
  return jsonify(color)


@app.route('/get_data')
def get_data():
  sizes = [125, 150, 100]
  numbers = random.sample(range(1, 9), 2)
  bigger_circle = random.choice([0, 1])
  if numbers[0] > numbers[1]:
    command = 'Kliknij większe koło'
  else:
    command = 'Wybierz większą cyfrę'
  random_sizes = random.sample(sizes, 2)
  data = {
    'sizes': random_sizes if bigger_circle == 0 else random_sizes[::-1],
    'numbers': numbers,
    'bigger_circle': bigger_circle,
    'command': command
  }
  return jsonify(data)


@app.route("/page8")
def page8():
  return render_template('kolka.html')

@app.route('/page9', methods=['POST'])
def kolka_to_db():
  try:
    score2 = None
    if request.method == 'POST':
      score2 = request.json['score2']

    new_kolka = kolka(koncentracja_id=session['user_id'], score2=score2)
    db.session.add(new_kolka)
    db.session.commit()

    return jsonify({'success': True})

  except Exception as e:
    db.session.rollback()
    print(str(e))
    return redirect('/erorr')


@app.route("/final")
def page10():
  return render_template('final.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
