#!/usr/bin/python
# -*- coding: utf-8 -*-

import fractions, time, math, random

class PrimitiveRoots():

    def totient(self, n):
        m = 0
        for k in range(1, n + 1):
            if fractions.gcd(n, k) == 1:
                m += 1
        return m

    def mdcrec(self, a, b):
        if b == 0:
            return a
        if a == 0:
            return b
        return self.mdcrec(b, a % b)

    def isprime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

    ###################################################
    # For example, if n = 14 then the elements of     #
    # Zn^x are the congruence classes {1, 3, 5, 9,    #
    # 11, 13} there are phi(14) = 6 of them. Here     #
    # is a table of their powers modulo 14:           #
    #-------------------------------------------------#
    # x      x  , x2  , x3 ,             ... (mod 14) #
    #-------------------------------------------------#
    # 1  :   1                                        #
    # 3  :   3  ,  9  , 13 , 11 ,  5 ,  1             #
    # 5  :   5  ,  11 , 13 ,  9 ,  3 ,  1             #
    # 9  :   9  ,  11 ,  1                            #
    # 11 :   11 ,   9 ,  1                            #
    # 13 :   13 ,   1                                 #
    ###################################################

    def trialdiv(self, primos, n):
        if n < 2:
            return []
        fatores = []

        for p in primos:
            while n % p == 0:
                fatores.append(p)
                n //= p

        if n > 1:
            fatores.append(n)

        return fatores


    def proots(self, n):
        print ("Valor de Entrada:", n)

        if not self.isprime(n):
            return "Entrada precisa ser um nro primo"

        print ("Deve-se computar raizes primitivas: ", self.totient(self.totient(n)))

        fatores = []
        primos = []
        proots = []

        totient = n - 1

        for v in range(2, n - 1):
            if self.isprime(v):
                primos.append(v)

        primos = sorted(set(primos))
        # print (primos)

        fatores = self.trialdiv(primos, totient)
        # print (fatores)

        print ('As classes congruentes de Z' + str(n) + 'x :', primos)

        for m in range(2, n - 1):
            todosRaiz = True
            #######################################################
            # Um nro m tal qual elevado a totient/p mod n         #
            # e retornar um valor diferente de 1 é raiz primitiva #
            #######################################################
            for pf in fatores:
                if self.moduloPotencia(m, totient // pf, n) == 1:
                    todosRaiz = False
                    break
            if todosRaiz:
                proots.append(m)

        # print (len(sorted(set(proots))) == self.totient(self.totient(n)))

        return sorted(set(proots))

    ######################################################
    # The following is an example in pseudocode based    #
    # on Applied Cryptography by Bruce Schneier.[1]      #
    # The inputs base, expoente, and modulo correspond   #
    # to b, e, and m in the equations given above.       #
    #                                                    #
    #                                                    #
    # [1] : Schneier 1996, p. 244.                       #
    ######################################################

    def moduloPotencia(self, base, expoente, modulo):
        resultado = 1
        base = base % modulo
        while expoente > 0:
            if expoente % 2 == 1:
                # print 'resultado =', resultado, '*', base, 'mod', modulo
                resultado = (resultado * base) % modulo
            expoente = expoente >> 1
            base = (base * base) % modulo

        return resultado

def main():
    pr = PrimitiveRoots()
    print (pr.proots(191))

if __name__ == "__main__":
    main()
