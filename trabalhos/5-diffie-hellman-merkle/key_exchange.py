#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Implementa um exemplo do protocolo Diffie-Hellman-Merkle (DHM).
'''

from random import randrange
from fractions import gcd
from dhm import DHM
from dhm_utils import DHMUtils
from primality import MillerRabin

# Procurando primo de 512 bits (possuem mais do que 100 digitos)
prime = MillerRabin.encontrar_primo(30)

# Procurando raizes primitivas desse número primo e obtendo alguma de forma aleatória.
primitive_root = DHMUtils.raiz_primitiva(prime)

# Calculando chave pública de Alice e Bob
alice = DHM(prime, primitive_root)
bob = DHM(prime, primitive_root)
A = alice.public_key()
B = bob.public_key()

# Calculando segredo compartilhado
secretAlice = alice.shared_secret_key(B)
secretBob = bob.shared_secret_key(A)

print("Quantidade de dígitos do número primo: {}".format(len(str(prime))))
print("O segredo compartilhado entre Alice e Bob é igual?")
print(secretAlice == secretBob)