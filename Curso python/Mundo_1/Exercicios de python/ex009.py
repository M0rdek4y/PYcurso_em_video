from stylefont import aze, ved, azc, res, ama

num = int(input('{}Digite um valor: '.format(aze)))
b = ('–'*16)
print("""{12}{0}
{13}{1}{15} x 1 = {14}{2}
{13}{1}{15} x 2 = {14}{3}
{13}{1}{15} x 3 = {14}{4}
{13}{1}{15} x 4 = {14}{5}
{13}{1}{15} x 5 = {14}{6}
{13}{1}{15} x 6 = {14}{7}
{13}{1}{15} x 7 = {14}{8}
{13}{1}{15} x 8 = {14}{9}
{13}{1}{15} x 9 = {14}{10}
{13}{1}{15} x 10 = {14}{11}
{12}{0}""".format(b, num, num*1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10, ama, azc, res, ved, aze))
