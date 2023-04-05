from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/firma')
def firma():
    return render_template('firma.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/visitas')
def visitas():
    return render_template('visitas.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')