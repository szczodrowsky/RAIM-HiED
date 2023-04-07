from flask import Flask, render_template,jsonify,request
import random
from database import full_db

app = Flask(__name__)

@app.route("/")
def page0():
  return render_template('home.html')

@app.route("/ankieta")
def page1():
  return render_template('ankieta.html')

@app.route("/opis1")
def page2():
  return render_template('opis1.html')

@app.route('/colors')
def page4():
  return render_template('colors.html')

@app.route("/opis2")
def page5():
  return render_template('opis2.html')

@app.route('/get_color')
def get_color():
  colors = ['red', 'blue', 'green']
  color = random.choice(colors)
  return jsonify(color)

@app.route('/get_data')
def get_data():
  sizes = [125,150,100]
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

@app.route("/kolka")
def page6():
  return render_template('kolka.html')
  

@app.route("/final", methods=['get'])
def page7():
    data = request.args
    full_db(data)
    return render_template('final.html',data=data)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)