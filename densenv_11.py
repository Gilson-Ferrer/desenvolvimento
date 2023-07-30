def calculator (num0, num1 =0, num2 =0):
    
    if num0 == 1:
        return num1 + num2
    elif num0 == 2:
        return num1 - num2
    elif num0 == 3:
        return num1 * num2
    elif num0 == 4:
        return num1 / num2
    return 'Parâmetro desconhecido'

while True:
    nro_op = int(input('Digite a operação:\n\n1 - Soma\n2 - Subtração\n'
                  '3 - Multiplicação\n4 - Divisão\n0 - Sair\n-->'))
    
    if  nro_op > 4 or nro_op < 0:
        print('\n\033[31mOpção inexitente\033[m\n')
        ...
    if nro_op == 0:
        break
    if 0 < nro_op < 5:
        while True:
            nro_1 = float(input('\nDigite o primeiro numero: '))
            nro_2 = float(input('Digite o primeiro numero: '))
            if nro_op == 4 and nro_1 == 0 or nro_2 == 0:
                print('\nDigite somente números \033[32mNÃO NULOS\033[m\n')
                continue
            print('-' *30)
            print(f'Resultdo : {calculator(nro_op, nro_1, nro_2)}')
            print('-' *30)
            break

print('\nFim do programa')