from datetime import time
from flask import Flask, render_template, request,redirect,session, flash


from ifcamp.ext.dao import TimeCampDao, TimeDao, UserDao, CampDao, JogoDao
from ifcamp.ext.models import Time, Usuario, Campeonato, Jogo

from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key='LP2'





app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_Camp1'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
user_dao = UserDao(db)
campeonato_dao = CampDao(db)
jogo_dao = JogoDao(db)
time_dao = TimeDao(db)
time_camp_dao = TimeCampDao(db)




@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar',methods=['POST',])
def autenticar():
    usuario = user_dao.buscar_um(request.form['usuario'])
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

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/registrar_conta',methods=['POST'],)
def registrar_conta():
    nome = request.form['usuario']
    senha = request.form['senha']

    # Coloco id 0 porque não vai fazer diferença
    usuario = Usuario(0, nome, senha,1)
    print(usuario)
    user_dao.criar(usuario)
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/novo')
def novo():
    jogos=jogo_dao.buscar()
    return render_template('novo.html',jogos=jogos)


@app.route('/criar_camp',methods=['POST'],)
def criar_camp():

    nome = request.form['nome']
    jogo = request.form['jogo']
    qtd = request.form['qtd_jogadores']
    data = request.form['data_campeonato']
    data = data + ' 9:00:00'
    jogo_id = jogo_dao.buscar_id_por_nome(jogo)
    premio = request.form['premio']
    campeonato = Campeonato(nome,premio,jogo_id,qtd,data)
    print(campeonato.getData())
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
    jogos = []
    dados = campeonato_dao.buscar_camp()
    for i in dados:
        jogo = jogo_dao.buscar_um(i[4])
        jogo=jogo[1]
        camp.append(Campeonato(i[0],i[1],i[2],jogo,i[3],i[5]))

    dados = jogo_dao.buscar()
    for i in dados:
        jogos.append(i)

    return render_template('campeonato.html',camp = camp, jogos=jogos)

@app.route('/cadastrar_time', methods=['POST'],)
def cadastrar_time():
    id = request.form['id']
    qtd = request.form['qtd']
    print(qtd)

    return render_template('cadastrar_time.html',qtd = int(qtd),id = int(id))

@app.route('/registra_time',methods=['POST'],)
def registra_time():
    nome = request.form['nomeTime']
    id_camp = request.form['idcamp']

    jogadores = []
    for i in request.form:
        jogadores.append(request.form[i])
    del[jogadores[0]]
    del[jogadores[0]]
    time = Time(1,nome,jogadores)
    time_dao.criar(time)
    time_dao.insere_jogadores(time)

    time_camp_dao.criar(time,id_camp)



    return render_template('sucesso.html')
    # time = Time(1,nome,)


@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/admin/usuarios')
def admin_usuarios():
    usuarios = user_dao.buscar_todos()
    print(usuarios)
    if usuarios is None:
        usuarios = []
    return render_template('admin/usuarios.html', usuarios = usuarios)


@app.route('/admin/altera_usuario/<int:id>')
def altera_usuario(id):
    usuario = user_dao.buscar_um_user_pid(id)
    return render_template('admin/altera_usuario.html', usuario=usuario)

@app.route('/admin/realiza_atualizacao', methods=['POST'],)
def realiza_atualizacao():
    id_user = request.form['id']
    nome = request.form['nome']
    senha = request.form['senha']
    tipo = request.form['tipo']
    print(type(id_user))
    print(nome)
    usuario = Usuario(id_user,nome,senha,tipo)
    user_dao.atualiza(usuario)
    return redirect('/admin')

@app.route('/admin/excluir_usuario/<int:id>')
def excluir_usuario(id):
    user_dao.excluir_usuario(id)
    return redirect('/admin')

if __name__ == '__main__':
    app.run()



@app.route('/admin/jogos')
def admin_jogos():
    jogos_dados = jogo_dao.buscar()

    jogos = []
    for i in jogos_dados:
        jogo = Jogo(i[1],i[2],i[0])
        jogos.append(jogo)
    if jogos is None:
        jogos = []
    print(jogos_dados)
    print(jogos)
    return render_template('admin/jogos.html', jogos = jogos)
    
@app.route('/admin/altera_jogo/<int:id>')
def altera_jogo(id):
    jogo = jogo_dao.buscar_um(id)
    print(jogo)
    novo_jogo = Jogo(jogo[1],jogo[2],jogo[0])
    return render_template('admin/altera_jogo.html', jogo=novo_jogo)

@app.route('/admin/realiza_atualizacao_jogo', methods=['POST'],)
def realiza_atualizacao_jogo():
    id_jogo = request.form['id']
    nome = request.form['nome']
    status = request.form['status']
    jogo = Jogo(nome,status,id_jogo)
    jogo_dao.atualiza(jogo)
    return redirect('/admin')

@app.route('/admin/excluir_jogo/<int:id>')
def excluir_jogo(id):
    jogo_dao.excluir_jogo_id(id)
    return redirect('/admin')


@app.route('/admin/campeonatos')
def admin_campeonatos():
    camp = []
    dados = campeonato_dao.buscar_camp()
    

    for i in dados:
        jogo = jogo_dao.buscar_um(i[4])
        jogo=jogo[1]
        camp.append(Campeonato(i[0],i[1],i[2],jogo,i[3],i[5]))

    return render_template('admin/campeonatos.html', camp = camp)
    
@app.route('/admin/altera_campeonato/<int:id>')
def altera_campeonato(id):
    camp = campeonato_dao.buscar_um_camp(id)
    editar_camp = Campeonato(camp[0],camp[1],camp[2],camp[4],camp[3],camp[5])
    return render_template('admin/altera_campeonato.html', camp=editar_camp)

@app.route('/admin/excluir_campeonato/<int:id>')
def excluir_campeonato(id):
    campeonato_dao.excluir_camp(id)
    return redirect('/admin')