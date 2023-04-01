def readInputOneLine(filename):
    data = open(filename, 'r')
    data = data.readline()
    return data

def readInput(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

def escreveSaida(dados, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(dados)

def inputHandling(data):
    for line in range(len(data)):
        data[line] = data[line].strip().replace(' ', '')
    return data

def makeDictionary(cleanData):
    dictionary = {}
    for line in range(len(cleanData)):
        breakData = cleanData[line].split('-')
        rule = breakData[0]
        if rule.isupper():
            rest = breakData[1].split('|')
            dictionary[rule] = rest
        else:
            return False
    return dictionary

def exibeAP(Q0, Q1, QF):
    dadosAp = ''
    dadosAp += 'Estado (q0)\n'
    dadosAp +='Transições: \n'
    dadosAp += Q0.exibeEstado()+'\n'
    dadosAp += 'Estado (q1)\n'
    dadosAp +='Transições: \n'
    dadosAp += Q1.exibeEstado()+'\n'
    dadosAp += 'Estado (qf)\n'
    dadosAp +='Estado Final!\n'
    dadosAp += QF.exibeEstado()
    return dadosAp

def mainInputReady():
    cleanInput = inputHandling(readInput('entradas/input.txt'))
    inputDictionary = makeDictionary(cleanInput)
    if inputDictionary:
        return inputDictionary
    else:
        print('Entrada inválida!')
        return False