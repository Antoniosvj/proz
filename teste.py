def calculadora():
    while True:
        print("""
        Essas são as operações disponiveis:
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        0 - Sair
        """)
    
        operacao = int(input("Qual operação deseja fazer: (digite o número)"))
        
        if operacao == 0:
            print("Fechando calculadora...")
            break
        
        num_1 = float(input("Digite o primeiro número: "))
        num_2 = float(input("Digite o segundo número: "))
    
        if operacao == 1:
            resultado = num_1 + num_2
            print(f"Resultado: {resultado}")
        elif operacao == 2:
            resultado = num_1 - num_2
            print(f"Resultado: {resultado}")
        elif operacao == 3:
            resultado = num_1 * num_2
            print(f"Resultado: {resultado}")
        elif operacao == 4:
            if num_1 == 0 or num_2 == 0:
                print("Erro, dividir por 0 é brincadeira")
            resultado = num_1 / num_2
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida")
    

calculadora()