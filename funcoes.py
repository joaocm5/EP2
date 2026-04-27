import random
def rolar_dados(numero):
    dados = []
    for i in range(numero):
        valor = random.randint(1, 6)
        dados.append(valor)
    return dados

#exercicio 2
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novo_rolados = []
    
    for i in range(len(dados_rolados)):
        if i == dado_para_guardar:
            dados_no_estoque.append(dados_rolados[i])
        else:
            novo_rolados.append(dados_rolados[i])
    
    return [novo_rolados, dados_no_estoque]
#ex 3
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []

    for i in range(len(dados_no_estoque)):

        if i == dado_para_remover:

            dados_rolados.append(dados_no_estoque[i])

        else:
            novo_estoque.append(dados_no_estoque[i])
    
    return [dados_rolados, novo_estoque]
#ex 4
def calcula_pontos_regra_simples(lista):
    dicio = {}
    dicio[1] = 0
    dicio[2] = 0
    dicio[3] =0
    dicio[4] =0
    dicio[5] =0
    dicio[6] =0
    for numero in lista:
        if numero == 1:
            dicio[1] += 1
        elif numero == 2:
            dicio[2] += 2
        elif numero == 3:
            dicio[3] += 3
        elif numero == 4:
            dicio[4] += 4
        elif numero == 5:
            dicio[5] += 5
        elif numero == 6:
            dicio[6] += 6
    return dicio
#ex 5
def calcula_pontos_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma
#ex 6
def calcula_pontos_sequencia_baixa(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    elif 5 in lista and 2 in lista and 3 in lista and 4 in lista:
        return 15
    elif 5 in lista and 6 in lista and 3 in lista and 4 in lista:
        return 15
    else:
        return 0

#ex7
def calcula_pontos_sequencia_alta(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        return 30
    elif 5 in lista and 2 in lista and 3 in lista and 4 in lista and 6 in lista:
        return 30
    else:
        return 0

#ex8
def calcula_pontos_full_house(lista):
    dicio = {}
    soma = 0

    for numero in lista:
        if numero in dicio:
            dicio[numero] += 1
        else:
            dicio[numero] = 1
    
    if len(dicio) != 2:
        return 0

    for quantidades in dicio.values():
        if quantidades == 2 or quantidades == 3:
            
            for dado, quantidade in dicio.items():
                soma += dado*quantidade
        else:
            return 0

    return int(soma/2)
#ex9
def calcula_pontos_quadra(lista):
    soma = 0
    dicio = {}
    tem4 = False

    for numero in lista:
        if numero in dicio:
            dicio[numero] += 1
        else:
            dicio[numero] = 1
        
    for quantidade in dicio.values():
        if quantidade >= 4:
            tem4 = True
    
    if tem4 == False:
        return 0
    else:
        for dado, valor in dicio.items():
            soma += valor*dado
    return soma

#ex10
def calcula_pontos_quina(lista):
    dicio = {}
    tem = False

    for numero in lista:
        if numero in dicio:
            dicio[numero] += 1
        else:
            dicio[numero] = 1
        
    for quantidade in dicio.values():
        if quantidade >= 5:
            tem = True
    
    if tem == False:
        return 0
    else:
        return 50