import sympy as sp
import numpy as np
import rich
from itertools import product

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
x = sp.Symbol("x", real=True)
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
plt.scatter([0, 3, 0], [0, 0, 2], s=100, c='black')
plt.text(0, 0, "A", fontsize=24)
plt.text(3, 0, "B", fontsize=24)
plt.text(0, 2, "C", fontsize=24)
c1 = Circle((0, 0), 1, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c1)
c2 = Circle((1, 0), 1, fill=False, edgecolor='blue', linewidth=2)
c3 = Circle((0, 1), 1, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c2)
plt.gca().add_patch(c3)
plt.plot([0, 3], [0, 3], 'b-', linewidth=2)
plt.scatter(1.2, 1.2, s=100, c='blue')
plt.text(1.2, 1.2, "E", fontsize=24)
c4 = Circle((0, 0), 6*np.sqrt(2)/5, fill=False, edgecolor='blue', linewidth=2)
c5 = Circle((1.2, 1.2), 6*np.sqrt(2)/5, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c4)
plt.gca().add_patch(c5)
plt.plot([3/5-3*np.sqrt(3)/5, 3/5+3*np.sqrt(3)/5], [3/5+3*np.sqrt(3)/5, 3/5-3*np.sqrt(3)/5], 'b-', linewidth=2)
plt.scatter(1.2, 0, s=100, c='blue')
plt.text(1.2, 0, "D", fontsize=24)
plt.scatter(0, 1.2, s=100, c='blue')
plt.text(0, 1.2, "F", fontsize=24)
plt.plot([0, 1.2], [1.2, 1.2], 'b-', linewidth=2)
plt.plot([1.2, 1.2], [1.2, 0], 'b-', linewidth=2)
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.gca().set_aspect('equal')
plt.savefig("week4-T9.png")
plt.close()
rich.print("[dim white]Picture generated: ./week4-T9.png[/dim white]")

print("10、")
try:
    x1, x2 = sp.solve(sp.Rational(1, 2)*x-1-2*x**2, x)
    print(f"  (1)x1={x1} x2={x2}")
except Exception:
    print("  (1)无实数根")
x1, x2 = sp.solve(2*x**2-12*x+1, x)
print(f"  (2)x1={x1} x2={x2}")
m = sp.Symbol("m", real=True)
a = m
b = 1-2*m
c = m
delta = b**2-4*a*c
domain = sp.solve((delta>=0), m)
print(f"  (3){domain}")
data1 = ["R", "B"]
data2 = ["R", "B1", "B2"]
comb = list(product(data1, data2))
avail = len([i for i in comb if i[0][0]!=i[1][0]])
total = len(comb)
print(f"11、{avail/total}")
print("12、")
l = [i for i in sp.solve(x*(72-3*x)-384, x) if 72-3*i<=36][0]
print(f"  (2){l}")
print("14、")
percent = [i for i in sp.solve(50*(1+x)**2-72, x) if i>0][0]*100
print(f"  (1){percent}%")
y = sp.Symbol("y")
price = min(sp.solve((y-30)*(900-10*y)-8000, y))
print(f"  (2){price}")
print("16、")
f = x**2-8*x+9 # 令f(x)=x^2-8x+9
zero_point = sp.solve(sp.diff(f, x), x)[0] # 令f'(x)=0, 则x=4
min_val = f.subs(x, zero_point)
print(f"  (1){min_val}")
f1 = 3*x**2-2*x+5
f2 = 2*x**2+4*x-6
f = f1-f2 # f(x)=x^2-6x+11
zero_point = sp.solve(sp.diff(f, x), x)[0] # 令f'(x)=0, 则x=3
min_val = f.subs(x, zero_point)
print("  (2)3x^2-2x+5>2x^2+4x-6" if min_val>0 else "  (2)3x^2-2x+5<2x^2+4x-6")
t = sp.Symbol("t")
AC = 4
BC = 8
AM = t
CN = 2*t
CM = AC-AM
SMCN = CM*CN/2
zero_point = sp.solve(sp.diff(SMCN, t), t)[0]
max_val = SMCN.subs(t, zero_point)
print(f"  (3){zero_point};{max_val}")
