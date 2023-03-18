from readInput import mainInputReady
from pilha import Pilha
from glc import GLC

class AP:
    def __init__(self):
        self.glc = GLC()
        self.pilha = Pilha()
        self.estados = self.makeStates()
        self.transicoes = self.criaTransicoes()

    def makeStates(self):
        stateDictionary = {}
        states = ['Q0', 'Q1', 'Q2']
        for state in states:
            stateDictionary[state] = []
        return stateDictionary

    def criaTransicoes(self):
        self.estados['Q0'] = ('Q0', '£', '£', )
        pass

ap = AP()
print(ap.estados)
print(ap.glc.terminais)
print(ap.glc.variaveis)