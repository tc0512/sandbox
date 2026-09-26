import sympy as sp
import numpy as np
import rich

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

m = sp.Symbol("m", real=True)
a = m - 1
b = 2
c = -1
delta = b**2-4*a*c
domain = sp.solve((delta>0), m)
print(f"3、{domain}")
a, b, c = sp.symbols("a b c", positive=True)
B = sp.Point(0, 0) # 以B为原点建立平面直角坐标系
A = sp.Point(0, a)
C = sp.Point(b, 0)
D = sp.Point(b, a)
P = sp.Point(c, (a*b-a*c)/b) # 点P是矩形ABCD的对角线AC上一点
E = sp.Point(0, P.y)
F = sp.Point(b, P.y)
f1 = A.distance(E)-2
f2 = P.distance(F)-8
a, b, c = sp.solve([f1, f2], [a, b, c])[-1]
S = sp.simplify((a*b-a*c)/b*c/2+8*2/2)
print(f"4、{S}")
B = sp.Point(0, 0) # 以B为原点建立平面直角坐标系
A = sp.Point(0, 5) # 正方形ABCD的边长为5
C = sp.Point(5, 0)
D = sp.Point(5, 5)
E = sp.Point(2, 5) # AE=2
F = sp.Point(5, 3) # DF=2
G = sp.Line(B, E).intersection(sp.Line(A, F))[0] # BE与AF相交于点G
H = sp.Point(sp.Rational(5, 2), sp.Rational(3, 2)) # 点H为BF的中点
print(f"6、{G.distance(H)}")
x = sp.Symbol("x")
B = sp.Point(0, 0) # 以B为原点建立平面直角坐标系
A = sp.Point(sp.Rational(9, 5), sp.Rational(12, 5)) # AB=3
C = sp.Point(5, 0)
P = sp.Point(x, 0) # P为边BC上一动点
E = sp.Point(sp.Rational(9, 25)*x, sp.Rational(12, 25)*x) # PE垂直于AB于点E
F = sp.Point((16*x+45)/25, (60-12*x)/25) # PF垂直于AC于点F
M = sp.Point((E.x+F.x)/2, (E.y+F.y)/2) # M为EF中点
f = sp.expand(A.distance(M)) # f(x)=√(1/4x^2-9/10x+9/4)
zero_point = sp.solve(sp.diff(f, x), x)[0] # 令f'(x)=0, 则x=9/5
min_val = f.subs(x, zero_point)
print(f"8、{min_val}")

plt.plot([0, 3, 0, 0], [0, 0, 2, 0], 'k-', linewidth=2)
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.gca().set_aspect('equal')
plt.savefig("week4-T9.png")
plt.close()
rich.print("[dim white]Picture generated: ./week4-T9.png[/dim white]")
