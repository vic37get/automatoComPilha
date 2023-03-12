
def readInput(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

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

def mainInputReady(filename):
    cleanInput = inputHandling(readInput(filename))
    inputDictionary = makeDictionary(cleanInput)
    if inputDictionary:
        return inputDictionary
    else:
        print('Entrada inválida!')
        return False