#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from lcg import lcg
from primality import MillerRabin 

"""

Esta classe gera números pseudo-aleatórios utilizando o algoritmo BBS (Blum Blum Shub).
Para chamar esta classe a partir da linha de comando basta digitar:
    
    $ python blum_blum_shub.py <qtd_de_bits>

Onde "<qtd_de_bits>" é a quantidade de bits que o número gerado deve possuir. Exemplo:

    $ python blum_blum_shub.py 32
    [Blum Blum Shub] Gerando número de 32 bits...
    [Blum Blum Shub] Número: 3234751506

Referências:
    https://en.wikipedia.org/wiki/Blum_Blum_Shub
    https://pt.wikipedia.org/wiki/Blum_Blum_Shub
    https://crypto.stackexchange.com/questions/3454/blum-blum-shub-vs-aes-ctr-or-other-csprngs
    https://jeremykun.com/2016/07/11/the-blum-blum-shub-pseudorandom-generator/
    http://cs.ucsb.edu/~koc/cren/project/pp/gawande-mundle.pdf

"""
class BlumBlumShub(object):

    def __init__(self, seed = None, size = None):
        """
        Construtor da classe do gerador de números pseudo-aleatórios.

        Por padrão vai gerar um número pseudo-aleatório de até 32 bits, mas caso um "size" seja fornecido, 
        vai gerar somente números com "size" bits.

        Args:
            seed: valor de semente para iniciar o gerador de números pseudo-aleatórios. Se não 
                  informado, utiliza um valor numérico pseudo-aleatório entre 2 e (m - 1).
            size: o tamanho em bits do número a ser gerado, cujo valor padrão é None (na prática é 32).

        Returns:
            Esse método não retorna nada.
                
        """
        self.size = size
        self.m = MillerRabin.encontrar_primo(self.size) * MillerRabin.encontrar_primo(self.size)
        if (seed):
            self.state = seed % self.m
        else:
            self.state = lcg(size=self.size).randint(2, self.m - 1) % self.m
    
    def rand(self):
        """
        Gera um número aleatório utilizando o algoritmo BBS, que é descrito da seguinte forma:
       
            Xn+1 = (Xn)² mod M 

        Onde: 
            M: é o produto de dois números primos muito grandes (comumente denominados p e q), 
               ambos congruentes a 3 (mod 4) e com mdc (máximo divisor comum) pequeno (fazendo
               o tamanho do ciclo ser grande).
            X0: o seed (X0) precisa ser um inteiro co-primo à M e não pode ser 1 ou 0.
            Xn+1: o próximo número a ser gerado.

        Args:
            Este método não recebe nenhum argumento.

        Returns:
            Um valor numérico pseudo-aleatório de "size" bits. No BBS a saída costuma ser o bit de paridade
            ou um ou mais dos bits menos significantes (vide método bitstram(self)).

        """
        output_bits = ''
        for bit in self.bitstream():
            output_bits += str(bit)
            if (len(output_bits) == self.size):
                break
 
        return int(output_bits, 2)

    def seed(self, new_seed):
        """
        Método para mudar o valor do seed para algum valor desejado.

        Args:
            new_seed: um valor numérico para indicar o novo valor de seed.

        Returns:
            Esse método não retorna nada.

        """
        self.state = new_seed

    def size(self, new_size):
        """
        Método para mudar a quantidade de bits que o número gerado terá.

        Args:
            new_size: um valor numérico para indicar a nova quantidade de bits do número gerado.

        Returns:
            Esse método não retorna nada.

        """
        if self.size != new_size:
            self.size = new_size
            self.m = 2**new_size
    
    def bitstream(self):
        """
            Método auxiliar (e necessário) para o cálculo do número pseudo-aleatório utilizando o algoritmo BBS.

            Returns:
                Bit que vai compor um conjunto de bits pseudo-aleatórios que depois serão convertidos
                para um valor numérico pseudo-aleatório.
        """
        while (True):
            yield (sum(int(x) for x in bin(self.state)[2:]) % 2)
            self.state = pow(self.state, 2, self.m)

if (__name__ == "__main__"):
    
    bits = int(sys.argv[1])

    print("[Blum Blum Shub] Gerando número de {} bits...".format(bits))
    print("[Blum Blum Shub] Número: {}".format(BlumBlumShub(size=bits).rand()))
