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

# %%
### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje e nossa terceira aula do bootcamp , bootcamp de python"
palavras = texto.split()
print(palavras)
contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] + 1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)
# %%
