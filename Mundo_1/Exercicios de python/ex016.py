# resolução 1

import math
v = float(input('Digite um valor:'))
vin = math.trunc(v)
print('O valor inteiro de {} é {}'.format(v, vin))

# resolução 2

from math import trunc
v = float(input('Digite um valor:'))
vin = trunc(v)
print('O valor inteiro de {} é {}'.format(v, vin))

# resolução 3

v = float(input('Digite um valor:'))
print('O valor inteiro de {} é {}'.format(v, int(v)))
