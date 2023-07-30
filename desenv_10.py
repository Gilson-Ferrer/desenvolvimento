#calculadora

def calculator (op=str, num1 =0, num2 =0):
    
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    return 'Parâmetro desconhecido'


nro_1 = float(input('Digite o primeiro numero: '))
ope = input('Digite a operação: | + | - | * | / | ')
nro_2 = float(input('Digite o primeiro numero: '))

print(f'{calculator(ope, nro_1, nro_2):.2f}')


