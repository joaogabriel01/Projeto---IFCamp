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

    def getNome(self):
        return self._nome
    def getPremio(self):
        return self._premio
    def getJogo(self):
        return self._jogo
    def getData(self):
        return self._data

class Jogo:
    def __init__(self,jogo,id=0):
        self._jogo = jogo
        self._id = id

class Transforma:
    @staticmethod
    def transformaStr(x):
        y = []

        for i in x:
            sub = []
            print("i: {}".format(i))
            for z in i:
                sub.append(str(z))
            print("sub: {}".format(sub))
            y.append(sub)
        return y
