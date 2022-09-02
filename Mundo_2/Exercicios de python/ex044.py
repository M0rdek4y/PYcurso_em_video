prod = float(input('Digite o valor do seu produto: '))
pag = str(input('Diga o seu metodo de pagamento:\nDINHEIRO/CHEQUE(1)\nCARTÃO(2)\n'))

if pag.upper() == 'DINHEIRO' or pag == '1':
    print('Seu metodo de pagamento será em DINHEIRO ou CHEQUE!\nVALOR DO PRODUTO: R${:.2f}\nPARCELAMENTO: NÃO\nJUROS: 0%\nDESCONTO: 10%\nTOTAL: R${:.2f}.'.format(prod, prod - (prod * 10) / 100))
else:
    desc = str(input('Seu metodo de pagamento é CARTÃO! Deseja parcelar?\nSIM(1)\nNÃO(2)\n'))
    if desc.upper() == 'SIM' or desc == '1':
        parc = str(input('Deseja parcelar em quantas vezes?\n2x no CARTÃO sem juros(1)\n3x ou MAIS no CARTÃO com 20% de juros(2)\n'))
        if parc == '1':
            print('Seu metodo de pagamento será em CARTÃO!\nVALOR DO PRODUTO: R${:.2f}\nPARCELAMENTO: SIM\nQUANTIDADE DE PARCELAS: 2 VEZES\nJUROS: 0%\nDESCONTO: 0%\nTOTAL: R${:.2f}.'.format(prod,
                                                                                                                                                                                             prod))
        else:
            total = (prod + (prod * 20) / 100)
            qparc = int(input('Em quantas parcelas deseja pagar? \n'))
            vlparc = (total / qparc)
            print('Seu metodo de pagamento será em CARTÃO!\nVALOR DO PRODUTO: R${:.2f}\nPARCELAMENTO: SIM\nQUANTIDADE DE PARCELAS: {} VEZES de {}\nJUROS: 20%\nDESCONTO: 0%\nTOTAL: R${:.2f}.'.format(
                prod, qparc, vlparc, total))
    else:
        print('Seu metodo de pagamento será em CARTÃO!\nVALOR DO PRODUTO: R${:.2f}\nPARCELAMENTO: NÃO\nJUROS: 0%\nDESCONTO: 5%\nTOTAL: R${:.2f}.'.format(prod, prod - (prod * 5) / 100))
