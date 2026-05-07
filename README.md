Autor: Lucas Giovanni Ramos Chambi

Exercícios Pt1 (Adaptados da lista cedida pelo Prof. Ricardo Satoshi) – Fazer em Python
1. Criar e coletar um vetor [50] inteiro. Calcular e exibir:
a. A média dos valores entre 10 e 200;
b. A soma dos números ímpares.
2. Criar e coletar um vetor [100] inteiro e exibir:
a. O maior e o menor valor;
b. A média dos valores.
4. Criar e coletar em um vetor [30] real e calcular e exibir:
a. A média do grupo;
b. A quantidade de notas acima do grupo;
c. As posições dos valores abaixo da média do grupo.

Exercícios Pt2 - Fazer em Python
1. Fazer um Python um processo que tenha uma função que retorne o nome do SO. A mesma
aplicação deve ter um procedimento que chame a saída da função de nome de SO e,
dependendo do SO (Linux ou Windows) faça a leitura da saída da função PING (parte dela muda
dependendo do SO) e exiba apenas a média de PING que é exibido na última linha do processo.
(No Windows a saída deve ser Mdia = XXX ms e no Linux a saída deve ser avg separardo por /).
Usar o split para que a saída seja o valor e milissegundos.
* Processo de chamada de PING com 10 iterações, em IPv4 para www.google.com.br
Windows: ping -4 -n 10 www.google.com.br
Linux: ping -4 -c 10 www.google.com.br

2. Fazer em Python uma aplicação que liste os processos ativos, permita ao usuário entrar com o
nome ou o PID do processo e o mate.
A aplicação deverá funcionar, minimamente em Windows e Linux.
É notório que cada SO tem comandos diferentes para as ações supracitadas, portanto:
A main deve possibilitar o usuário a entrar com 4 valores (1 – para listar os processos, 2 – para
matar por PID, 3 – para matar por nome e 9 – para encerrar a aplicação)

1) deve haver uma função chamada os, que identifica e retorna o nome do Sistema Operacional
2) Deve haver um procedimento que permita chamar processos filhos e executá-los, de acordo
com o SO.
Depois de escolher a opção, se for a opção 1, já deve-se exibir os processos ativos, senão, se for
a opção 2, na main deve-se pedir o PID do processo a se matar e passar como parâmetro para a
função que chama processo filho, senão, se for a opção 3, na main deve-se pedir o nome do
processo a se matar e passar como parâmetro para a função que chama processo filho.

Dicas:
1) Chamada de processo para listagem da tabela de processos:
Windows: TASKLIST /FO TABLE
Linux: ps -ef
2) Chamada de processo que mata processo por PID:
Windows: TASKKILL /PID pid_do_processo
Linux: kill -9 pid_do_processo
3) Chamada de processo que mata processo por Nome:
Windows: TASKKILL /IM nome_do_processo
Linux: pkill -f nome_do_processo
