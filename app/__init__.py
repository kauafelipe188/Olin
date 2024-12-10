from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta

# Configuração da aplicação
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Sessão dura 30 minutos

# Inicialização do banco de dados e migrações
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importação e registro do Blueprint
from .routes import routes
app.register_blueprint(routes)
