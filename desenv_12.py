# Nome e idade do usuário

from datetime import date

current = date.today().year
while True:
    name = input('\nDigite seu nome: ').title().strip()
    year = input('Digite o ano de seu nascimento: ')

    if len(name) == 0:
        print('Digite um nome válido\n')
        continue
    try:
        int(year)
    except (ValueError):
        print('Digite somente números\n')
        continue
    break

print(f'\nOlá {name}, nesse ano de {current} você completou/completará {current - int(year)} anos.')


 




