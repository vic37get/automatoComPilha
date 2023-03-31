class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.transicoes = []
    
    def adicionaTransicao(self, transicao):
        self.transicoes.append(transicao)
    
    def exibeEstado(self):
        transicoes = ''
        for i in self.transicoes:
            transicoes += i.exibeTransicao()+'\n'
        return transicoes
            
    
    def getEstados(self):
        for transicao in self.transicoes:
            return transicao.getTransicao()