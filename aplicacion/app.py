from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)


# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'jerez.ricardo09@gmail.com'
app.config['MAIL_PASSWORD'] = 'uimgymohuknlsari'

mail = Mail(app)



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
    return render_template('inicio.html')

@app.route('/visitas')
def visitas():
    return render_template('inicio.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Procesar los datos y enviar un correo electrónico
        msg = Message('Mensaje de ' + name, sender=email, recipients=['jerez.ricardo09@gmail.com'])
        msg.body = message
        mail.send(msg)

        # Devolver una respuesta al usuario
        return render_template('inicio.html')
    else:
        # Renderizar el formulario HTML
        return render_template('contacto.html')