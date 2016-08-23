#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from lcg import lcg

class MillerRabin(object):

    @staticmethod
    def verificar_testemunha(possivel_testemunha, p, exp, resto):
        possivel_testemunha = pow(possivel_testemunha, resto, p)
        if ((possivel_testemunha == 1) or (possivel_testemunha == p - 1)):
            return False

        for _ in range(exp):
            possivel_testemunha = pow(possivel_testemunha, 2, p)
            if (possivel_testemunha == (p - 1)):
                return False

        return True
    
    @staticmethod
    def verificar_primalidade(p, certeza=100):
        if (p == 2 or p == 3): 
            return True
        elif (p < 2): 
            return False

        resto = p - 1
        exp = 0
        while (resto % 2 == 0):
            resto = resto/2
            exp += 1

        for _ in range(certeza):
            possivel_testemunha = lcg().randint(2, p - 2)
            if (MillerRabin.verificar_testemunha(possivel_testemunha, p, exp, resto)):
                return False

        return True

    @staticmethod
    def encontrar_primo(bits=None):
        bits = bits or 32
        random = lcg(size=bits)

        while (True):
            primo = random.rand()
            if (MillerRabin.verificar_primalidade(primo)):
                return primo

class FermatPrimality(object):

    @staticmethod
    def verificar_primalidade(p):
        if (p == 2):
            return True
        if (not p & 1):
            return False

        if (pow(2, p-1, p) == 1):
            return True
        else:
            return False

    @staticmethod
    def encontrar_primo(bits=None):
        bits = bits or 32
        random = lcg(size=bits)

        while (True):
            primo = random.rand()
            if (FermatPrimality.verificar_primalidade(primo)):
                return primo

if (__name__ == "__main__"):

    bits = int(sys.argv[1])

    print("[MillerRabin] Procurando primo...")
    print("[MillerRabin] {} é primo!".format(MillerRabin.encontrar_primo(bits)))
    
    time.sleep(2)
    
    print("[Fermat] Procurando primo...")
    print("[Fermat] {} é primo!".format(FermatPrimality.encontrar_primo(bits)))


