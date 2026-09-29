# Controle de Gastos Pessoais — V2.0

Projeto desenvolvido em Python com o objetivo de praticar conceitos fundamentais de programação através da criação de uma aplicação simples para registro e análise de gastos pessoais.

A V2 representa uma evolução da primeira versão, adicionando validações de entrada e novas funcionalidades para análise dos dados registrados.

## Funcionalidades da V2

* Cadastro de múltiplos gastos;
* Validação de categoria;
* Validação de descrição;
* Validação de valores numéricos;
* Impedimento de valores menores ou iguais a zero;
* Cálculo do total de gastos;
* Identificação do menor gasto;
* Identificação do maior gasto;
* Cálculo da média dos gastos;
* Cálculo do total gasto por categoria;
* Definição de orçamento mensal;
* Cálculo do saldo restante;
* Identificação de orçamento excedido;
* Tratamento para situações em que nenhum registro é realizado.

## Conceitos praticados

Durante o desenvolvimento da V2, foram utilizados e reforçados conceitos como:

* Variáveis;
* Listas;
* Tuplas;
* Dicionários;
* Estruturas `if/elif/else`;
* Estruturas `for` e `while`;
* `try/except` para tratamento de erros;
* Validação de entradas;
* Manipulação e análise de dados;
* Operações matemáticas;
* Organização do fluxo de execução.

## Como funciona

O usuário pode iniciar o cadastro de gastos e informar:

1. Categoria;
2. Valor;
3. Descrição.

Os dados são armazenados durante a execução do programa e posteriormente utilizados para gerar análises.

O sistema apresenta informações como:

* Total gasto;
* Maior gasto;
* Menor gasto;
* Média dos gastos;
* Total por categoria;
* Situação em relação ao orçamento mensal.

Caso nenhum registro seja realizado, o programa identifica essa situação e não executa as análises.

## Exemplo de funcionamento

```text
Gostaria de iniciar seus registros? (s/n): s

Categoria: Alimentação
Qual foi o valor: 45.90
Descrição: Almoço

Gostaria de adicionar um novo registro? (s/n): s

Categoria: Transporte
Qual foi o valor: 20
Descrição: Uber

Gostaria de adicionar um novo registro? (s/n): n

Gastos totais: 65.90

Qual seu orçamento mensal?: 500

Saldo restante: 434.10
Valor minimo é: 20.0
Valor maior é: 45.9
Media de gastos 32.95
Total por gastos: {
    'Alimentação': 45.9,
    'Transporte': 20.0
}
```

## V1 → V2

A evolução desta versão foi baseada principalmente em **validação e análise dos dados**.

**V1**

* Registro básico de gastos;
* Cálculo do total;
* Maior e menor gasto.

**V2**

* Validação das entradas;
* Média dos gastos;
* Total por categoria;
* Orçamento mensal;
* Saldo restante;
* Tratamento de diferentes situações de entrada.

## Próxima versão — V3.0

A próxima etapa será trabalhar com **persistência dos dados utilizando arquivos CSV**.

Atualmente, os registros ficam armazenados apenas durante a execução do programa. Na V3, o objetivo será permitir que os dados sejam mantidos e reutilizados posteriormente.

Entre as funcionalidades planejadas estão:

* Salvar os gastos em CSV;
* Carregar registros existentes ao iniciar o programa;
* Adicionar novos registros aos dados já salvos;
* Editar registros;
* Excluir registros;
* Consultar registros armazenados;
* Continuar utilizando as análises desenvolvidas na V2.

Com essa evolução, o projeto passará de uma aplicação que trabalha apenas com dados temporários para uma aplicação capaz de **armazenar e gerenciar dados ao longo do tempo**.

## Objetivo do projeto

Este projeto faz parte da minha jornada de aprendizado em Python e tem como objetivo transformar conceitos estudados em aplicações práticas.

A proposta é evoluir o projeto progressivamente, utilizando cada nova versão para aplicar novos conhecimentos e aumentar a complexidade da aplicação.

**V1 → Registro**
**V2 → Validação e análise**
**V3 → Persistência e gerenciamento dos dados**
