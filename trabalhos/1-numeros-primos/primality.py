#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from lcg import lcg

"""

As classes deste arquivo verificam se os números fornecidos são primos e geram números 
primos de tamanho variável de bits de forma pseudo-aleatória.

Para executar esse arquivo a partir da linha de comando basta digitar:
    
    $ python primality.py <qtd_de_bits>

Onde "<qtd_de_bits>" é a quantidade de bits que o número gerado deve possuir. Exemplo:

    $ python primality.py 128
    [MillerRabin] Procurando primo...
    [MillerRabin] 304159568226184448912103696911866306307 é primo!
    [Fermat] Procurando primo...
    [Fermat] 301970148924118150955226359108149582211 é primo!

Referências:
    https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
    https://en.wikipedia.org/wiki/Pseudoprime
    https://pt.wikipedia.org/wiki/Teste_de_primalidade_de_Miller-Rabin
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    https://pt.wikipedia.org/wiki/Teste_de_primalidade_de_Fermat
    https://jeremykun.com/2013/06/16/miller-rabin-primality-test/
    http://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html
    https://www.youtube.com/watch?v=qfgYfyyBRcY

"""
class MillerRabin(object):

    @staticmethod
    def verificar_testemunha(possivel_testemunha, p, exp, resto):
        """
        Verifica se a possível testemunha de que um número não é primo é
        realmente testemunha. Se for, significa que o número que está 
        sendo testado tem uma testemunha da sua não primalidade, de forma
        que a hipótese de que o número testado é primo pode ser descartada.

        Args:
            possivel_testemunha: a possível testemunha de que "p" não é primo.
                                 Será testemunha caso a^d ≢ 1 (mod n) e 
                                 a^((2^r)d) ≢ -1 (mod n) para todo 0 <= r <= s - 1.
            p: o número para o qual a primalidade está sendo testada.
            exp, resto: números inteiros, onde 'resto' é um número ímpar.

        Returns:
            True se a possível testemunha for uma testemunha de que "p" não é primo.
            False se a possível testemunha não for uma testemunha de verdade.

        """
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
        """
        O teste de Miller-Rabin é um importantíssimo teste probabilístico da primitividade de um número dado.
        Se um número passa nesse teste significa que ele tem uma probabilidade >= 75% de ser um número primo,
        mas até este número ser provado como sendo um número primo ele é considerado apenas um "pseudoprimo".

        Ao aplicar o mesmo teste várias vezes, a margem de erro pode ser diminuída aleatoriamente, de forma
        que a margem de erro final seja consideravelmente baixa. Ele é baseado no "Pequeno Teorema de Fermat",
        que consiste do "Teste de primalidade de Fermat".

        Args:
            p: o número a ser testado.
            certeza: o grau de "certeza" de que este número seja de fato um número primo. Valor padrão é 100, o
                     que significa que o teste será aplicado 100 vezes.

        Returns:
            True se o número é um (pseudo-)primo.
            False se o número não é primo.

        """
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
        """
        Encontra um número primo que possui 'bits' bits utilizando uma busca com números gerados de forma pseudo-aleatória. 

        Args:
            bits: quantidade de bits que o número primo deve possuir. Se nenhum valor for informado, será usado 32 bits.
        
        Returns:
            Um valor númerico com 'bits' bits e que é primo.

        """
        bits = bits or 32
        random = lcg(size=bits)

        while (True):
            primo = random.rand()
            if (MillerRabin.verificar_primalidade(primo)):
                return primo

class FermatPrimality(object):

    @staticmethod
    def verificar_primalidade(p):
        """
        Verifica se o número dado 'p' é um número primo através do método de Fermat, também conhecido 
        como "Teste de Primalidade de Fermat". Este é um dos métodos mais simples para verificar se um 
        número é primo ou não (e provavelmente um dos mais elegantes também). Neste método a composição
        do número dado é verificada e os números que falham no teste não são primos.

        Esta implementação não leva em consideração os números de Carmichael, que são infinitos e
        passam pelo teste, mas não são primos. Portanto, a partir deste teste podemos obter apenas
        números que são considerados "pseudoprimos".

        Args:
            p: o número que será testado a primalidade.

        Returns:
            True significa que o número é pseudoprimo, ou seja, provavelmente é primo (existem falso-positivos).
            False significa que o número é composto, ou seja, não é primo.

        """
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
        """
        Encontra um número primo que possui 'bits' bits utilizando uma busca com números gerados de forma pseudo-aleatória. 

        Args:
            bits: quantidade de bits que o número primo deve possuir. Se nenhum valor for informado, será usado 32 bits.
        
        Returns:
            Um valor númerico com 'bits' bits e que é primo.

        """
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


