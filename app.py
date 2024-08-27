from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    get_flashed_messages,
    session,
)
from flask_login import LoginManager
from models import User, db
from config import Config, magic_key_word

print(magic_key_word)
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

# Criar o banco de dados e as tabelas
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username_f"]
        password = request.form["password_f"]
        key_word = request.form["key_word_f"]

        # Verificar se o usuário já existe
        user = User.query.filter_by(username=username).first()

        if key_word != magic_key_word:
            flash("Palavra chave invalida","error")
            return redirect(url_for("register"))

        if user:
            flash("Usuário já existe", "error")
            # return render_template("register.html")
            return redirect(url_for("register"))

        # Criar um novo usuário

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/")
def iniciar():
    return render_template("base.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Verificar se o usuário existe
        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash("Invalid username or password!")
            return redirect(url_for("login"))

        # Armazenar informações do usuário na session
        session["user_id"] = user.id
        session["username"] = user.username

        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", user=user)


@app.route("/logout")
def logout():
    # Limpar a sessão do usuário
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
