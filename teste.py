def calcularPremio(P, D, B):
    # Calcula os pontos totais
    pontoTotal = (P * 1) + (D * 2) + (B * 3)
    
    # Define o prêmio baseado no total de pontos
    if pontoTotal >= 150:
        return 'B'
    elif 120 <= pontoTotal < 150:
        return 'D'
    elif 100 <= pontoTotal < 120:
        return 'P'
    else:
        return 'N'

def imprimirPremios(colaboradores):
    # Para cada colaborador, imprime o prêmio calculado
    for i, premio in enumerate(colaboradores): #para i < premio 
        print(f"Colaborador {i+1}: {premio}")

# Quantidade de colaboradores
N = int(input('Quantos colaboradores: '))

# Lista para armazenar os prêmios
colaboradores = []

# Coletar dados e calcular prêmio para cada colaborador
for i in range(N): #para i < 1 até N
    print(f"\nColaborador {i+1}:")
    P = int(input("Pães vendidos: "))
    D = int(input("Doces vendidos: "))
    B = int(input("Bolos vendidos: "))
    
    # Calcula e armazena o prêmio do colaborador
    premio = calcularPremio(P, D, B)
    colaboradores.append(premio)

# Imprimir os prêmios de todos os colaboradores
imprimirPremios(colaboradores)