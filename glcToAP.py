from readInput import mainInputReady
from stack import Stack

def makeStates():
    stateDictionary = {}
    states = ['Q0', 'Q1', 'Q2']
    for state in states:
        stateDictionary[state] = []
    return stateDictionary

pilha = Stack()
pilha.showStack()
pilha.stackUp(('S'))
pilha.showStack()
pilha.unstack()
pilha.showStack()
print(pilha.emptyStack())

#data = mainInputReady('input.txt')
#estados = makeStates()
#print(estados)