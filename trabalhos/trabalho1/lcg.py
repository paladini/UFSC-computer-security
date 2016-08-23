#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

class lcg(object):

    # Initializes everything
    # Values taken rom "Numerical Recipes"
    def __init__(self, seed = int(time.time()), m = 2**32, a = 1664525, c = 1013904223, size = None):
        self.a = a
        self.c = c
        self.seed = seed
        self.size = size
        if self.size:
            self.m = 2**size
        else:
            self.m = m

    # Generate a new number
    def rand(self):
        self.seed = self.seed * self.a + self.c
        num = self.seed % self.m
        if self.size:
            while (num.bit_length() < self.size):
                self.seed = self.seed * self.a + self.c
                num = self.seed % self.m
        return num

    # Generate random between interval
    def randint(self, a, b):
        self.seed = self.seed * self.a + self.c
        num = self.seed % self.m
        while (not (a <= num <= b)):
            self.seed = self.seed * self.a + self.c
            num = self.seed % self.m
        return num

    # Change the seed
    def seed(self, new_seed):
        self.seed = new_seed

    # Change the size of generated PRN.
    def size(self, new_size):
        if self.size != new_size:
            self.size = new_size
            self.m = 2**new_size

 
if (__name__ == "__main__"):
    
    bits = int(sys.argv[1])

    print("[LCG] Gerando número de {} bits...".format(bits))
    print("[LCG] Número: {}".format(lcg(size=bits).rand()))