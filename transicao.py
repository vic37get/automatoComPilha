class Transicao:
    def __init__(self, estadoAtual, simboloLido, simboloDesempilhado, simboloEmpilhado, estadoDestino):
        self.estadoAtual = estadoAtual
        self.simboloLido = simboloLido
        self.simboloEmpilhado = simboloEmpilhado
        self.simboloDesempilhado = simboloDesempilhado
        self.estadoDestino = estadoDestino
    
    def getTransicao(self):
        return [self.simboloLido, self.simboloDesempilhado,self.simboloEmpilhado]
        #print('Estado atual: {}\nSimbolo lido: {}\nSimbolo empilhado: {}\nSimbolo desempilhado: {}\nEstado destino: {}\n'.format(self.estadoAtual,
        #self.simboloLido, self.simboloEmpilhado, self.simboloDesempilhado, self.estadoDestino))
    
    def exibeTransicao(self):
        print('({},{},{})'.format(self.simboloLido, self.simboloDesempilhado, self.simboloEmpilhado))
        #print('Estado atual: {}\nSimbolo lido: {}\nSimbolo empilhado: {}\nSimbolo desempilhado: {}\nEstado destino: {}\n'.format(self.estadoAtual,
        #self.simboloLido, self.simboloEmpilhado, self.simboloDesempilhado, self.estadoDestino))