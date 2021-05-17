# -*- coding: utf-8 -*-

# URI Online Judge | Distância Entre Dois Pontos | 1015
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 14/05/2021

#-- Descrição --#
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula.

# Entrada: O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída: Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.


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
