from flask import Flask, render_template, request,redirect,session, flash
app = Flask(__name__)
app.secret_key='LP2'

class Usuario:
    def __init__(self,id,nome,senha):
        self._id = id
        self._nome = nome
        self._senha = senha

usuario1 = Usuario('joaogf','Joao Gabriel','1234')
usuario2 = Usuario('pedrosd', 'Pedro Paulo','123123')

usuarios={usuario1._id:usuario1,usuario2._id:usuario2}

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = ''
    return render_template('login.html', proxima=proxima)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autenticar',methods=['POST',])
def autenticar():
    print(request.form['usuario'])
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario._senha== request.form['senha']:
            session['usuario_logado']=request.form['usuario']
            proxima_pagina = request.form['proxima']
            if proxima_pagina != '':
                return redirect('/'+proxima_pagina)
            else:
                return redirect('/')
    flash("Não logado")
    return redirect('/login')





if __name__ == '__main__':
    app.run()



