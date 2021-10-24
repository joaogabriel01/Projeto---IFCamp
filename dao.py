from models import Usuario, Campeonato, Transforma
#SQL_CRIA_CAMPEONATO = 'insert into tb_campeonatos(Nome, Premio, Data_Camp, idJogos) values (%s, %s, %s,%s)'
SQL_CRIA_CAMPEONATO = 'insert into tb_campeonatos(Nome, Premio, idJogos) values (%s, %s, %s)'
SQL_ATUALIZA_CAMPEONATO = 'UPDATE tb_campeonatos SET Nome=%s, Premio=%s, idJogos=%s where idCampeonato=%s'
SQL_BUSCA_CAMP = 'SELECT Nome, Premio, Data_Camp, idJogos from tb_campeonatos'

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

SQL_CRIA_USUARIO = 'insert into tb_usuarios(usuario, senha, tipo_usuario) values (%s, %s, %s)'
SQL_ATUALIZA_SENHA_USUARIO= 'UPDATE tb_usuarios SET senha=%s where usuario=%s'
SQL_USUARIO= 'SELECT usuario, senha, tipo_usuario from tb_usuarios where usuario=%s'

class UserDao:
    def __init__(self,db):
        self.__db=db
    def criar(self,user):
        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_CRIA_USUARIO, (user._nome,user._senha,user._tipo))
        # cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return user

    def traduz_usuario(self,tupla):
        return Usuario(tupla[0],tupla[1],tupla[2])

    def buscar(self,usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO,(usuario,))
        dados = cursor.fetchone()
        usuario = self.traduz_usuario(dados) if dados else None
        return usuario

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

    def buscar_id(self,nome):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSC_ID_JOGO,(nome,))
        dados = cursor.fetchone()

        return dados

