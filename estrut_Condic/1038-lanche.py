# -*- coding: utf-8 -*-

listaCodigo = [1, 2, 3, 4, 5]
listaPreco = [4.00, 4.50, 5.00, 2.00, 1.50]
linhaEntrada = input().split()
c, q = linhaEntrada
c = int(linhaEntrada[0])
q = int(linhaEntrada[1])
c, q = int(linhaEntrada[0]), int(linhaEntrada[1])
if c == listaCodigo[0]:
    total=listaPreco[0]*q
elif c == listaCodigo[1]:
    total=listaPreco[1]*q
elif c == listaCodigo[2]:
    total=listaPreco[2]*q
elif c == listaCodigo[3]:
    total=listaPreco[3]*q
elif c == listaCodigo[4]:
    total=listaPreco[4]*q
print('Total: R$ %.2f' % total)

