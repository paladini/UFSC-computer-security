#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Os métodos implementados permitem encontrar as raízes primitivas de um inteiro n.
Utiliza o método de cálculo de MDC disponível na biblioteca padrão do Python (fractions.gdc).

Como usar:
    python raizes.py <n_desejado>

O programa fará os cálculos e então imprimirá na tela as raízes primitivas do <n_desejado> inserido. Exemplo:

    python raizes.py

'''

from random import randrange
from fractions import gcd
import sys

def num_coprimos(n):
    '''
    Função que calcula o totiente de Euler de n (ou o número de coprimos de 'n').
    '''
    num_coprimos = 0
    for i in range(n):
        if (gcd(i, n) == 1):
            num_coprimos += 1
    return num_coprimos

def fatores_primos(n):
    '''
    Função que calcula todos os fatores primos de 'n' (até que a sua raiz quadrada seja atingida).
    Retorna uma lista ordenada dos fatores primos de 'n'.
    '''
    fatores = set()
    i = 2
    while (i**2 <= n):
        if (n % i == 0):
            n = n // i
            fatores.add(i)
        else:
            i += 1
    fatores.add(n)
    return sorted(fatores)

def raizes_primitivas(n):
    '''
    Função que encontra todas as raízes primitivas de um inteiro n.
    '''
    p = num_coprimos(n)
    fatores = fatores_primos(p)
    limite = num_coprimos(p)
    raizes_p = set()
    while (len(raizes_p) != limite):
        a = randrange(1, n)
        if (all(pow(a, p // f, n) != 1 for f in fatores)):
            raizes_p.add(a)
    return sorted(raizes_p)

if (__name__ == "__main__"):
    # Verificando se existe algum argumento para o programa
    if (len(sys.argv) <= 1):
        print("Por favor, insira um valor numerico n.")
        sys.exit(0)
    n = int(sys.argv[1])
    raizes_primitivas = raizes_primitivas(n)
    print("As raízes primitivas de {} são:".format(n))
    print(raizes_primitivas)