# -*- coding: utf-8 -*-
from pseudo import PrimeTester, Twister
import subprocess as sub
import sys, math

BITS = int(math.log10(10 ** 100) / math.log10(2)) + 1  # 333 BITS
BYTES = int((int(math.log10(10 ** 100) / math.log10(2)) + 1) / 8) + 1  # 42 BYTES
IO = open('stderr', 'w')


def dd():
    try:
        comandos = ['dd', 'if=/dev/urandom', 'of=./entropy', 'count=1', 'bs=8']
        a = sub.Popen(comandos, stderr=IO)
        a.communicate()
    except IOError:
        print(IOError)
        sys.exit()
    finally:
        sub._cleanup()

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


def main():
    if len(sys.argv) > 2:
        QUANTIDADE, ACURACIDADE = eval(sys.argv[1]), eval(sys.argv[2])
    else:
        QUANTIDADE, ACURACIDADE = 10, 25

    primestester = PrimeTester()
    pseudo = Twister()

    rejeitados_miller_rabin = 0
    rejeitados_solovay_strassen = 0
    dez_primos_miller_rabin = []
    dez_primos_solovay_strassen = []

    dd()
    n = lerarquivo('entropy')
    pseudo.alimentar(int(n))

    while len(dez_primos_miller_rabin) < QUANTIDADE:
        candidato = pseudo.extrair() | 0x1

        p = primestester.miller_rabin(candidato, ACURACIDADE)
        if p[1]:
            dez_primos_miller_rabin.append(('http://www.wolframalpha.com/input/?i=' + str(candidato) + '+prime?', p[1]))
            print('Valor', candidato, 'primo (Miller-Rabin) ?', p, 'Rejeitados:', rejeitados_miller_rabin)
        rejeitados_miller_rabin += 1

    while len(dez_primos_solovay_strassen) < QUANTIDADE:
        #dd()
        #n = lerarquivo('entropy')
        #twister.alimentar(int(n))
        candidato = pseudo.extrair() | 0x1

        q = primestester.solovay_strassen(candidato, ACURACIDADE)
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
    print('Taxa Rejeitados Miller-Rabin/Rejeitados Solovay-Strassen:',
          rejeitados_miller_rabin / rejeitados_solovay_strassen)
    print('\nMiller-Rabin rejeita:', (rejeitados_miller_rabin / rejeitados_solovay_strassen) * 100, '%',
          'em relacao a Solovay-Strassen')
    print('Taxa de Acertos=', QUANTIDADE, '/', 'Rejeitos Miller-Rabin:', 10 / rejeitados_miller_rabin)
    print('Taxa de Acertos=', QUANTIDADE, '/', 'Rejeitos Solovay-Strassen:', 10 / rejeitados_solovay_strassen)


if __name__ == "__main__":
    main()
