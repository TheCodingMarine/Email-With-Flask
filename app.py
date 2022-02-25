from email import message
import os
from flask import Flask
from flask_mail import Mail, Message


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')


mail = Mail(app)


@app.route("/")
def index():
    
    msg = Message("This is a test!", sender=app.config['MAIL_USERNAME'],
                  recipients=[os.environ.get('RECIPIENT')])
    msg.body = 'This is a test!'
    mail.send(msg)
    return 'Mail Sent'