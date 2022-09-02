"""
seno é cateto oposto
consceno é cateto adjacente
hipotenusa é
"""

# resolução 1

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Compirmento do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))

# resolução 2

import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('DIgite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
