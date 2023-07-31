# # Nome e idade do usuário

from datetime import date

current = date.today().year
while True:
    try:
        name = input('\nDigite seu nome: ').title().strip() 
        year = input('Digite o ano de seu nascimento: ')
        if int(year) < 1922 or int(year) > current - 1:
            print(f'Por favor {name}, digite datas entre 1922 e {current -1}')
            continue
        if len(name) == 0:
            print('Digite o seu nome por favor.')
            continue
    except Exception as error:
        print(error)
        continue
    break

print(f'\nOlá {name}, nesse ano de {current} você completou/completará {current - int(year)} anos.')

