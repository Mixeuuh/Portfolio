# -*- coding: utf-8 -*-
# Programa: fibonaci02.py
# Programador: Mixeuuh
# Data: 16/05/2023
# Este programa lê um inteiro positivo num > 1 e calcula e imprime
# os num termos da sequência de Fibonaci usando um algoritmo iterativo.
# início do módulo principal
# descrição das variáveis utilizadas
# int num, fib1, fib2, novoFib, i
# pré: num > 0
# Passo 1. Leia um inteiro positivo
num = int(input())

# Passo 2. Calcule e imprima os num termos da sequência
# Passo 2.1. Inicializando as variaveis
fib1 = 1
fib2 = 1
novoFib = 2

# Passo 2.2. Imprima o primeiro termo
print('{0:d} {1:d} {2:d} '.format(fib1, fib2, novoFib),end='')

# Passo 3. Gere e imprima os demais termos da sequência
for i in range(1, num-2):
    fib1 = fib2
    fib2 = novoFib    
    novoFib = fib1 + fib2
    print('{0:d} '.format(novoFib),end='')

# pós: para i em {1,...,num}: fib_i and fib_1 == 1 and 
#      fib_2 == 1 and fib_i == fib_(i-2) + fib_(i-1) and i >= 3
# fim do módulo principal
# ==============================================================================>
