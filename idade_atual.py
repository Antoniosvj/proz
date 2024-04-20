'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou,
ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano,
o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''
import datetime

ano_atual = datetime.datetime.now().year
nome = input('Digite seu nome: ')
ano = 0
while ano <1922 or ano > ano_atual:
    try:
        ano = int(input('Digite o ano que você nasceu: '))
        if ano < 1922 or ano > ano_atual:
            print('Ano inválido')
    except:
        print('Informação inválida, digite o ano que você nasceu no período entre 1922 e 2021')

idade = ano_atual - ano

print(f'Olá {nome}, este ano você está completando {idade} anos.')