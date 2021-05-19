# -*- coding: utf-8 -*-

# URI Online Judge | Lanche | 1038
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 18/05/2021

## Descrição:
# Com base na tabela abaixo, escreva um programa que leia o 
# código de um item e a quantidade deste item. A seguir, 
# calcule e mostre o valor da conta a pagar.
#
# codigo especificação       preço
# 1      Cachorro quente     R$ 4.00
# 2      X-Salada            R$ 4.50
# 3      X-Bacon             R$ 5.00
# 4      Torrada Simples     R$ 2.00  
# 5      Refrigerante        R$ 1.50

# Entrada: O arquivo de entrada contém dois valores inteiros 
# correspondentes ao código e à quantidade de um item 
# conforme tabela acima.
# Saída: O arquivo de saída deve conter a mensagem "Total: R$ " 
# seguido pelo valor a ser pago, com 2 casas após o ponto 
# decimal.

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

