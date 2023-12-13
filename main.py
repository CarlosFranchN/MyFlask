from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def inicio():
    return "<p>Hello, World!</p>"


@app.route("/user/<username>")
def show_user(username):
    return f"<h1>User {escape(username)}</h1>"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"


@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {escape(name)}!!</h1>"


@app.route("/projeto/")
def projeto():
    return "Project Page"


@app.route("/sobre")
def sobre():
    return "Sobre pag"


@app.get("/login")
def login_get():
    return show_the_login_form()


@app.route("/form")
def pag():
    return render_template("inicio.html")


@app.post("/process_form")
def form():
    primeiro_nome = request.form["primeiro_nome"]
    segundo_nome = request.form["segundo_nome"]

    # Faça algo com os dados, como imprimir no console para este exemplo
    print(f"Primeiro Nome: {primeiro_nome}, Segundo Nome: {segundo_nome}")

    # Você pode redirecionar para outra página ou renderizar uma página de confirmação
    return "Formulário enviado com sucesso!"


if __name__ == "__main__":
    app.run(debug=True)
    # testesr
