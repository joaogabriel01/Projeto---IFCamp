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

class Time:
    def __init__(self,id,nome,jogadores):
        self._id = id
        self._nome = nome

        self._jogadores = jogadores



class Campeonato:
    def __init__(self,id,nome,premio,jogo,qtdJogTime=5,data="",status=1):
        self._id = id
        self._nome = nome
        self._premio = premio
        self._jogo = jogo
        self._data = data
        self._qtdJogTime = qtdJogTime
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
    def getId(self):
        return self._id
    def getQtdJogTime(self):
        return self._qtdJogTime
        

class Jogo:
    def __init__(self,jogo,status=1,id_jogo=0):
        self._jogo = jogo
        self._id = id_jogo
        self._status = status

    def getJogo(self):
        return self._jogo
    def getId(self):
        return self._id
    def getStatus(self):
        return self._status

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
