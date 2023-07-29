# Impressão de identificador de andar (exceto 13º)
#=============================================================

# 1ª forma de impresão

counter = 20
while True:
    print(f'{counter}º andar' if counter != 13 else '--- -----')
    counter -= 1
    if not counter:
        break


#=============================================================

# 2ª forma de impresão

for a in range(20, 0, -1):
    print('{}º andar' .format(a) if a != 13 else '--- ------')



#=============================================================

# 3ª forma de impresão

counter_2 = 20
while counter_2 > 0:
    if counter_2 != 13:
        print('%dº andar' %(counter_2))
    counter_2 -= 1