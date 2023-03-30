class Pilha:
    def __init__(self):
        self.pilha = []

    def empilha(self, item):
        item = item[::-1]
        for unidade in range(len(item)):
            self.pilha.append(item[unidade])

    def desempilha(self):
        if len(self.pilha) > 0:
            self.pilha.pop()
    
    def pilhaVazia(self):
        if len(self.pilha) < 1:
            return True
        else:
            return False
        
    def getTopoPilha(self):
        if len(self.pilha) > 0:
            return self.pilha[-1]
    
    def getPilha(self):
        return self.pilha