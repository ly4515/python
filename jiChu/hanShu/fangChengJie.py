# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解

import math
def quadratic(a, b, c):
    d = math.sqrt(b*b-4*a*c)
    if d < 0:
        return ("error,b*b-4*a*c<0")
    else:
        x1 = (-b+d)/2*a
        x2 = (-b-d)/2*a
    return x1, x2

print(quadratic(2, -3, 1))
print(quadratic(-1, 3, 4))
print(quadratic(1, 3, -4))