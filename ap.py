from readInput import mainInputReady
from pilha import Pilha
from glc import GLC
from estado import Estado
from transicao import Transicao

class AP:
    def __init__(self):
        self.glc = GLC()
        self.pilha = Pilha()
        #Estados
        self.Q0 = Estado('Q0')
        self.Q1 = Estado('Q1')
        self.Q2 = Estado('Q2')
        self.transicoesReconhecidas = []

    def criaTransicoes(self):
        #Transição inicial
        self.Q0.adicionaTransicao(Transicao(self.Q0.nome, '#', '#', self.glc.getVariavelInicial(), self.Q1.nome))
        #Transições terminais
        for terminal in self.glc.getTerminais():
            self.Q1.adicionaTransicao(Transicao(self.Q1.nome, terminal, terminal, '#', self.Q1.nome))
        #Transições com variáveis
        for variavel in self.glc.dados.keys():
            for producao in self.glc.dados[variavel]:
                self.Q1.adicionaTransicao(Transicao(self.Q1.nome, '#', variavel, producao, self.Q1.nome)) 
        #Transição final
        self.Q1.adicionaTransicao(Transicao(self.Q1.nome, '?', '?', '#', self.Q2.nome))
        #Exibe estados:
        '''self.Q0.exibeEstado()
        self.Q1.exibeEstado()'''
    def computaTransicao(self, palavra, transicao):
        self.transicoesReconhecidas.append('({}, {} ,{})'.format(transicao.estadoAtual, palavra, self.pilha.pilha))
    
    #MELHORAR A FORMA DE PERCORRER CADA ESTADO
    def reconhecimento(self, palavra):
        for transicao in self.Q0.transicoes:
            self.pilha.empilha(transicao.simboloEmpilhado)
            self.computaTransicao(palavra, transicao)
        
        for transicao in self.Q1.transicoes:
            #Lendo terminais
            if transicao.simboloLido != '#':
                if self.pilha.getTopoPilha() == palavra[0]:
                    self.pilha.desempilha()
                    palavra = palavra[1:]
            #Lendo variáveis e terminais.
            else:
                if self.pilha.getTopoPilha() == transicao.simboloDesempilhado:
                    self.pilha.desempilha()
                if transicao.simboloEmpilhado != '#':
                    self.pilha.empilha(transicao.simboloEmpilhado)

ap = AP()
ap.criaTransicoes()
ap.reconhecimento('aabbccdd')