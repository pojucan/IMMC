# -*- coding: utf-8 -*-

linha1 = input().split(' ')
x1 = float(linha1[0])
y1 = float(linha1[1])
linha2 = input().split(' ')
x2 = float(linha2[0])
y2 = float(linha2[1])
#
x1, y1 = float(linha1[0]), float(linha1[1])
x2, y2 = float(linha2[0]), float(linha2[1])
distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print('%.4f' % distancia)
