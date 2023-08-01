# # Nome e idade do usuário

from datetime import date

current = date.today().year
while True:
    try:
        name_ = input('\nDigite seu nome: ').title().strip() or 'usuário' 
        year_ = input('Digite o ano de seu nascimento: ')
        if int(year_) < 1922 or int(year_) > current - 1:
            print(f'Por favor {name_}, digite datas entre 1922 e {current -1}')
            continue
    except Exception as error:
        print(error)
        continue
    break

print(f'\nOlá {name_}, nesse ano de {current} você completou/completará {current - int(year_)} anos.')

