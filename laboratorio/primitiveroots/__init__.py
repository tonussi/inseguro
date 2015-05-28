__author__ = 'lucastonussi'

import sys
from roots import PrimitiveRoots

def main():
    if len(sys.argv) > 1:
	    nro_primo = eval(sys.argv[1])
    else:
	    nro_primo = 331

    pr = PrimitiveRoots()
    myroots = pr.proots(nro_primo)
    print ('Raizes primitivas do', nro_primo, '\n', myroots)

if __name__ == "__main__":
    main()
