def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}metros quadrados. ')


#Programa principal
print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
área(l, c)
