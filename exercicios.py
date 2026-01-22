# %%
### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = [1, 2, 3]
precos = [1, 2, - 3]

for i in quantidade:
    if i >= 0:
        print('Dados válidos')
    else:
        print('Dados inválidos')
        
for i in precos:
    if i >= 0:
        print('Dados válidos')
    else:
        print('Dados inválidos')
