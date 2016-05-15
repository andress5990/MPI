"""
Program that calculates PI using the Wallis product
To execute this run: python pi_serial.py
"""
def calcular_pi(N, i=1):

    acum = 1.0

    while i < N:
        # Producto de Wallis
        acum *= ((2.*i / (2.*i - 1)) * (2.*i / (2.*i + 1)))
        i += 1

    return acum


if __name__ == '__main__':
    print calcular_pi(100000000) * 2
