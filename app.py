from flask import Flask, render_template, request, redirect, flash, url_for
from flask_migrate import Migrate
from utils import db
from models.Mensagem import Mensagem
from controllers.Mensagem import bp_mensagens


app = Flask(__name__)
app.register_blueprint(bp_mensagens, url_prefix='/mensagens')

app.config['SECRET_KEY'] = 'segredinho'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')