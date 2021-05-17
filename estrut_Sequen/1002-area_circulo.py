# -*- coding: utf-8 -*-

# URI Online Judge | Área do Círculo | 1002
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 14/05/2021

#-- Descrição --#
# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159: Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula.

# Entrada: O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída: Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.


pi = 3.14159
raio = float(input())
area = pi*raio**2
print('A=%.4f' % area)
