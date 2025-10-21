# TP2-Grafo-Coloracao

🧩 Trabalho II – Teoria e Modelo de Grafos (CCF-331)
Universidade Federal de Viçosa – Campus Florestal

Professor: Marcus Henrique Soares Mendes
Data de entrega: 11/11/2025 – até 23h59

📘 Descrição do Projeto

Este projeto tem como objetivo resolver o problema de alocação de horários de disciplinas utilizando o conceito de coloração de grafos.
O problema é modelado da seguinte forma:

Cada vértice representa uma disciplina.

Existe uma aresta entre duas disciplinas se elas não podem ocorrer simultaneamente (ou têm o mesmo professor ou alunos em comum).

O objetivo é minimizar o número de cores, ou seja, usar o menor número possível de horários sem conflitos.

⚙️ Funcionalidades Implementadas

Leitura de um arquivo CSV com os pares de disciplinas em conflito.

Construção do grafo de conflitos.

Utilização da biblioteca GCol (documentação
) para aplicar diferentes algoritmos de coloração.

Exibição dos seguintes resultados:

✅ Número mínimo de cores (horários) utilizadas;

🎨 Cor atribuída a cada disciplina;

⏱️ Tempo de execução aproximado.

🧠 Conceitos Envolvidos

Coloração de grafos;

Minimização de conflitos;

Representação de problemas reais através de teoria dos grafos;

Uso prático da biblioteca GCol.

🧩 Entrada e Saída

Entrada: Arquivo .csv com pares de disciplinas em conflito, no formato:

Disciplina1,Disciplina2
A,B
A,C
B,D
C,D
C,E


Saída:

Quantidade mínima de horários necessários;

Lista de disciplinas com suas cores correspondentes;

Tempo total de execução.
