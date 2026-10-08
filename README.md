# Sprint 5 - Sistema de Análise de Dados

## Descrição

Este projeto foi desenvolvido em Python para realizar a leitura e análise de dados armazenados em um arquivo CSV.

O programa verifica e valida informações como e-mail, CPF, telefone e data.

Foram utilizados conceitos de:

- Manipulação de arquivos
- Expressões regulares
- Tratamento de exceções
- Exceção personalizada
- Listas
- Estruturas de repetição
- f-strings

## Arquivos

O projeto possui os seguintes arquivos:

- `dados.csv` - arquivo com os dados que serão analisados.
- `analise_dados.py` - programa principal.
- `README.md` - documentação do projeto.

## Validações

### E-mail

Foi utilizada uma expressão regular para verificar se o e-mail possui um formato básico válido.

Exemplo:



maria@gmail.com


### CPF

O programa aceita CPF no formato:



123.456.789-00


A expressão regular utilizada verifica os números, pontos e hífen.

### Telefone

O telefone deve seguir o formato:



(11) 99999-8888


### Data

A data deve seguir o formato:



15/05/2000


Também é verificado se o dia está entre 1 e 31 e se o mês está entre 1 e 12.

## Expressões regulares

O programa utiliza o módulo `re`.

Foram utilizados alguns metacaracteres:

- `\d` para representar números.
- `\w` para letras, números e alguns caracteres.
- `^` para indicar o início do texto.
- `$` para indicar o final do texto.
- `.` para representar caracteres específicos dentro dos padrões.

## Tratamento de exceções

O programa possui tratamento para alguns erros.

### FileNotFoundError

É utilizado quando o arquivo `dados.csv` não é encontrado.

### KeyError

É utilizado quando alguma coluna necessária não existe no arquivo CSV.

### ValueError

É utilizado para tratar valores que não podem ser convertidos corretamente.

### FormatoInvalidoError

Foi criada uma exceção personalizada para indicar quando um dado não está no formato esperado.

## Exemplo de entrada

O arquivo `dados.csv` possui dados como:



email,cpf,telefone,data maria@gmail.com,123.456.789-00,(11) 99999-8888,15/05/2000 joao@gmail.com,987.654.321-00,(21) 98888-7777,20/10/1999


## Exemplo de saída



============================== RELATÓRIO FINAL ==============================

Total de registros: 5 Registros válidos: 4 Registros inválidos: 1

REGISTROS VÁLIDOS:

E-mail: maria@gmail.com | CPF: 123.456.789-00 | Telefone: (11) 99999-8888 | Data: 15/05/2000


## Como executar

Primeiro, coloque os três arquivos na mesma pasta.

Depois, execute:



python analise_dados.py


O programa irá ler o arquivo `dados.csv`, verificar os dados e mostrar o relatório final.


:::

Estrutura final para o GitHub
Sprint_5
│
├── dados.csv
├── analise_dados.py
└── README.md


Essa versão atende aos pontos principais do enunciado: CSV, with/open ou manipulação de arquivo, regex com re, try/except/else/finally, FileNotFoundError, ValueError, KeyError, exceção personalizada, f-strings e README.

Só faria uma pequena correção antes da entrega: no código acima usei open() com finally, porque o enunciado pede explicitamente with open(...). Para ficar 100% alinhado ao que foi solicitado, posso montar uma versão ainda simples usando with open() e mantendo o nível de 1º período.
