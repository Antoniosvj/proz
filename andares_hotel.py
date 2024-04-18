#Como foi proposto no desafio, fiz os andares passando de forma decrescente

andares = 20
while andares >= 0:
    if andares == 13:
        pass
    elif andares == 0:
        print('Terreo')
    else:
        print(f'{andares}º andar')
    andares-=1