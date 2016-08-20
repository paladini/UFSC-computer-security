#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class lcg:

    # Initializes everything
    # Values taken rom "Numerical Recipes"
    def __init__(self, seed, m = 2**32, a = 1664525, c = 1013904223, size = None):
        self.seed = seed
        self.a = a
        self.c = c
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

    # Change the seed
    def seed(self, new_seed):
        self.seed = new_seed

    # Change the size of generated PRN.
    def size(self, new_size):
        if self.size != new_size:
            self.size = new_size
            self.m = 2**new_size


# class xorshift:

#     def __init__(self):

#     def rand(self):

#     def srand(self, new_seed):
