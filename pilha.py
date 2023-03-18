class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, item):
        self.stack.append(item)

    def desempilhar(self):
        if len(self.stack) > 0:
            self.stack.pop()
    
    def exibePilha(self):
        print(self.stack)
    
    def pilhaVazia(self):
        if len(self.stack) < 1:
            return True
        else:
            return False