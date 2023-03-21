class Pilha:
    def __init__(self):
        self.pilha = []

    def empilha(self, item):
        for unidade in range(len(item)):
            self.pilha.append(unidade)

    def desempilha(self):
        if len(self.pilha) > 0:
            self.pilha.pop()
    
    def exibePilha(self):
        print(self.pilha)
    
    def pilhaVazia(self):
        if len(self.pilha) < 1:
            return True
        else:
            return False
        
    def getTopoPilha(self):
        return self.pilha[-1]