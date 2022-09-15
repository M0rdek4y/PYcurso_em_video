v = float(input('Digite a velocidade do veiculo: '))
if v > 80:
    print('Você foi multado por execesso de velocidade!\nVocê foi flagrado a {:.1f}Km/h!\nA multa custará: R${:.2f}'.format(v, (v-80)*7))
print('Tenha um bom dia! Dirija com segurança!')
