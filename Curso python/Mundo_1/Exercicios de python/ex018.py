# resolução 1

import math

angle = int(input('Digite o ângulo que você deseja: '))
rad = math.radians(angle)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO DE {:.2f}\n'
      'o ângulo de {} tem a TANGENTE de {:.2f}\n'. format(angle, sen, angle, cos, angle, tan))

# resolução 2

from math import sin, cos, tan, radians

angle = int(input('Digite o ângulo que você deseja: '))
rad = radians(angle)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO DE {:.2f}\n'
      'o ângulo de {} tem a TANGENTE de {:.2f}\n'. format(angle, sen, angle, cos, angle, tan))
