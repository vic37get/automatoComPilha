<h1 align="center"> 💻✅❓ Automato Pilha: Conversão de GLC em AP e reconhecimento de palavras </h1>

## ℹ️ Sobre

Implementação em python da conversão de uma GLC (Gramática Livre de Contexto) não recursiva a esquerda em AP (Automato Pilha) e reconhecimento de palavras para a disciplina de Teoria da Computação.

## ⌨️ Entrada

A entrada do programa consiste em dois arquivos: `input.txt` e `palavra.txt`.

1. O arquivo **`input.txt`** deve conter uma GLC (Gramática Livre de Contexto) **sem recursão a esquerda**, veja um exemplo:

   ```
   S - aSb | #
   ```

   > A gramática acima é correspondente a linguagem _L = {**a<sup>n</sup>b<sup>n</sup>**, n>=0 }_.

2. O arquivo **`palavra.txt`** deve conter a palavra que deve ser reconhecida no AP, vejamos um exemplo de palavra **aceita** e palavra **rejeitada** para a GLC mostrada acima:

   | Aceita | Rejeitada |
   | ------ | --------- |
   | `aabb` | `aaabb`   |

## 🖥️ Saída

A saída do programa deve aparecer **no terminal**, e deve mostrar o **processo de reconhecimento da palavra no AP (Automato Pilha), retornando ao final se a palavra foi rejeitada ou aceita**.

**Exemplos:**

Saída para as entradas `ab` e `aab` usando o GLC que foi mostrado anteriormente:

> Para `ab` (palavra aceita):

```
Configuração atual:
Estado atual: Q0
Palavra atual: ab
Pilha atual: []
Profundidade: 0


Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['S']
Profundidade: 1

Proximos possíveis estados:
[Q1, ab, ['b', 'S', 'a']]
[Q1, ab, []]

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: []
Profundidade: 2

Proximos possíveis estados:
[Q1, ab, ['b', 'S', 'a']]

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['a', 'S', 'b']
Profundidade: 2

Proximos possíveis estados:
[Q1, b, ['b', 'S']]

Configuração atual:
Estado atual: Q1
Palavra atual: b
Pilha atual: ['S', 'b']
Profundidade: 3

Proximos possíveis estados:
[Q1, b, ['b', 'b', 'S', 'a']]
[Q1, b, ['b']]

Configuração atual:
Estado atual: Q1
Palavra atual: b
Pilha atual: ['b']
Profundidade: 4

Proximos possíveis estados:
[Q1, b, ['b', 'b', 'S', 'a']]
[Q1, , []]

Configuração atual:
Estado atual: Q1
Palavra atual:
Pilha atual: []
Profundidade: 5

ACEITA A PALAVRA!
```

> Para `aab` (palavra rejeitada):

```
Configuração atual:
Estado atual: Q0
Palavra atual: aab
Pilha atual: []
Profundidade: 0


Configuração atual:
Estado atual: Q1
Palavra atual: aab
Pilha atual: ['S']
Profundidade: 1

Proximos possíveis estados:
[Q1, aab, ['b', 'S', 'a']]
[Q1, aab, []]

Configuração atual:
Estado atual: Q1
Palavra atual: aab
Pilha atual: []
Profundidade: 2

Proximos possíveis estados:
[Q1, aab, ['b', 'S', 'a']]

Configuração atual:
Estado atual: Q1
Palavra atual: aab
Pilha atual: ['a', 'S', 'b']
Profundidade: 2

Proximos possíveis estados:
[Q1, ab, ['b', 'S']]

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['S', 'b']
Profundidade: 3

Proximos possíveis estados:
[Q1, ab, ['b', 'b', 'S', 'a']]
[Q1, ab, ['b']]

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['b']
Profundidade: 4

Proximos possíveis estados:
[Q1, ab, ['b', 'b', 'S', 'a']]

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['a', 'S', 'b', 'b']
Profundidade: 4

Proximos possíveis estados:
[Q1, b, ['b', 'b', 'S']]

Configuração atual:
Estado atual: Q1
Palavra atual: b
Pilha atual: ['S', 'b', 'b']
Pilha atual: ['a', 'S', 'b', 'b', 'b']
Profundidade: 6

Proximos possíveis estados:
REJEITA A PALAVRA!
```

## ▶️ Como executar

1. Baixe o projeto;
2. Verifique os arquivos de entrada: `input.txt` (GLC) e `palavra.txt` (palavra a ser reconhecida);
3. Execute o arquivo `ap.py` e veja a saída no terminal.

## 📜 Alunos

| [<img src="https://avatars.githubusercontent.com/u/51518489?v=4" width=115><br><sub>Camila Fernanda Alves</sub>](https://github.com/vic37get) | [<img src="https://avatars.githubusercontent.com/u/57508736?v=4" width=115><br><sub>Jhoisnáyra Vitória</sub>](https://github.com/jhoisz) |
| :-------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
