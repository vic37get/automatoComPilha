<h1 align="center"> 💻✅❓ Automato com Pilha: Conversão de GLC em AP e reconhecimento de palavras </h1>

## ℹ️ Sobre

Implementação em **python** da **conversão de uma GLC** (Gramática Livre de Contexto) não recursiva a esquerda **em AP** (Automato Pilha) e **reconhecimento de palavras**. Desenvolvido para a disciplina de Teoria da Computação de 2022.2, ministrada pelo Carlos André (Ciência da Computação, UFPI).

## ⌨️ Entrada

A entrada do programa consiste em **dois arquivos: `input.txt` e `palavra.txt`**.

1. O arquivo **`input.txt`** deve conter uma GLC (Gramática Livre de Contexto) **sem recursão a esquerda**, veja um exemplo:

   ```
   S - aSb | #
   ```

   > A gramática acima é correspondente a linguagem _L = {**a<sup>n</sup>b<sup>n</sup>**, n>=0 }_.

   > Note que a gramática deve seguir esse padrão, símbolo inicial, hífen (que é o símbolo que representa a geração) e produções. Veja que as produções são separadas pelo caractere |.

2. O arquivo **`palavra.txt`** deve conter a palavra que deve ser reconhecida no AP, vejamos um exemplo de palavra **aceita** e palavra **rejeitada** para a GLC mostrada acima:

   | Aceita | Rejeitada |
   | ------ | --------- |
   | `aabb` | `aaabb`   |

## 🖥️ Saída

A saída do programa consiste em **dois arquivos**:

1. **`reconhecimento.txt`**: contém o processo de reconhecimento da palavra (`palavra.txt`) no AP (Automato Pilha), retornando ao final se a palavra foi rejeitada ou aceita.

2. **`representacaoAP.txt`**: contém a representação do AP (Automato Pilha) para a gramática de entrada (`input.txt`).

**➡️ Exemplo de saída:**

Vejamos um exemplo de saída para as entrada `ab` (palavra aceita) utilizando o GLC que foi mostrado anteriormente:

> Arquivo `representacaoAP.txt`:

```
Estado (q0)
Transições:
(#,#,S)

Estado (q1)
Transições:
(a,a,#)
(b,b,#)
(#,S,aSb)
(#,S,#)
(?,?,#)

Estado (qf)
Estado Final!
```

> Arquivo `reconhecimento.txt`:

```
-------------------

Configuração atual:
Estado atual: Q0
Palavra atual: ab
Pilha atual: []
Profundidade: 0

-------------------

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['S']
Profundidade: 1

Proximo(s) estado(s):
(Q1, ab, ['b', 'S', 'a'])
(Q1, ab, [])

-------------------

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: []
Profundidade: 2

Proximo(s) estado(s):
(Q1, ab, ['b', 'S', 'a'])

-------------------

Configuração atual:
Estado atual: Q1
Palavra atual: ab
Pilha atual: ['a', 'S', 'b']
Profundidade: 2

Proximo(s) estado(s):
(Q1, b, ['b', 'S'])

-------------------

Configuração atual:
Estado atual: Q1
Palavra atual: b
Pilha atual: ['S', 'b']
Profundidade: 3

Proximo(s) estado(s):
(Q1, b, ['b', 'b', 'S', 'a'])
(Q1, b, ['b'])

-------------------

Configuração atual:
Estado atual: Q1
Palavra atual: b
Pilha atual: ['b']
Profundidade: 4

Proximo(s) estado(s):
(Q1, b, ['b', 'b', 'S', 'a'])
(Q1, , [])

-------------------

Configuração atual:
Estado atual: Q1
Palavra atual:
Pilha atual: []
Profundidade: 5

RESULTADO: Palavra Aceita!!

```

## ▶️ Como executar

1. Baixe o projeto;
2. Antes de executar, certifique-se de que você já inseriu a GLC desejada no arquivo `input.txt` e a palavra _w_ a ser reconhecida no arquivo `palavra.txt`;
3. Execute o arquivo `main.py` e veja a saída nos arquivos `reconhecimento.txt` e `representacaoAP.txt`.

## 📜 Alunos

| [<img src="https://avatars.githubusercontent.com/u/51518489?v=4" width=115><br><sub>Camila Fernanda Alves</sub>](https://github.com/vic37get) | [<img src="https://avatars.githubusercontent.com/u/57508736?v=4" width=115><br><sub>Jhoisnáyra Vitória</sub>](https://github.com/jhoisz) |
| :-------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
