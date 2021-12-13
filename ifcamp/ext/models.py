class Usuario:
    def __init__(self,iduser,nome,senha,tipo):
        self._iduser = iduser
        self._nome = nome
        self._senha = senha
        self._tipo = tipo

    def getID(self):
        return self._iduser
    def getNome(self):
        return self._nome
    def getSenha(self):
        return self._senha
    def getTipo(self):
        return self._tipo

class Campeonato:
    def __init__(self,nome,premio,jogo,data=0,status=1):

        self._nome = nome
        self._premio = premio
        self._jogo = jogo
        self._data = data
        self._status = status

    def getNome(self):
        return self._nome
    def getPremio(self):
        return self._premio
    def getJogo(self):
        return self._jogo
    def getData(self):
        return self._data
    def getStatus(self):
        return self._status

class Jogo:
    def __init__(self,jogo,status=1,id=0):
        self._jogo = jogo
        self._id = id
        self._status = status

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
