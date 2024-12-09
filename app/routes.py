from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, Message, Admin

# Nome único para o Blueprint
routes = Blueprint('unique_routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/services')
def services():
    return render_template('services.html')

@routes.route('/projects')
def projects():
    return render_template('projects.html')

@routes.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_text = request.form['message']

        if not name or not email or not message_text:
            flash('Todos os campos são obrigatórios!')
            return redirect(url_for('unique_routes.contact'))

        message = Message(name=name, email=email, message=message_text)
        db.session.add(message)
        db.session.commit()
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('unique_routes.contact'))

    return render_template('contact.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password, password):
            session['admin_logged_in'] = True
            flash('Login realizado com sucesso!')
            return redirect(url_for('unique_routes.messages'))
        else:
            flash('Usuário ou senha inválidos!')

    return render_template('login.html')

@routes.route('/mensagens', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_text = request.form['message']

        if not name or not email or not message_text:
            flash('Todos os campos são obrigatórios!')
            return redirect(url_for('unique_routes.messages'))

        message = Message(name=name, email=email, message=message_text)
        db.session.add(message)
        db.session.commit()
        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('unique_routes.messages'))

    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

@routes.route('/sobre')
def about():
    messages = Message.query.all()
    return render_template('about.html', messages=messages)
