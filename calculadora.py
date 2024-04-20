operacao = 1
while operacao != 0:
    try:
        operacao = int(input('''Qual tipo de operação deseja fazer:
                        1 . Soma
                        2 . Subtração
                        3 . Multiplicação
                        4 . Divisão
                        0 . Sair\n'''))
        if operacao == 0:
            print('Obrigado por ter utilizado nossa calculadora!!!')
        else:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            def calculadora(num1, num2, operacao):
                if operacao == 1:
                    return num1 + num2
                elif operacao == 2:
                    return num1 - num2
                elif operacao == 3:
                    return num1 * num2
                elif operacao == 4:
                    if num1 == 0 or num2 == 0:
                        return "operação invalida"
                    else:
                        return num1 / num2
                        
                else:
                    return "operação invalida"
                
            resultado = calculadora(num1, num2, operacao)
            print("O resultado da operação selecionada é: ", resultado)
    except:
        print("O valor digitado não foi um número")
    