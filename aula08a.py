from math import sqrt
import random
num = float(input('Digite um número: '))
raiz = sqrt(num)
print(f'o numero {num:.0f} tem a raiz quadrada de {raiz:.2f}')



num2 = random.randint(1, 10)

#para randomizar numeros inteiros
# #utilizamos random.randint
print(f'o numero random é {num2}')

import emoji
print(emoji.emojize('O seu emoji é :new_moon: '))