from app import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    image = db.Column(db.String(100))  # Caminho da imagem do projeto.
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @property
    def progress(self):
        """Calcula o progresso com base no tempo decorrido."""
        now = datetime.utcnow().date()
        if now < self.start_date:
            return 0
        elif now > self.end_date:
            return 100
        else:
            total_duration = (self.end_date - self.start_date).days
            elapsed_time = (now - self.start_date).days
            return int((elapsed_time / total_duration) * 100)
