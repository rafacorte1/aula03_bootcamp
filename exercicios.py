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

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

valor = transacao['valor']
print(valor)
hora = transacao['hora']
print(hora)

if valor >= 10000 and hora >= 18:
    print('Transação suspeita')
else:
    pass
# %%

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    if i % 2 == 0:
        print(i)
    else:
        pass
# %%
### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {'id': 1, 'categoria': 'Eletrônicos', 'produto': 'Notebook', 'valor': 2500.00},
    {'id': 2, 'categoria': 'Roupas', 'produto': 'Camiseta', 'valor': 45.00},
    {'id': 3, 'categoria': 'Eletrônicos', 'produto': 'Mouse', 'valor': 85.00},
    {'id': 4, 'categoria': 'Alimentos', 'produto': 'Arroz', 'valor': 25.00},
    {'id': 5, 'categoria': 'Roupas', 'produto': 'Calça', 'valor': 120.00},
    {'id': 6, 'categoria': 'Eletrônicos', 'produto': 'Teclado', 'valor': 250.00},
    {'id': 7, 'categoria': 'Alimentos', 'produto': 'Feijão', 'valor': 18.00},
    {'id': 8, 'categoria': 'Roupas', 'produto': 'Jaqueta', 'valor': 280.00},
    {'id': 9, 'categoria': 'Eletrônicos', 'produto': 'Monitor', 'valor': 800.00},
    {'id': 10, 'categoria': 'Alimentos', 'produto': 'Leite', 'valor': 8.50},
    {'id': 11, 'categoria': 'Roupas', 'produto': 'Sapato', 'valor': 150.00},
    {'id': 12, 'categoria': 'Eletrônicos', 'produto': 'Webcam', 'valor': 320.00},
]

total_eletronicos = 0
total_roupa = 0
total_alimento = 0

for i in vendas:
    # print(i['id'], i['categoria'], i['valor'])
    if i['categoria'] == 'Eletrônicos':
        total_eletronicos += i['valor']
        print(total_eletronicos)
    elif i['categoria'] == 'Roupas':
        total_roupa += i['valor']
        print(total_roupa)
    else:
        total_alimento += i['valor']
        print(total_alimento)

print(f'O total de vendas de eletronicos foi de {total_eletronicos}, de roupas foi de {total_roupa} e de alimentos foi de {total_alimento}')
# %%
### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

palavras = []
entrada = ''

while entrada != 'sair':
    entrada = input('Digite uma palavra para continuar ou sair para sair: ')
# %%
### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
numero = int(input('Digite um numero: '))

while numero > 0 and numero < 10:
    numero = int(input('Digite um numero: '))
# %%
