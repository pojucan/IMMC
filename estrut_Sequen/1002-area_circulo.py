# -*- coding: utf-8 -*-

# URI Online Judge | Área do Círculo | 1002
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 14/05/2021

<<<<<<< HEAD
# Descrição
# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando 
# para este problema que π = 3.14159: Efetue o cálculo da área, elevando o valor de raio 
# ao quadrado e multiplicando por π.

# Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a 
# variável raio.
# Saída: Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme 
# exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla 
# precisão (double).Como todos os problemas, não esqueça de imprimir o fim de linha após 
# o resultado, caso contrário, você receberá "Presentation Error".
=======
#-- Descrição --#
# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159: Efetue o cálculo da área, elevando o 
# valor de raio ao quadrado e multiplicando por π.

# Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
# Saída: Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla 
# precisão (double).Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
>>>>>>> aee50729ce7fa6b6998e47c863c447b2bad8cfc4


pi = 3.14159
raio = float(input())
area = pi*raio**2
print('A=%.4f' % area)
