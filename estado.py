class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.transicoes = []
    
    def adicionaTransicao(self, transicao):
        self.transicoes.append(transicao)
    
    def exibeEstado(self):
        for i in self.transicoes:
            i.exibeTransicao()