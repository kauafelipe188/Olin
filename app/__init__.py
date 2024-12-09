from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Configuração da aplicação
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados e migrações
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importação e registro do Blueprint
from .routes import routes

# Registro correto do Blueprint
app.register_blueprint(routes)  # Removido o parâmetro `name`
