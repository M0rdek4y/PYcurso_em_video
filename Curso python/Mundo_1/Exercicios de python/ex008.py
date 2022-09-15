from stylefont import aze, ved, azc, res, rox

m = float(input('{}Digite uma distancia em metros: '.format(aze)))
cm = m*100
mm = cm*10
print('{3}A distância de {4}{0}{3} metro tem {5}{1:.2f}{3} centimetros e {6}{2:.2f}{3} milimetros!{6}'.format(m, cm, mm, aze, ved, azc, rox, res))
