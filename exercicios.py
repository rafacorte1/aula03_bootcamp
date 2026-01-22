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
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperaturas = [0, 20, 40]

for i in temperaturas:
    if i <= 19:
        print('Temperatura baixa')
    elif i <= 39:
        print("Temperatura normal")
    else:
        print('Temperatura alta')
   

# %%
### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

valor = []

for i in log.values():
    valor.append(i)

print(valor[2])

# if log['level'] == 'ERROR':
#     print(log['message'])

# %%
### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

email_valido = False
idade_valida = False

try:
    email = input('Insira seu email: ')
    if any(email.isdigit() for i in email):
        raise ValueError('O email deve conter apenas letras')
    else:
        print('Email válido', email)
        email_valido = True
except ValueError as e:
    print(e)

try:
    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade < 18 or idade > 65:
        print('Por favor, digite uma idade válida')
    else:
        print('Idade válida', idade)
        idade_valida = True
except ValueError:
    print('A idade só pode ter números')
    
if email_valido and idade_valida:
    print('Dados de usuário válidos')
else:
    print('Cadastro incompleto')


    

# %%
