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
    
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []

    for i in range(len(dados_no_estoque)):

        if i == dado_para_remover:

            dados_rolados.append(dados_no_estoque[i])

        else:
            novo_estoque.append(dados_no_estoque[i])
    
    return [dados_rolados, novo_estoque]