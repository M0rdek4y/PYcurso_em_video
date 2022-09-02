from time import sleep
cr = str(input('DIgite 0 para inicar a contagem regressiva dos fogos'))
if cr == '0':
    for cc in range(10, -1, -1):
        print(cc)
        sleep(1)
    print('BOOM!!')
