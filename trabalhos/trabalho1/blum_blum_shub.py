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
        Gera um número aleatório utilizando a fórmula para calcular a LCG, que é descrita pela relação
        de recorrência expressa a seguir:

            Xn+1 = (a * Xn + c) mod m

        Onde: 
            m: o módulo (0 < m)
            a: o multiplicador (0 < a < m)
            c: o incremento (0 <= c < m)
            X: sequência de valores pseudo-aleatórios.
            X0: o "seed" ou valor de começo.
            Xn+1: o próximo número a ser gerado.

        Se uma instância dessa classe possuir o atributo "size" definido no momento da construção do objeto
        ou definido posteriormente em uma chamada ao método seed(self, new_seed), então o número gerado de 
        forma pseudo-aleatória possuirá "size" bits (ficará dentro de um loop enquanto não atingir essa 
        quantidade de bits estipulada). Caso a instância não possua o atributo "size" definido, então o
        número pseudo-aleatório gerado possuirá até 32 bits.

        Args:
            Este método não recebe nenhum argumento.

        Returns:
            Um valor numérico pseudo-aleatório de "size" bits.

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
        while (True):
            yield (sum(int(x) for x in bin(self.state)[2:]) % 2)
            self.state = pow(self.state, 2, self.m)

if (__name__ == "__main__"):
    
    bits = int(sys.argv[1])

    print("[Blum Blum Shub] Gerando número de {} bits...".format(bits))
    print("[Blum Blum Shub] Número: {}".format(BlumBlumShub(size=bits).rand()))
