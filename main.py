from ap import AP
from readInput import readInputOneLine, escreveSaida, exibeAP


print('\nAntes de executar, certifique-se de que você já inseriu a GLC desejada no arquivo input.txt e a palavra w a ser reconhecida no arquivo palavra.txt\n')
palavra = readInputOneLine('entradas/palavra.txt')

ap = AP()
ap.criaTransicoes()
ap.reconhecimento(palavra)

escreveSaida(ap.transicoesReconhecidas, 'saidas/reconhecimento.txt')
escreveSaida(exibeAP(ap.Q0, ap.Q1, ap.QF), 'saidas/representacaoAP.txt')

