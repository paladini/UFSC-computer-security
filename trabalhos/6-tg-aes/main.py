#!/usr/bin/env python

from aes import AES

# Entradas necessarias para o AES
chave = 0x2d955154c41b31540604cf94c898defde069b7b92df4a03aff0975a68f32ddf9
texto_plano = 0xabcdef0123456789abcdef0123456789

def prepare_hex_to_print(hex_string):
	return " ".join(hex(ord(n)) for n in hex_string)

if (__name__ == "__main__"):

	aes = AES(chave)

	# Processo de encriptacao
	print("\n\t\tE N C R I P T A C A O\n")
	print("Chave: {}".format(hex(chave)))
	print("Entrada (texto plano): {}".format(hex(texto_plano)))
	encriptado = aes.encrypt(texto_plano)
	print("Saida (encriptado): {}\n\n".format(hex(encriptado)))
