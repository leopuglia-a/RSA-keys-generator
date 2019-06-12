# coding: utf-8
# Leonardo Puglia Assunção  RA: 94518
# Hugo Vinícius Sartori     RA: 94609

import random

def gdc(e, z):
    if (z == 0):
        return e
    else:
        return gdc(z, e%z)

def main():
    p = 5
    q = 7

    n = p * q
     # n e o tamanho do conjunto

    z = (p-1) * (q-1)

    while True:
        e = random.randrange(2,n)
        if gdc(e, z) == 1:
            break

    d = e+1
    while True:
        t = (e*d) - 1
        if t%z == 0:
            break
        else:
            d += 1

    public_key = (n,e)
    private_key = (n,d)
    print("Chave pública: " + str(public_key))
    print("Chave privada: " + str(private_key))

if __name__ == '__main__':
    main()
