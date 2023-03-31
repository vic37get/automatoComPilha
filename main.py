from ap import AP
from readInput import readInputOneLine, escreveSaida, exibeAP


print('\nAntes de executar, certifique-se de que você já inseriu a GLC desejada no arquivo input.txt e a palavra w a ser reconhecida no arquivo palavra.txt\n')
palavra = readInputOneLine('palavra.txt')

ap = AP()
ap.criaTransicoes()
ap.reconhecimento(palavra)

escreveSaida(ap.transicoesReconhecidas, 'reconhecimento.txt')
escreveSaida(exibeAP(ap.Q0, ap.Q1, ap.QF), 'representacaoAP.txt')

