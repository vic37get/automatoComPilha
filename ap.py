from pilha import Pilha
from glc import GLC
from estado import Estado
from transicao import Transicao
from copy import deepcopy
from readInput import readInputOneLine

class AP:
    def __init__(self):
        #Gramática, Pilha
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
        #self.Q0.exibeEstado()
        #self.Q1.exibeEstado()

    def computaTransicaoPercorrida(self, palavra, transicao):
        self.transicoesReconhecidas.append('({}, {} ,{})'.format(transicao.estadoAtual, palavra, self.pilha.pilha))
    
    def primeiroCaractere(self, palavraAtual):
        if len(palavraAtual) > 0:
            return palavraAtual[0]
        return None
    
    #Gera as transições possíveis a partir do estado atual.
    def possiveisTransicoes(self, estadoAtual, palavraAtual, pilhaAtual, profundidade):
        transicoesCandidatas = []
        for transicao in self.Q1.transicoes:
            #Se o simbolo lido for igual ao simbolo na cabeça da fita ou o simbolo lido é vazio.
            if transicao.simboloLido == self.primeiroCaractere(palavraAtual) or transicao.simboloLido == '#':
                #Se o simbolo desempilhado na transição for igual ao do topo da pilha ou se não desempilhar nada.
                if transicao.simboloDesempilhado == pilhaAtual.getTopoPilha() or transicao.simboloDesempilhado == '#':
                    #print('Transicao: ',transicao.getTransicao())
                    palavraNova, pilhaNova, profundidadeNova = self.computaEstadoAtual(palavraAtual, pilhaAtual, transicao, profundidade)
                    transicoesCandidatas.append([estadoAtual, palavraNova, pilhaNova, profundidadeNova])
        return transicoesCandidatas
    
    def computaEstadoAtual(self, palavraAtual, pilhaAtual, transicao, profundidade):
        pilhaNova = deepcopy(pilhaAtual)
        palavraNova = deepcopy(palavraAtual)
        profundidadeNova = deepcopy(profundidade) + 1
        if transicao.simboloLido != '#':
            palavraNova = palavraNova[1:]
        if transicao.simboloDesempilhado != "#":
            pilhaNova.desempilha()
        if transicao.simboloEmpilhado != "#":
            pilhaNova.empilha(transicao.simboloEmpilhado)
        return palavraNova, pilhaNova, profundidadeNova

    #Exibe na tela a lista dos possíveis estados.
    def exibePossiveisEstados(self, possiveisEstados):
        print('Proximos possíveis estados:')
        for estado in possiveisEstados:
            print('[{}, {}, {}]'.format(estado[0], estado[1], estado[2].getPilha()))
    
    def exibeConfiguracaoAtual(self, estadoAtual, palavra, pilha, profundidade):
        print('\nConfiguração atual:')
        print('Estado atual: {}\nPalavra atual: {}\nPilha atual: {}\nProfundidade: {}\n'.format(estadoAtual, palavra, list(reversed(pilha.getPilha())), profundidade))
    
    #Execução do reconhecimento da palavra no AP
    def reconhecimento(self, palavra):
        possiveisEstados = []
        profundidade = 0
        #Obtendo as informações da primeira transição. (Q0 -> Q1)
        estadoInicial = self.Q0.getEstados()
        #Empilha o símbolo do estado inicial.
        simboloEmpilhado = estadoInicial[2]
        pilhaAtual = Pilha()
        self.exibeConfiguracaoAtual(self.Q0.nome, palavra, pilhaAtual, profundidade)
        pilhaAtual.empilha(simboloEmpilhado)
        profundidade+=1
        #Estado atual, palavra, pilha
        possiveisEstados.append([self.Q1.nome, palavra, pilhaAtual, profundidade])
        while len(possiveisEstados) != 0:
            configuracaoAtual = possiveisEstados.pop()
            self.exibeConfiguracaoAtual(configuracaoAtual[0], configuracaoAtual[1], configuracaoAtual[2], configuracaoAtual[3])
            estadoAtual = self.Q1.nome
            palavraAtual = configuracaoAtual[1]
            pilhaAtual = configuracaoAtual[2]
            profundidade = configuracaoAtual[3]
            
            if len(palavraAtual) == 0 and pilhaAtual.pilhaVazia():
                print('ACEITA A PALAVRA!')
                return True
            
            if profundidade > (20*len(palavra)):
                continue
            #Gera as transições possíveis a partir daquele estado.
            possiveisTransicoes = self.possiveisTransicoes(estadoAtual, palavraAtual, pilhaAtual, profundidade)
            #print(possiveisTransicoes)
            #Se eu consigo gerar mais transicoes a partir daquele estado.
            if len(possiveisTransicoes) != 0:
                for transicaoPossivel in possiveisTransicoes:
                    possiveisEstados.append(transicaoPossivel)
            self.exibePossiveisEstados(possiveisEstados)
        print('REJEITA A PALAVRA!')
        return False
        


palavra = readInputOneLine('palavra.txt')

ap = AP()
ap.criaTransicoes()
ap.reconhecimento(palavra)