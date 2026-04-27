from funcoes import *

cartela = {
    'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
 
imprime_cartela(cartela)

for i in range(12):
    guardados = []
    rolados = rolar_dados(5)
    rerolado = 0

    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    while True:
        jogada = input()

        if jogada == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(rolados, guardados, indice)
            rolados = resultado[0]
            guardados = resultado[1]
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif jogada == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(rolados, guardados, indice)
            rolados = resultado[0]
            guardados = resultado[1]
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif jogada == '3':
            if rerolado == 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rolados = rolar_dados(len(rolados))
                rerolado += 1
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif jogada == '4':
            imprime_cartela(cartela)
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif jogada == '0':
            print("Digite a combinação desejada:")
            while True:
                combinacao = input()
                if combinacao in ['1', '2', '3', '4', '5', '6']:
                    chave = int(combinacao)
                    if cartela['regra_simples'][chave] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(rolados + guardados, combinacao, cartela)
                        break
                elif combinacao in cartela['regra_avancada']:
                    if cartela['regra_avancada'][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(rolados + guardados, combinacao, cartela)
                        break
                else:
                    print("Combinação inválida. Tente novamente.")
            
            break

        else:
            print("Opção inválida. Tente novamente.")

soma_simples = 0
for valor in cartela['regra_simples']:
    if cartela['regra_simples'][valor] != -1:
        soma_simples += cartela['regra_simples'][valor]

if soma_simples >= 63:
    soma_simples += 35

total = soma_simples
for valor in cartela['regra_avancada']:
    if cartela['regra_avancada'][valor] != -1:
        total += cartela['regra_avancada'][valor]

imprime_cartela(cartela)
print(f"Pontuação total: {total}")
