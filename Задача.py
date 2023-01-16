import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Задача
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0
# Данные для работы
# Заданная функция

def func(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30

# Производная
xs =sp.Symbol('x',real=True)
f = -12*xs**4*sp.sin(sp.cos(xs)) - 18*xs**3+5*xs**2 + 10*xs - 30
d = sp.diff(f)
d
def d1func(x):
    return d.subs(xs,x)
    #return 12*x**4*np.sin(x)*np.cos(np.cos(x)) - 48*x**3*np.sin(np.cos(x))-54*x**2 + 10*x + 10

# Интервал, сетка, значение функции
lhs = -10
rhs = 10
N = (abs(lhs)+abs(rhs))*100
x = np.linspace(lhs,rhs,N)
y = [func(x_i) for x_i in x]

# Нахождения корня на отрезке
def bisection(f, lhs, rhs, eps=1e-10):
    mid = (lhs+rhs)/2
    while abs(lhs-rhs) > eps:
        mid = (lhs+rhs)/2
        if f(lhs)*f(mid) > 0:
            lhs = mid
        else:
            rhs = mid
    return mid

# 1. Определить корни
corn = []
for i in range(x.size-1):
    q =  bisection(func,x[i],x[i+1])  
    if round(func(q),4) == 0:
        corn.append(round(q,5))
        print(f"X = {round(q,5)}")
    
X = -7.65062
X = -5.02687
X = -1.33897
X = 2.27306
X = 4.38352
X = 8.03516

# 2. Найти интервалы, на которых функция возрастает или убывает
# Экстремумы
extr = []
for i in range(x.size-2):
    q =  bisection(d1func,x[i],x[i+1])  
    if round(d1func(q),4) == 0:
        extr.append(round(q,5))
        print(f"X = {round(q,5)}")
X = -9.97895
X = -6.83137
X = -4.16778
X = -0.39268
X = 0.45457
X = 1.70061
X = 3.81931
X = 7.00103
X = 9.87715

# Интервалы возрастния и убывания
interval_e = [lhs]
interval_e += extr
interval_e.append(rhs)
for i in range(len(interval_e)-1):
    if func((interval_e[i] + interval_e[i+1])/2) > func(interval_e[i]):
        ans = 'возрастает'
    else:
        ans = 'убывает'
    print(f'На отрезке ({interval_e[i]} < X < {interval_e[i+1]}) функция {ans}')
# На отрезке (-10 < X < -9.97895) функция возрастает
# На отрезке (-9.97895 < X < -6.83137) функция убывает
# На отрезке (-6.83137 < X < -4.16778) функция возрастает
# На отрезке (-4.16778 < X < -0.39268) функция убывает
# На отрезке (-0.39268 < X < 0.45457) функция возрастает
# На отрезке (0.45457 < X < 1.70061) функция убывает
# На отрезке (1.70061 < X < 3.81931) функция возрастает
# На отрезке (3.81931 < X < 7.00103) функция убывает
# На отрезке (7.00103 < X < 9.87715) функция возрастает
# На отрезке (9.87715 < X < 10) функция убывает

# 3. Построить график
plt.plot(x,y)
ax = plt.gca() 
ax.axhline(y=0, color='r')    
ax.axvline(x=0, color='r');

# 4. Вычислить вершину
h_extr = max(extr, key=func)
l_extr = min(extr, key=func)
print(f'Набольшая вершина на отрезке ({lhs} < X < {rhs}):\nточка с координатами:\nX = {h_extr}\nY = {round(func(h_extr),5)}')
print(f'Наименьшая вершина на отрезке ({lhs} < X < {rhs}):\nточка с координатами:\nX = {l_extr}\nY = {round(func(l_extr),5)}')

# Набольшая вершина на отрезке (-10 < X < 10):
# точка с координатами:
# X = -9.97895
# Y = 107678.04164
# Наименьшая вершина на отрезке (-10 < X < 10):
# точка с координатами:
# X = 7.00103
# Y = -25610.50968

# 5. Определить промежутки, на котором f > 0 или f < 0
interval_c = [lhs]
interval_c += corn
interval_c.append(rhs)
for i in range(len(interval_c)-1):
    if func((interval_c[i] + interval_c[i+1])/2) > 0:
        ans = 'f > 0'
    else:
        ans = 'f < 0'
    print(f'На отрезке ({interval_c[i]} < X < {interval_c[i+1]}) функция {ans}')

# На отрезке (-10 < X < -7.65062) функция f > 0
# На отрезке (-7.65062 < X < -5.02687) функция f < 0
# На отрезке (-5.02687 < X < -1.33897) функция f > 0
# На отрезке (-1.33897 < X < 2.27306) функция f < 0
# На отрезке (2.27306 < X < 4.38352) функция f > 0
# На отрезке (4.38352 < X < 8.03516) функция f < 0
# На отрезке (8.03516 < X < 10) функция f > 0