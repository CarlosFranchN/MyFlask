from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager
from models import User,db,load_user
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Criar o banco de dados e as tabelas
with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar se o usuário já existe
        user = User.query.filter_by(name=username).first()
        if user:
            return render_template('register.html', message='Username already exists.')

        # Criar um novo usuário
        new_user = User(name=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar se o usuário existe
        user = User.query.filter_by(name=username).first()

        if user is None or not user.check_password(password):
            flash('Login Invalido!')
            return redirect(url_for('login'))

        # Armazenar informações do usuário na session
        session['user_id'] = user.id
        session['username'] = user.name

        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    # Limpar a sessão do usuário
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
