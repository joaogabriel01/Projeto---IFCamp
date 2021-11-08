from ifcamp.ext.models import Usuario, Campeonato, Transforma
SQL_CRIA_CAMPEONATO = 'insert into tb_campeonatos(nome, premio, idJogos) values (%s, %s, %s)'
SQL_ATUALIZA_CAMPEONATO = 'UPDATE tb_campeonatos SET nome=%s, premio=%s, idJogos=%s where idCampeonato=%s'
SQL_BUSCA_CAMP = 'SELECT nome, premio, dataCamp, idJogos from tb_campeonatos'

class CampDao:
    def __init__(self,db):
        self.__db=db
    def salvar(self,campeonato):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_CAMPEONATO, (campeonato._nome,campeonato._premio,campeonato._jogo))
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


SQL_CRIA_USUARIO = 'INSERT INTO tb_usuarios(usuario, senha, tipoUsuario ) SELECT %s, %s, %s FROM DUAL WHERE NOT EXISTS(SELECT usuario FROM tb_usuarios WHERE usuario = %s)'
SQL_ATUALIZA_SENHA_USUARIO= 'UPDATE tb_usuarios SET senha=%s where usuario=%s'
SQL_ATUALIZA_USUARIO = 'UPDATE tb_usuarios SET usuario=%s, senha=%s, tipoUsuario=%s where idUsuario=%s'
SQL_UM_USUARIO= 'SELECT idUsuario, usuario, senha, tipoUsuario from tb_usuarios where usuario=%s'
SQL_TODOS_USUARIOS = 'SELECT idUsuario, usuario,senha,tipoUsuario from tb_usuarios'

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

    def buscar_todos(self,):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_TODOS_USUARIOS,)
        dados = cursor.fetchall()
        # print(dados)
        usuarios = self.traduz_usuarios(dados) if dados else None
        return usuarios

SQL_CRIA_JOGO = 'INSERT INTO tb_jogos(Nome) SELECT %s FROM DUAL WHERE NOT EXISTS(SELECT Nome FROM tb_jogos WHERE Nome = %s)'
SQL_BUSC_JOGO_1= 'SELECT idJogos, Nome from tb_jogos where idJogos=%s'
SQL_BUSC_JOGO= 'SELECT idJogos, Nome from tb_jogos'
SQL_BUSC_ID_JOGO= 'SELECT idJogos from tb_jogos where Nome=%s'
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
        cursor.execute(SQL_BUSC_JOGO_1,(jogo))
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



