class Usuario:
    def __init__(self,nome,senha,tipo):
        self._nome = nome
        self._senha = senha
        self._tipo = tipo

class Campeonato:
    def __init__(self,id,nome,premio,jogo,data):
        self._id = id
        self._nome = nome
        self._premio = premio
        self._jogo = jogo
        self._data = data