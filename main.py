from flask import Flask, render_template, request,redirect,session, flash

from dao import UserDao, CampDao, JogoDao
from flask_mysqldb import MySQL

from models import Usuario, Campeonato, Jogo

app = Flask(__name__)
app.secret_key='LP2'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_Camp'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
user_dao = UserDao(db)
campeonato_dao = CampDao(db)
jogo_dao = JogoDao(db)




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
    jogos=jogo_dao.buscar()
    return render_template('novo.html',jogos=jogos)

@app.route('/registrar_conta',methods=['POST'],)
def registrar_conta():
    nome = request.form['usuario']
    senha = request.form['senha']

    usuario = Usuario(nome, senha,2)
    print(usuario)
    user_dao.criar(usuario)
    return redirect('/')

@app.route('/criar_camp',methods=['POST'],)
def criar_camp():

    nome = request.form['nome']
    jogo = request.form['jogo']
    jogo_id = jogo_dao.buscar_id_por_nome(jogo)
    premio = request.form['premio']
    campeonato = Campeonato(nome,premio,jogo_id)
    campeonato_dao.salvar(campeonato)
    return redirect('/')

@app.route('/novo_jogo')
def novo_jogo():

    return render_template('novo_jogo.html')

@app.route('/cad_jogo', methods=['POST'],)
def cad_jogo():
    nome = request.form['nome']
    jogo = Jogo(nome)
    jogo_dao.criar(jogo)
    return redirect('/')

@app.route('/campeonato')
def campeonato():
    camp = []
    dados = campeonato_dao.buscar_camp()
    for i in dados:
        jogo = jogo_dao.buscar_um(i[3])
        jogo=jogo[1]
        camp.append(Campeonato(i[0],i[1],jogo,i[2]))

    return render_template('campeonato.html',camp = camp)

if __name__ == '__main__':
    app.run()



