# HEAD
import moeda
import dado

# BODY
p = dado.leiadinheiro('\33[36mDigite o preço: R$')
moeda.resumo(p, 35, 22)
