#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Classe responsável por representar uma parte interessada dentro do algoritmo de acordo de chaves Diffie-Hellman-Merkle (DHM).
'''

import random

class DHM(object):

	def __init__(self, p, g):
		self.private = random.getrandbits(512)
		self.p = p
		self.g = g

	def public_key(self):
		'''
		Gera a "chave pública" do DHM. Supondo que a parte em questão seja Alice, este método vai 
		gerar o valor que será trocado publicamente com Bob.
		
		Returns:
			g^{a} \pmod{p} = g**a mod p

		'''
		return pow(self.g, self.private, self.p)

	def shared_secret_key(self, key):
		'''
		Gera o segredo compartilhado do DHM a partir da chave recebida. Supondo que a parte em questão
		seja Alice, este método vai gerar o segredo compartilhado entre Alice e Bob, parte fianl do
		protocolo DHM.

		Args:
			key: a chave pública da outra parte interessada.

		Returns:
			key^{a} \pmod{p} = key**a mod p
		'''
		return pow(key, self.private, self.p)