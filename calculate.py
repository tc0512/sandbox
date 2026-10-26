from sympy import*
a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2, f2, x, y = symbols("a1 b1 c1 d1 e1 f1 a2 b2 c2 d2 e2 f2 x y")
eq1 = a1*x**2+b1*x*y+c1*y**2+d1*x+e1*y+f1
eq2 = a2*x**2+b2*x*y+c2*y**2+d2*x+e2*y+f2
print(solve([eq1, eq2], [x, y]))
