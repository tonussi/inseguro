# -*- coding: utf-8 -*-
from pseudo import PrimeTester, Twister
import random, subprocess, sys

IO = open('stderr', 'w')


def dd():
    try:
        comandos = ['dd', 'if=/dev/urandom', 'of=./entropy', 'count=1', 'bs=8']
        a = subprocess.Popen(comandos, stderr=IO)
        a.communicate()
    except IOError:
        print(IOError)
        sys.exit()
    finally:
        subprocess._cleanup()


def lerarquivo(nome):
    try:
        plain = ''
        arq = open(nome, 'rb')
        for byte in arq.read():
            plain += str(byte)
    except IOError:
        print(IOError)
        sys.exit()
    finally:
        arq.close()
    return plain


class RSAKeyGeneration(object):
    def generate(self, qbits, nova_acuracidade):

        if nova_acuracidade > 0 and nova_acuracidade <= 25:
            acuracidade = nova_acuracidade
        else:
            acuracidade = 15

        primestester = PrimeTester()
        pseudo = Twister()

        if sys.platform.startswith('linux'):
            dd()
            public_key = lerarquivo('entropy')
            pseudo.alimentar(int(public_key))
        else:
            pseudo.alimentar(162432351271981621172)

        test = False

        while not test:
            p = pseudo.extrair(qbits) | 0x1
            test = primestester.solovay_strassen(p, acuracidade)[1]

        # print('\nChecar primeiro nro primo:\n',
        # 'http://www.wolframalpha.com/input/?i=' + str(p) + '+prime?\n')

        test = False

        while not test:
            q = pseudo.extrair(qbits) | 0x1
            test = primestester.solovay_strassen(q, acuracidade)[1]

        # print('\nChecar segundo nro primo:\n',
        # 'http://www.wolframalpha.com/input/?i=' + str(q) + '+prime?\n')

        # 1. Choose two distinct prime numbers p and q.
        # 2. Compute n = pq.
        n = p * q
        # print(str(n) + ' = ' + str(p) + ' * ' + str(q))

        # 3. Compute phi(n) = phi(p)phi(q) = (p − 1)(q − 1) = n - (p + q -1),
        # where phi is Euler's phi euler function. This value is kept private.
        phi = n - (p + q - 1)
        # print(str(n) + ' - ' + '(' + str(p) + ' + ' + str(q) + ' - ' + str(1) + ')')

        # Choose an integer e such that 1 < e < phi(n) and
        # gcd(e, phi(n)) = 1; i.e., e and phi(n) are co-primes.
        e = 0
        while self.gcd(e, phi) != 1:
            e = random.randint(65537, phi)

        # 5. Determine d as d ≡ e⁻¹ (mod φ(n)); i.e., d is the modular
        # multiplicative inverse of e (modulo phi(n)).
        d = self.modinv(e, phi)
        # print('Inversa multiplicativa de: ' + str(e) + ' (modulo ' + str(phi) + ') is ' + str(d))

        return n, e, d

    def encrypt_bytes(self, message, exponent, public_key):
        arranjo = []
        for el in message:
            arranjo.append(self.encrypt(int(ord(el)), exponent, public_key))
        return arranjo

    def encrypt(self, message, exponent, public_key):
        return self.potencia(message, exponent, public_key)

    def decrypt_byte(self, ciphertext, private_key, public_key):
        arranjo = []
        for el in ciphertext:
            arranjo.append(self.decrypt(el, private_key, public_key))
        return arranjo

    def decrypt(self, ciphertext, private_key, public_key):
        return self.potencia(ciphertext, private_key, public_key)

    def potencia(self, base, exp, modulo):
        res = 1
        base = base % modulo
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % modulo
            exp = exp >> 1
            base = (base * base) % modulo
        return res

    def modinv(self, a, m):
        gcd, x, y = self.egcd(a, m)
        if gcd != 1:
            return None
        else:
            return x % m

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def totient(self, n):
        m = 0
        for k in range(1, n + 1):
            if self.gcd(n, k) == 1:
                m += 1
        return m

    def gcd(self, a, b):
        if b == 0:
            return a
        if a == 0:
            return b
        return self.gcd(b, a % b)
