# -*- coding: utf-8 -*-
import random as rand


class PseudoRandomGenerator(object):
    def __init__(self, index=0):
        self.N = 624
        self.M = 397
        self.mersenne_twister = [x for x in range(624)]
        self.index = 0

    def solovay_strassen(self, primo, acuracidade=5):
        nro_tentativas = 0

        if primo == 2 or primo == 3:
            return (nro_tentativas, True)
        if primo < 2:
            raise ValueError('Entrada < 2')
        if primo % 2 == 0:
            raise ValueError('Entrada % 2 == 0')

        for _ in range(acuracidade):
            nro_tentativas += 1
            a = rand.randint(2, primo - 1)

            res = self.adrien_legendre(a, primo)

            potencia = self.modulo_potencia(a, (primo - 1) // 2, primo)

            if res == 0 or potencia != res % primo:
                return (nro_tentativas, False)

        return (nro_tentativas, True)

    def adrien_legendre(self, a, primo):
        if a == 0 or a == 1:
            return a
        if a % 2 == 0:
            res = self.adrien_legendre(a // 2, primo)
            if ((primo ** 2) - 1) & 8 != 0:
                res = -res
        else:
            res = self.adrien_legendre(primo % a, a)
            if (a - 1) * (primo - 1) & 4 != 0:
                res = -res
        return res

    def fatora(self, n):
        exp2 = 0
        while n % 2 == 0:
            n = n // 2
            exp2 += 1
        return exp2, n

    def testa_candidato(self, primo_candidato, primo, expoente, resto):
        primo_candidato = self.modulo_potencia(primo_candidato, resto, primo)

        if primo_candidato == 1 or primo_candidato == primo - 1:
            return False

        for _ in range(expoente):
            primo_candidato = self.modulo_potencia(primo_candidato, 2, primo)

            if primo_candidato == primo - 1:
                return False

        return True

    def miller_rabin(self, primo, acuracidade=5):
        nro_tentativas = 0

        if primo == 2 or primo == 3:
            return (nro_tentativas, True)
        if primo < 2:
            return (nro_tentativas, False)
        if primo % 2 == 0:
            return (nro_tentativas, False)

        expoente, resto = self.fatora(primo - 1)

        for _ in range(acuracidade):
            nro_tentativas += 1

            possivelmente_primo = rand.randint(2, primo - 2)
            if self.testa_candidato(possivelmente_primo, primo, expoente, resto):
                return (nro_tentativas, False)

        return (nro_tentativas, True)

    def modulo_potencia(self, base, exp, modulo):
        res = 1
        base = base % modulo
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % modulo
            exp = exp >> 1
            base = (base * base) % modulo
        return res

    def alimentar_gerador(self, seed):
        self.index = 0
        self.mersenne_twister[0] = seed
        for i in range(1, self.N):
            self.mersenne_twister[i] = (
                1812433253 * (self.mersenne_twister[i - 1] ^ (self.mersenne_twister[i - 1] >> 30)) + i)

    def extract_number(self):
        if self.index == 0:
            self.gerar_valores()
        y = self.mersenne_twister[self.index]
        y = self.y(y)
        self.index += 1
        return y

    def y(self, y):
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= (y >> 18)
        return y

    def gerar_valores(self):
        for i in range(self.N):
            y = (self.mersenne_twister[i] and 0x80000000) + (self.mersenne_twister[(i + 1) % self.N] and 0x7fffffff)
            self.mersenne_twister[i] = self.mersenne_twister[(i + 397) % self.N] ^ (y >> 1)
            if y % 2 != 0:
                self.mersenne_twister[i] %= \
                    3165575419983653090010874830062594726784053790351448619853466963349163783494971481831605960617320681
