'''
    Функция Эйлера
    φ(p) = p − 1 для всех простых p,
    φ(p^k) = p^k − p^(k−1) для простых p и натуральных k ,
    φ(p·q) = φ(p)·φ(q) для взаимопростых p и q.
'''
from fractions import gcd


def EulerPhi(num):
    result = 1
    if not num % 2:
        for x in range(3, num, 2):
            if gcd(x, num) == 1:
                result += 1
    else:
        for x in range(2, num):
            if gcd(x, num) == 1:
                result += 1
    return result


print(EulerPhi(2))  # 2-1=1
print(EulerPhi(3))  # 3-1=2
print(EulerPhi(5))  # 5-1=4
print(EulerPhi(8))  # 2^3=2^3-2^2=8-4=4
print(EulerPhi(9))  # 3^2=9-3=6
print(EulerPhi(15))  # 2*4=8
print(EulerPhi(18))  # 1*(9-3)=6
