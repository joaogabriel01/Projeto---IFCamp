from ifcamp.ext.models import Usuario, Campeonato, Transforma
SQL_CRIA_CAMPEONATO = 'insert into tb_campeonatos(nome, premio, idJogos, qtdJogTime, idStatus, dataCamp) values (%s, %s, %s,%s,%s,%s)'
SQL_ATUALIZA_CAMPEONATO = 'UPDATE tb_campeonatos SET nome=%s, premio=%s, idJogos=%s, idStatus=%s where idCampeonato=%s'
SQL_BUSCA_CAMP = 'SELECT idCampeonato ,nome, premio, qtdJogTime, idJogos, dataCamp from tb_campeonatos'
SQL_BUSCA_UM_CAMP = 'SELECT idCampeonato ,nome, premio, qtdJogTime, idJogos, dataCamp from tb_campeonatos where idCampeonato = %s'
SQL_EXCLUIR_CAMP = 'DELETE from tb_campeonatos where idCampeonato=%s'

class CampDao:
    def __init__(self,db):
        self.__db=db
    def salvar(self,campeonato):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_CAMPEONATO, (campeonato._nome,campeonato._premio,campeonato._jogo,campeonato._qtdJogTime,campeonato._status,campeonato._data))
        cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        return campeonato

    def buscar_camp(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CAMP)
        dados = cursor.fetchall()
        print("dados = {}".format(dados))
        dados = Transforma.transformaStr(dados)
        print("dados = {}".format(dados))
        return dados
    def buscar_um_camp(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_UM_CAMP,(id,))
        dados = cursor.fetchone()
        return dados
    def excluir_camp(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EXCLUIR_CAMP,(id,))
        return 1


SQL_CRIA_USUARIO = 'INSERT INTO tb_usuarios(usuario, senha, idTipoUsuario ) SELECT %s, %s, %s FROM DUAL WHERE NOT EXISTS(SELECT usuario FROM tb_usuarios WHERE usuario = %s)'
SQL_ATUALIZA_SENHA_USUARIO= 'UPDATE tb_usuarios SET senha=%s where usuario=%s'
SQL_ATUALIZA_USUARIO = 'UPDATE tb_usuarios SET usuario=%s, senha=%s, idTipoUsuario=%s where idUsuario=%s'
SQL_UM_USUARIO= 'SELECT idUsuario, usuario, senha, idTipoUsuario from tb_usuarios where usuario=%s'
SQL_TODOS_USUARIOS = 'SELECT idUsuario, usuario,senha,idTipoUsuario from tb_usuarios'
SQL_BUSCA_USUARIO_ID = 'SELECT idUsuario, usuario, senha, idTipoUsuario from tb_usuarios where idUsuario=%s'
SQL_EXCLUIR_USUARIO = 'DELETE FROM tb_usuarios WHERE idUsuario=%s'

class UserDao:
    def __init__(self,db):
        self.__db=db
    def criar(self,user):
        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_CRIA_USUARIO, (user._nome,user._senha,user._tipo, user._nome))
        # cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return user
    def atualiza(self,user):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATUALIZA_USUARIO, (user._nome,user._senha,user._tipo, user._iduser))
        self.__db.connection.commit()

    def altera_senha_usuario(self,senha,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATUALIZA_SENHA_USUARIO,(senha,usuario))

    def traduz_usuario(self,tupla):
        return Usuario(tupla[0],tupla[1],tupla[2],tupla[3])

    def traduz_usuarios(self,usuarios):
        def traduz_usuario(tupla):
            return Usuario(tupla[0],tupla[1],tupla[2],tupla[3])
        return list(map(traduz_usuario,usuarios))

    def buscar_um(self,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_UM_USUARIO,(usuario,))
        dados = cursor.fetchone()
        
        usuario = self.traduz_usuario(dados) if dados else None
        return usuario
    def buscar_um_user_pid(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIO_ID,(id,))
        dados = cursor.fetchone()
        
        usuario = self.traduz_usuario(dados) if dados else None
        return usuario

    def buscar_todos(self,):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_TODOS_USUARIOS,)
        dados = cursor.fetchall()
        # print(dados)
        usuarios = self.traduz_usuarios(dados) if dados else None
        return usuarios

    def excluir_usuario(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EXCLUIR_USUARIO,(id,))
        self.__db.connection.commit()
        return 1



SQL_CRIA_JOGO = 'INSERT INTO tb_jogos(Nome,idStatus) SELECT %s,1 FROM DUAL WHERE NOT EXISTS(SELECT Nome FROM tb_jogos WHERE Nome = %s)'
SQL_BUSC_JOGO_1= 'SELECT idJogos, Nome, idStatus from tb_jogos where idJogos=%s'
SQL_BUSC_JOGO= 'SELECT idJogos, Nome, idStatus from tb_jogos'
SQL_BUSC_ID_JOGO= 'SELECT idJogos from tb_jogos where Nome=%s'
SQL_EXCLUIR_JOGO_ID = 'DELETE FROM tb_jogos where idJogos=%s'
SQL_ATUALIZA_JOGO = 'UPDATE tb_jogos SET Nome=%s, idStatus=%s where idJogos=%s'
class JogoDao:
    def __init__(self,db):
        self.__db=db
    def criar(self,jogo):
        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_CRIA_JOGO, (jogo._jogo,jogo._jogo,))
        # cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return jogo

    def buscar_um(self,jogo):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSC_JOGO_1,(jogo,))
        dados = cursor.fetchone()
        print(dados)
        return dados

    def buscar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSC_JOGO)
        dados = cursor.fetchall()
        return dados

    def buscar_id_por_nome(self,nome):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSC_ID_JOGO,(nome,))
        dados = cursor.fetchone()
        print(dados)
        return dados[0]
    
    def excluir_jogo_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EXCLUIR_JOGO_ID,(id,))
        self.__db.connection.commit()
        return 1

    def atualiza(self,jogo):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATUALIZA_JOGO, (jogo._jogo,jogo._status,))
        self.__db.connection.commit()


SQL_CRIA_TIME = 'INSERT INTO tb_times(nome) values(%s)'
SQL_RETORNA_ID_NOME = 'SELECT idTime from tb_times where nome = %s'
SQL_INSERT_JOGADORES = 'INSERT INTO tb_usuarios_times(idUsuario,idTime) values(%s,%s)'
class TimeDao:
    def __init__(self,db):
        self.__db=db
    def criar(self,time):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_TIME, (time._nome,))
        self.__db.connection.commit()
        return time
    def insere_jogadores(self,time):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RETORNA_ID_NOME, (time._nome,))
        id_time = cursor.fetchone()
        for i in time._jogadores:
            cursor.execute(SQL_INSERT_JOGADORES, (i,id_time[0]))
        self.__db.connection.commit()
        return time


SQL_CRIA_CAMP_TIME = 'INSERT INTO tb_campeonatos_times(idCampeonato, idtime) values(%s,%s)'
SQL_RETORNA_ID_NOME = 'SELECT idTime from tb_times where nome = %s'
class TimeCampDao:
    
    def __init__(self,db):
        self.__db=db
    def criar(self,time,id_camp):
        
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RETORNA_ID_NOME, (time._nome,))
        id_time = cursor.fetchone()
        print(id_time[0])
        cursor.execute(SQL_CRIA_CAMP_TIME, (id_camp,id_time[0],))
        self.__db.connection.commit()
        return time