#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from lcg import lcg
from primality import MillerRabin 

class BlumBlumShub(object):

    def __init__(self, seed = None, size = None):
        self.size = size
        self.m = MillerRabin.encontrar_primo(self.size) * MillerRabin.encontrar_primo(self.size)
        if (seed):
            self.state = seed % self.m
        else:
            self.state = lcg(size=self.size).randint(2, self.m - 1) % self.m
    
    def rand(self):
        output_bits = ''
        for bit in self.bitstream():
            output_bits += str(bit)
            if (len(output_bits) == self.size):
                break
 
        return int(output_bits, 2)

    def seed(self, new_seed):
        self.state = new_seed
    
    def bitstream(self):
        while (True):
            yield (sum(int(x) for x in bin(self.state)[2:]) % 2)
            self.state = pow(self.state, 2, self.m)

if (__name__ == "__main__"):
    
    bits = int(sys.argv[1])

    print("[Blum Blum Shub] Gerando número de {} bits...".format(bits))
    print("[Blum Blum Shub] Número: {}".format(BlumBlumShub(size=bits).rand()))
