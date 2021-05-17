# -*- coding: utf-8 -*-

# URI Online Judge | Consumo | 1014
# Adaptado: Neilor Tonin, URI Online Judge Brasil
# Resolução: Pojucan
# Data: 14/05/2021

#-- Descrição --#
# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).


# Entrada: O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

# Saída: Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

distancia = int(input())
combustivel = float(input())
consumo = distancia / combustivel
print("%0.3f km/l" %consumo)
