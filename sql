sistemas gerenciadores de banco de dados:


softwares responsaveis por 
manter os dados integros, prover acesso a quem tem direito, permitir rotinas de copia de segurança e restauraçao, prover
mecanismo de replicaçao/clusterizaçao, otimizar consultar atraves da indexacao, controlar concorrencia, permitir atualizacao

SISTEMAS IMPRECENDIVEIS


DADOS NAO ESTRUTURADOS: 
documentos
emails
videos
redes sociais

DADOS SEMI ESTRUTURADOS: 
existe uma estrutura previa 
flexivel

DADOS ESTRUTURADOS:
estrutura predefinida

select---comando
*---colunas
from---comando
tabela---tabelas

WHERE
usar o where para filtar, por exemplo select clinte, sexo, status from clientes where status = silver OR platinum ou usar o IN ao inves de '=' e nao colocar o 'or'
traduçao: SELECIONE CLIENTE, SEXO, STATUS DE 'CLIENTES' QUANDO STATUS FOR OU SILVER OU PLATINUM 
------------------------------------------------------------------------------------------------------------------------------
LIKE
operador 'like' para saber determinado caracter em um nome por exemplo... 'select cliente, sexo, status from clientes where cliente like '%Alb%'
usar o sinal de porcentagem para definir se quer saber o alb no comeco ou no final, ou tambem nos dois
traduçao: SELECIONE CLIENTE, SEXO, STATUS DE 'CLIENTES' QUANDO CLIENTE CONTER(LIKE) '%Alb%' EM SEU NOME(estou dando exemplo)
------------------------------------------------------------------------------------------------------------------------------------
COMPARAÇÃO
operador de comparacao: select * from vendas where total > 6000
-----------------------------------------------------------------------------------------------------------------------------------------
ORDENAR
operador para ordenar: select cliente from clientes order by cliente // select cliente from clientes order by cliente DESC //
slect cliente from clientes order by cliente desc, status
DESC = ordenar na forma decrescente
-----------------------------------------------------------------------------------------------------------------------------------
BETWEEN
operador para trazer algum resultado com um intervalo, por exemplo: select * from vendas where total between 6000 and 8000
between = entre...
----------------------------------------------------------------------------------------------------------------------------------
TOP = LIMIT
operador top que no caso se usa o limit. exemplo: select * from VENDAS limit 10
-----------------------------------------------------------------------------------------------------------------------------------
DISTINCT
operador distinct: select distinct status from clientes
-----------------------------------------------------------------------------------------------------------------------------------------
AGREGAR
operador agregaçao que se usa para contar certos dados.
exemplos
select count(*) from vendas / usado para contar um total de vendas, mas tambem se tem o
MIN() pegar menor valor, MAX() maior valor, AVG() media dos valores e SUM() a soma de tudo
----------------------------------------------------------------------------------------------------------------------------------
AGREGAÇÃO COM WHERE
usar o where para filtrar, como por exemplo: select count(*)
 from vendas where total > 6000
 ------------------------------------------------------------------------------------------------------------------------------------
 AGRUPAR
agrupar informações como por exemplo select idvendedor, count(idvendedor) from vendas group by idvendedor
-----------------------------------------------------------------------------------------------------------------------------------
HAVING
é uma condição do oprador de agregaçao, exemplo: select id vendedor, count(idvendedor) from vendas group by idvendedor
                                                 having count(idvendedor) > 40
-----------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------

tipos de junções
INNER JOIN // LEFT JOIN // RIGHT JOIN // FULL JOIN
tem equi-  // só chave  // só a chave // trazer to
valencia   // primária  // estrangeir // dos registros                                            

INNER JOIN: select count(*) from vendas inner join vendedores on(vendas.idvendedor = vendedores.idvendedor)











