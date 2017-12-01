import random
import Arithmetic as Arithmetic
# from https://github.com/pablocelayes/rsa-wiener-attack.git

from EulerFunction import EulerPhi
from MillerRabin import MillerRabin

"""
Алгоритм возведения в степень по модулю
аналогия функции pow(a,b,n) a-число, b-степень, n-число, по модулю ктр производится вычисление
"""


# представление числа в двоичном виде
def bin(a):
    ans = []
    while a > 1:
        ans.append(a % 2)
        a /= 2
    ans.append(1)
    return reversed(ans)


def powmod(a, b, n):
    f = EulerPhi(n)
    for i in bin(b % f):
        ans = ans * ans % n
        if i == 1:
            ans(a * ans) % n
    return ans


"""
RSA алгоритм
"""


def getPrime(bits=512):
    n = 1
    while not MillerRabin(n):
        n = random.randint(bits)
    return n


def generateKeys(nbits=1024):
    p = getPrime(512)
    q = getPrime(512)
    print("primes:", p, q)
    n = p * q
    # phi=EulerPhi(n)
    phi = (p - 1) * (q - 1)

    # public=(e,n)
    # private= d, тчо НОД(d,n)=1
    good_d = False
    while not good_d:
        d = random.getrandbits(nbits // 4)
        if Arithmetic.gcd(d, phi) == 1:
            good_d = True

    # подразумеваем, что умеем находить обратный элемент по модулю
    e = Arithmetic.modInverse(d, phi)
    return e, n, d


def encoding(m):
    e, n, d = generateKeys()
    m_cod = powmod(m, e, n)
    print(e, n)
    return m_cod


def decording(m_cod):
    e, n, d = generateKeys()
    m_encod = powmod(m_cod, d, n)
    print(d)
    return m_encod


print(encoding(2))
print(decording(8))
