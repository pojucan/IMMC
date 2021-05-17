# -*- coding: utf-8 -*-

# URI Online Judge | Salário | 1008
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 14/05/2021

#-- Descrição --#
# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

# Entrada: O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente. 

# Saída: Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.


numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
salario = float(horas_trabalhadas * valor_hora)
print("NUMBER = %d" %numero_funcionario)
print("SALARY = U$ %0.2f" %salario)
