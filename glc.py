from readInput import mainInputReady

class GLC:
    def __init__(self):
        self.dados = mainInputReady()
        self.variaveis = self.getVariaveis()
        self.terminais = self.getTerminais()
        self.variavelInicial = self.getVariavelInicial()
        self.terminaisProducao = self.getTerminaisProducao()
        self.variaveisProducao = self.getVariaveisProducao()
    
    def unico(self, string):
        return list(set(string))
    
    def getVariaveisProducao(self):
        variaveisProducao = []
        for variavel in self.variaveis:
            for producao in self.dados[variavel]:
                if producao.isupper():
                    variaveisProducao.append(producao)
        return variaveisProducao
    
    def getTerminaisProducao(self):
        variaveisProducao = []
        for variavel in self.variaveis:
            for producao in self.dados[variavel]:
                if producao.islower():
                    variaveisProducao.append(producao)
        return variaveisProducao

    def getVariaveis(self):
        variaveis = list(self.dados.keys())
        return variaveis
    
    def getVariavelInicial(self):
        return self.variaveis[0]
    
    def getTerminais(self):
        stringTerminais = ''
        for itens in self.dados.keys():
            for item in self.dados[itens]:
                if item.islower():
                    stringTerminais+=item
        return self.unico(stringTerminais)