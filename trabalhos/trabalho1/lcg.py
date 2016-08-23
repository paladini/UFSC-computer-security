#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

"""

Esta classe gera números pseudo-aleatórios utilizando o algoritmo LCG (Linear Congruential Generator).
Para chamar esta classe a partir da linha de comando basta digitar:
    
    $ python lcg.py <qtd_de_bits>

Onde "<qtd_de_bits>" é a quantidade de bits que o número gerado deve possuir. Exemplo:

    $ python lcg.py 32
    [LCG] Gerando número de 32 bits...
    [LCG] Número: 4174021489

Referências:
    https://en.wikipedia.org/wiki/Linear_congruential_generator
    https://en.wikipedia.org/wiki/Combined_Linear_Congruential_Generator
    http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_rand.aspx
    https://rosettacode.org/wiki/Linear_congruential_generator

"""
class lcg(object):

    def __init__(self, seed = int(time.time()), m = 2**32, a = 1664525, c = 1013904223, size = None):
        """
            O construtor da classe do gerador de números pseudo-aleatórios é altamente customizável e
            recebe alguns parâmetros com valores padrão baseados no livro "Numerical Recipes: The Art 
            of Scientific Computing" (Press, WH; Teukolsky, SA; Vetterling, WT; Flannery, BP).

            Por padrão vai gerar um número de 32 bits, mas caso um "size" seja fornecido, vai gerar
            somente números com "size" bits.

            Args:
                seed: valor de semente para iniciar o gerador de números pseudo-aleatórios. Se não 
                      informado, utiliza o Unix Timestamp (Epoch) de acordo com as informações do sistema.
                m: o módulo, cujo valor padrão é 2^32 / 4294967296.
                a: o multiplicador, cujo valor padrão é 1664525.
                c: o incremento, cujo valor é 1013904223.
                size: o tamanho em bits do número a ser gerado, cujo valor padrão é None (na prática é 32).

            Returns:
                Esse método não retorna nada.
                
        """
        self.a = a
        self.c = c
        self.seed = seed
        self.size = size
        if self.size:
            self.m = 2**size
        else:
            self.m = m

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
        self.seed = self.seed * self.a + self.c
        num = self.seed % self.m
        if self.size:
            while (num.bit_length() < self.size):
                self.seed = self.seed * self.a + self.c
                num = self.seed % self.m
        return num

    def randint(self, a, b):
        """
        Gera um número aleatório que está entre os intervalos "a" e "b". 

        O número a ser gerado, denominado "num", será maior ou igual à "a" e menor ou igual
        à "b". Em outras palavras, a <= num <= b.

        Args:
            a: valor numérico de limite inferior para o número a ser gerado.
            b: valor numérico de limite superior para o número a ser gerado.

        Returns:
            Um valor numérico pseudo-aleatório que está entre os valores a e b.

        """
        self.seed = self.seed * self.a + self.c
        num = self.seed % self.m
        while (not (a <= num <= b)):
            self.seed = self.seed * self.a + self.c
            num = self.seed % self.m
        return num

    def seed(self, new_seed):
        """
        Método para mudar o valor do seed para algum valor desejado.

        Args:
            new_seed: um valor numérico para indicar o novo valor de seed.

        Returns:
            Esse método não retorna nada.

        """
        self.seed = new_seed

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

 
if (__name__ == "__main__"):
    
    bits = int(sys.argv[1])

    print("[LCG] Gerando número de {} bits...".format(bits))
    print("[LCG] Número: {}".format(lcg(size=bits).rand()))