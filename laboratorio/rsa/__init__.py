# -*- coding: utf-8 -*-

from rsa import RSAKeyGeneration
import sys


def main():
    print('mensagem:')
    mensagem = input()

    if len(sys.argv) > 2:
        tamanho_chave, acuracidade = eval(sys.argv[1]), eval(sys.argv[2])
    else:
        tamanho_chave, acuracidade = 64, 15

    rsa = RSAKeyGeneration()

    if isinstance(mensagem, int):
        public_key, exponent, private_key = rsa.generate(tamanho_chave, acuracidade)

        ciphertext = rsa.encrypt(mensagem, exponent, public_key)

        print('\nMensagem-valor encriptada:', ciphertext)

        m = rsa.decrypt(ciphertext, private_key, public_key)

        print('\nMensagem-valor decriptada:', m)

    if isinstance(mensagem, str):
        public_key, exponent, private_key = rsa.generate(tamanho_chave, acuracidade)

        ciphertext = rsa.encrypt_bytes(mensagem, exponent, public_key)

        print('\nMensagem-texto encriptada:')

        print('==rsa==')
        for x in ciphertext:
            print(x)
        print('==' + str(tamanho_chave) + 'bits==')

        m = rsa.decrypt_byte(ciphertext, private_key, public_key)

        print('\nMensagem-texto decriptada:', m)

        rest = ''
        for el in m:
            rest += chr(el)

        print('\nMensagem-texto decriptada restaurada:', rest)


if __name__ == "__main__":
    main()
