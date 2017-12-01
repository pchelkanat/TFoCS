# Вариация ρ-метода Полларда, разработанная Флойдом:
# x[i]=f^i(a)
# y[i] = f^2i(a) = f(f(x[i]))

import random
from fractions import gcd
from MillerRabin import MillerRabin


# Функция вычисляющая f(x) = (x^2 − 1) mod n
def f(a, n):
    return int((a * a - 1) % n)


def rho_pollard(n):
    # если число четное, то делим на 2, пока не станет нечетным
    # если число является степенью двойки, то возвращаем 2
    if n % 2 == 0:
        while n % 2 == 0:
            n = int(n / 2)
            if n == 1:
                return 2
            else:
                continue

    # выбираем небольшое число x
    x = random.randint(2, 10)
    i, d = 0, 1
    # пока НОД(n,d)=1 или =n (т.е d=0)
    while d == 1 or d == n:
        # на случай, если все зациклится, ограничиваем итерации до 10
        if i > 10:
            x = random.randint(2, 10)
            i = 0

        # вариация Флойда
        x = f(x, n)
        y = f(f(x, n), n)
        d = int(gcd(abs(x - y), n))
        i += 1
    # если число не простое, то d является делителем n, повторяем для n/d
    if not MillerRabin(d):
        return rho_pollard(int(n / d))
    # число простое, значит возвращаем его
    return d


print(rho_pollard(533))
