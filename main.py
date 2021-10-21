from flask import Flask, render_template, request,redirect,session, flash

from dao import UserDao
from flask_mysqldb import MySQL

from models import Usuario, Campeonato

app = Flask(__name__)
app.secret_key='LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_Camp'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
user_dao = UserDao(db)



@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autenticar',methods=['POST',])
def autenticar():
    usuario = user_dao.buscar(request.form['usuario'])
    if usuario:
        print("entrei aq")
        if usuario._senha== request.form['senha']:
            session['usuario_logado']=request.form['usuario']
            proxima_pagina = request.form['proxima']
            if proxima_pagina != '':
                return redirect('/'+proxima_pagina)
            else:
                return redirect('/')
    flash("Não logado")
    return redirect('/login')

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/registrar_conta',methods=['POST'],)
def registrar_conta():
    nome = request.form['usuario']
    senha = request.form['senha']

    usuario = Usuario(nome, senha,2)
    print(usuario)
    user_dao.criar(usuario)
    return redirect('/')


if __name__ == '__main__':
    app.run()



