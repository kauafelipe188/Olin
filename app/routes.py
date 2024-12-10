from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models import db, Message, Admin, Project
from datetime import datetime

# Nome único para o Blueprint
routes = Blueprint('unique_routes', __name__)

# Página inicial
@routes.route('/')
def home():
    return render_template('home.html')

# Serviços
@routes.route('/services')
def services():
    return render_template('services.html')

# Projetos
@routes.route('/projects')
def projects():
    projects = Project.query.all()  # Buscando os projetos do banco de dados
    return render_template('projects.html', projects=projects)

# Página de contato
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

# Login
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password_hash, password):
            session.permanent = True  # Define a sessão como permanente
            session['admin_logged_in'] = True
            flash('Login realizado com sucesso!')
            return redirect(url_for('unique_routes.admin_projects'))
        else:
            flash('Usuário ou senha inválidos!')

    return render_template('login.html')

# Logout
@routes.route('/logout', methods=['POST'])
def logout():
    session.pop('admin_logged_in', None)
    flash('Você foi deslogado!')
    return '', 204  # Resposta sem conteúdo para requisições AJAX

# Painel Administrativo - Projetos e Mensagens
@routes.route('/admin/projects', methods=['GET'])
def admin_projects():
    if 'admin_logged_in' not in session:
        flash('Acesso restrito. Faça login para acessar esta página.')
        return redirect(url_for('unique_routes.login'))

    projects = Project.query.all()
    messages = Message.query.all()
    return render_template('admin_projects.html', projects=projects, messages=messages)

# Adicionar um projeto
@routes.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if 'admin_logged_in' not in session:
        flash('Acesso restrito. Faça login para acessar esta página.')
        return redirect(url_for('unique_routes.login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()

        new_project = Project(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )

        db.session.add(new_project)
        db.session.commit()
        flash('Projeto adicionado com sucesso!')
        return redirect(url_for('unique_routes.admin_projects'))

    return render_template('add_project.html')

# Editar um projeto
@routes.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    if 'admin_logged_in' not in session:
        flash('Acesso restrito. Faça login para acessar esta página.')
        return redirect(url_for('unique_routes.login'))

    project = Project.query.get_or_404(project_id)

    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        project.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d').date()

        db.session.commit()
        flash('Projeto atualizado com sucesso!')
        return redirect(url_for('unique_routes.admin_projects'))

    return render_template('edit_project.html', project=project)

# Excluir um projeto
@routes.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    if 'admin_logged_in' not in session:
        flash('Acesso restrito. Faça login para acessar esta página.')
        return redirect(url_for('unique_routes.login'))

    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Projeto excluído com sucesso!')
    return redirect(url_for('unique_routes.admin_projects'))

# Sobre
@routes.route('/about')
def about():
    return render_template('about.html')
