# -*- coding: utf-8 -*-
from pseudo import PseudoRandomGenerator
import subprocess as sub
import sys, math

ACURACIDADE = 25
BITS = int(math.log10(10 ** 100) / math.log10(2)) + 1  # 333 BITS
BYTES = int((int(math.log10(10 ** 100) / math.log10(2)) + 1) / 8) + 1  # 42 BYTES
IO = open('stderr', 'w')


def dd():
    try:
        comandos = ['dd', 'if=/dev/urandom', 'of=./entropy', 'count=42', 'bs=1']
        a = sub.Popen(comandos, stderr=IO)
        a.communicate()
    except IOError:
        print(IOError)
        sys.exit()


def ler_arquivo(nome):
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


def main():
    pseudo = PseudoRandomGenerator()
    rejeitados_miller_rabin = 0
    rejeitados_solovay_strassen = 0
    dez_primos_miller_rabin = []
    dez_primos_solovay_strassen = []

    while len(dez_primos_miller_rabin) < 10:
        dd()
        n = ler_arquivo('entropy')
        pseudo.alimentar_gerador(int(n))
        candidato = pseudo.extract_number() | 0x1

        p = pseudo.miller_rabin(candidato, ACURACIDADE)
        if p[1]:
            dez_primos_miller_rabin.append(('http://www.wolframalpha.com/input/?i=' + str(candidato) + '+prime?', p[1]))
            print('Valor', candidato, 'primo (Miller-Rabin) ?', p, 'Rejeitados:', rejeitados_miller_rabin)
        rejeitados_miller_rabin += 1

    while len(dez_primos_solovay_strassen) < 10:
        dd()
        n = ler_arquivo('entropy')
        pseudo.alimentar_gerador(int(n))
        candidato = pseudo.extract_number() | 0x1

        q = pseudo.solovay_strassen(candidato, ACURACIDADE)
        if q[1]:
            dez_primos_solovay_strassen.append(
                ('http://www.wolframalpha.com/input/?i=' + str(candidato) + '+prime?', p[1]))
            print('Valor', candidato, 'primo (Solovay–Strassen) ?', q, 'Rejeitados:', rejeitados_solovay_strassen)
        rejeitados_solovay_strassen += 1

    print('\nOs 10 primos distintos para cada algoritmo de teste', '\n')
    print('Com constante de acuracidade igual a ', ACURACIDADE, '\n')

    for e in dez_primos_miller_rabin:
        print('Miller-Rabin:', e)

    for e in dez_primos_solovay_strassen:
        print('Solovay-Strassen:', e)

    print('\nTotal Rejeitados Miller-Rabin:', rejeitados_miller_rabin,
          '\nTotal Rejeitados Solovay-Strassen:', rejeitados_solovay_strassen)
    print('\nDados:')
    print('Rejeitados Miller-Rabin/Rejeitados Solovay-Strassen:', rejeitados_miller_rabin / rejeitados_solovay_strassen)
    print('Taxa de Acertos=10/Rejeitos Miller-Rabin:', 10 / rejeitados_miller_rabin)
    print('Taxa de Acertos=10/Rejeitos Solovay-Strassen:', 10 / rejeitados_solovay_strassen)


if __name__ == "__main__":
    main()
