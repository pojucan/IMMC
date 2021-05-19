# -*- coding: utf-8 -*-

# URI Online Judge | Teste de Seleção 1 | 1035
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 18/05/2021

## Descrição:
# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior 
# do que C e se D for maior do que A, e a soma de C com D for 
# maior que a soma de A e B e se C e D, ambos, forem positivos 
# e se a variável A for par escrever a mensagem "Valores aceitos", 
# senão escrever "Valores nao aceitos".

# Entrada: Quatro números inteiros A, B, C e D.
# Saída: Mostre a respectiva mensagem após a validação dos valores.

x = input().split()
a, b, c, d = x
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
