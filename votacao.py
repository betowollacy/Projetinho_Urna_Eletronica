
#CANDIDATE LIST PRESIDENT
bolsonaro = 0
lula = 0
nulo = 0
print()#BLANK TO SKIP A LINE

#LOOP 
while True:
    print(f'Votos de Bolsonaro: {bolsonaro}')
    print("*" *21)
    print(f'Votos de Lula: {lula}')
    print("*" *21)
    print(f'Votos Nulo: {nulo}')
    print("*" *21)
    print("*" *21)
    print("1 - BOLSONARO:\n2 - LULA :\n3 e Outros Numeros - VOTOS NULO: \n ")
#INPUT 
    voto = int(input("Escolha quem vai ser o Presidente: "))

 #CONDITION
    if voto == 1:
        bolsonaro += 1

    elif voto == 2:
        lula += 1
    else:
        nulo += 1







