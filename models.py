class Usuario:
    def __init__(self,nome,senha,tipo):
        self._nome = nome
        self._senha = senha
        self._tipo = tipo

class Campeonato:
    def __init__(self,nome,premio,jogo,data=0):

        self._nome = nome
        self._premio = premio
        self._jogo = jogo
        self._data = data

class Jogo:
    def __init__(self,jogo,id=0):
        self._jogo = jogo
        self._id = id