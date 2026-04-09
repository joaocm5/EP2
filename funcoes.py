import random
def rolar_dados(numero):
    dados = []
    for i in range(numero):
        valor = random.randint(1, 6)
        dados.append(valor)
    return dados

#exercicio 2
def guardar_dado(dados_rolados, estoque, dado_a_guardar):
    rolados_tirando_guardado = []

    for dado in dados_rolados:
        if dado == dado_a_guardar:
            estoque.append(dado)
        else:
            rolados_tirando_guardado.append(dado)

    return [rolados_tirando_guardado, estoque]
    