from flask import * 
from markupsafe import escape

app = Flask(__name__)
# forma de identificar o principal
@app.route('/')
@app.route('/index')
def index ():
    nomesList = ["Carlos","Pedro", "Mari","Vitoria"]
    return render_template('index.html', nomes = nomesList)

@app.route('/sobre')
def sobre():
    return  render_template('sobre.html')

@app.route('/hello/<name>')
def helloP(name):
    return f"<h1>Hello, {escape(name)}!!</h1>"



if __name__ =='__main__':
    app.run(debug=True)
    # testesr

   
