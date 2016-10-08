#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange
from fractions import gcd
import sys

class DHMUtils(object):

    @staticmethod
    def num_coprimos(n):
        '''
        Função que calcula o totiente de Euler de n (ou o número de coprimos de 'n').
        '''
        num_coprimos = 0
        for i in range(n):
            if (gcd(i, n) == 1):
                num_coprimos += 1
        return num_coprimos

    @staticmethod
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

    @staticmethod
    def raiz_primitiva(n):
        '''
        Função que encontra uma raiz primitiva de um inteiro n dado.
        '''
        p = DHMUtils.num_coprimos(n)
        fatores = DHMUtils.fatores_primos(p)
        while (True):
            a = randrange(1, n)
            if (all(pow(a, p // f, n) != 1 for f in fatores)):
                return a
