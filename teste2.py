colaboradores = int(input("Quantos colaboradores? "))
totalpaes = 0
totaldoces = 0
totalbolos = 0



def calcularPontos(totalpaes,totaldoces,totalbolos):
    pontos = totalpaes*1 + totaldoces*2 + totalbolos*3
    if pontos >= 150:
        premio = "bolo"
    elif pontos >=120 and pontos <150:
        premio ="doce"
    elif pontos >= 100 and pontos <120:
        premio = "pão"
    else:
        premio = "um abraço"
        return premio
    print(premio)
    
while 0 < colaboradores:
    colaboradores-=1
    paes = int(input((f"Quantos pães vendeu o {colaboradores+1}º: ")))
    doces = int(input((f"Quantos doces vendeu o {colaboradores+1}º: ")))
    bolos = int(input((f"Quantos bolos vendeu o {colaboradores+1}º: ")))
    totalpaes += paes
    totaldoces += doces
    totalbolos += bolos
    premio = calcularPontos(totalpaes,totaldoces,totalbolos)
print(f"O {colaboradores}º colaborador ganhou: {premio}")

'print((f"No total foram {totalpaes} pães"))'
'print((f"No total foram {totaldoces} doces"))'
'print((f"No total foram {totalbolos} bolos"))'


