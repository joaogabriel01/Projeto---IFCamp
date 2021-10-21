from models import Usuario
#SQL_CRIA_CAMPEONATO = 'insert into tb_campeonatos(Nome, Premio, Data_Camp, idJogos) values (%s, %s, %s,%s)'
SQL_CRIA_CAMPEONATO = 'insert into tb_campeonatos(Nome, Premio, idJogos) values (%s, %s, %s)'
SQL_ATUALIZA_CAMPEONATO = 'UPDATE tb_campeonatos SET Nome=%s, Premio=%s, idJogos=%s where idCampeonato=%s'

class CampDao:
    def __init__(self,db):
        self.__db=db
    def salvar(self,campeonato):
        cursor = self.__db.connection.cursor()

        if(campeonato._id):
            cursor.execute(SQL_ATUALIZA_CAMPEONATO, (campeonato._nome,campeonato._premio,campeonato._jogo,campeonato._id))
        else:
            cursor.execute(SQL_CRIA_CAMPEONATO, (campeonato._nome,campeonato._premio,campeonato._jogo))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return campeonato

SQL_CRIA_USUARIO = 'insert into tb_usuarios(usuario, senha, tipo_usuario) values (%s, %s, %s)'
SQL_ATUALIZA_SENHA_USUARIO= 'UPDATE tb_usuarios SET senha=%s where usuario=%s'
SQL_USUARIO= 'SELECT usuario, senha, tipo_usuario from tb_usuarios where usuario=%s'

class UserDao:
    def __init__(self,db):
        self.__db=db
    def criar(self,user):
        cursor = self.__db.connection.cursor()

        cursor.execute(SQL_CRIA_USUARIO, (user._nome,user._senha,user._tipo))
        cursor._id = cursor.lastrowid

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

