# CATEGORIA DE HABILITAÇÃO DE ACORDO COM VEÍCULO

import os
os.system('cls')

quantidade_rodas = int(input('Digite quantas rodas possui o veículo: '))
quantidade_assentos = int(input('Digite quantos assentos possui o veículo: '))
peso_bruto = float(input('Digite o peso do veículo em Kg: '))
print('-='*30)

if quantidade_rodas < 4:
    print(f'Veículo com {quantidade_rodas} rodas | \033[032m categoria [ A ]\033[m\n')

elif quantidade_rodas == 4 and quantidade_assentos <= 8 and peso_bruto <= 3500:
    print(f'Veículo com {quantidade_rodas} rodas, {quantidade_assentos} assentos e {peso_bruto:.0f} Kg |'
          f'\033[032m categoria [ B ]\033[m\n')
    
elif quantidade_rodas >= 4 and quantidade_assentos <= 8 and 3500 < peso_bruto < 6000:
    print(f'Veículo com {quantidade_rodas} rodas, {quantidade_assentos} assentos e {peso_bruto:.0f} Kg |'
          f'\033[032m categoria [ C ]\033[m\n')
    
elif quantidade_rodas >= 4 and quantidade_assentos > 8 and peso_bruto < 6000:
    print(f'Veículo com {quantidade_rodas} rodas, {quantidade_assentos} assentos e {peso_bruto:.0f} Kg |'
          f'\033[032m categoria [ D ]\033[m\n')

else:
    print(f'Veículo com {quantidade_rodas} rodas, {quantidade_assentos} assentos e {peso_bruto:.0f} Kg |'
        f'\033[032m categoria [ E ]\033[m\n')