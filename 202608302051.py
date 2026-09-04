import sympy as sp
import numpy as np
import rich
from itertools import product

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

expr = "4x^2-x+2"
a, right_part = expr.split("x^2")
linear, constant = right_part.split("x")
if linear=="-":
    b = "-1"
c = constant.split("+")[1]
res = [a, b, c]
coeff = [["4", "-1", "-1"], ["4", "-1", "2"], ["4", "1", "-2"], ["1", "-1", "2"]]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if res==coeff[i]:
        print(f"3、{choice[i]}")
        break
C = 20
a = C/4
x = sp.Symbol("x")
sol = sp.solve(25*x**2-a**2, x)[0]
l1, l2 = sol*8, sol*6
S = 1/2*l1*l2
A = [12.0, 96.0, 48.0, 24.0]
for i in range(4):
    if S==A[i]:
        print(f"4、{choice[i]}")
        break
D = (1, 3)
DO = sp.sqrt(D[0]**2+D[1]**2)
CE = DO
l = [3, 2*sp.sqrt(2), sp.sqrt(10), 4]
for i in range(4):
    if CE==l[i]:
        print(f"8、{choice[i]}")
        break
x1, x2 = sp.solve(x**2-3*x, x)
print(f"9、x1={x1} x2={x2}")
width = sp.solve((30-x)*(20-x)-551, x)
res = [i for i in width if 0<i<20][0]
print(f"12、{res}")
data = [0.64, 0.59, 0.63, 0.63, 0.60, 0.61, 0.61]
val = round(sum(data)/len(data), 1)

print(f"13、{val}")
# 以C为原点建立平面直角坐标系
A = sp.Point(0, 3) # AC=3
B = sp.Point(4, 0) # BC=4
C = sp.Point(0, 0)
D = sp.Point(x, sp.Rational(-3, 4)*x+3) # D(x,-3/4x+3)
E = sp.Point(0, D.y) # E(0,-3/4x+3)
F = sp.Point(D.x, 0) # F(x,0)
f = E.distance(F) # 注意到f(x)=√(x^2+(3-3/4x)^2)
# f'(x)=(25/16x-9/4)/√(x^2+(3-3/4x)^2)
min_point = sp.solve(sp.diff(f, x), x)[0] # 当x=36/25时, f'(x)=0
min_val = f.subs(x, min_point) #∴min(f(x))=12/5
print(f"14、{min_val}")

plt.scatter(0, 1.5, s=100, c="black")
plt.text(0, 1.5, "A", fontsize=24)
plt.scatter(0, 0, s=100, c="black")
plt.text(0, 0, "B", fontsize=24)
plt.scatter(3, 0, s=100, c="black")
plt.text(3, 0, "C", fontsize=24)
plt.scatter(2, 1.5, s=100, c="black")
plt.text(2, 1.5, "D", fontsize=24)
plt.plot([0, 0], [1.5, 0], 'k-', linewidth=2)
plt.plot([0, 3], [0, 0], 'k-', linewidth=2)
plt.plot([3, 2], [0, 1.5], 'k-', linewidth=2)
plt.plot([2, 0], [1.5, 1.5], 'k-', linewidth=2)
plt.plot([0, 2], [0, 1.5], 'b-', linewidth=2)
c1 = Circle((0, 0), 2.5, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c1)
c2 = Circle((2, 1.5), 2.5, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c2)
plt.plot([1-3*np.sqrt(3)/4, 1+3*np.sqrt(3)/4], [(2.25+3*np.sqrt(3))/3, (2.25-3*np.sqrt(3))/3], 'b-', linewidth=2)
plt.scatter(7/16, 1.5, s=100, c="black")
plt.text(7/16, 1.5, "E", fontsize=24)
plt.scatter(25/16, 0, s=100, c="black")
plt.text(25/16, 0, "F", fontsize=24)
plt.plot([0, 7/16], [0, 1.5], 'b-', linewidth=2)
plt.plot([25/16, 2], [0, 1.5], 'b-', linewidth=2)
plt.xlim(-1, 4)
plt.ylim(-1, 2.5)
plt.gca().set_aspect('equal')
plt.savefig("beginning-T15.png")
plt.close()
rich.print("[dim white]Picture generated: ./beginning-T15.png[/dim white]")
print("16、")
x1, x2 = sp.solve(x**2-4*x+3, x)
print(f"  (1)x1={x1} x2={x2}")
x1, x2 = sp.solve(2*x**2-3*x-1, x)
print(f"  (2)x1={x1} x2={x2}")
x1, x2 = sp.solve(2*(x-3)**2-15+5*x)
print(f"  (3)x1={x1} x2={x2}")
print("17、")
print(f"  (1){1/4}")
letter = ["A", "B", "C", "D"]
comb = list(product(letter, repeat=2))
avail = [i for i in comb if i[0]!=i[1]]
counter = 0
for i in avail:
    if 'D' in i:
        counter+=1
print(f"  (2){counter/len(avail)}")
print("19、")
sol = str(sp.factor(x**2+6*x+8))
a, b = sol.split("*")
l, r = a.removeprefix("(").removesuffix(")"), b.removeprefix("(").removesuffix(")")
x1, x2 = l.split("x + ")[1], r.split("x + ")[1]
print(f"  (1){x1};{x2}")
x1, x2 = sp.solve(x**2-3*x-4, x)
print(f"  (2)x1={x1} x2={x2}")
print("20、")
k, b = sp.symbols("k b")
eq1 = 40*k+b-600
eq2 = 45*k+b-550
f = sp.solve([eq1, eq2], [k, b])
print(f"  (1)y={f[k]}x+{f[b]}")
sol = sp.solve((x-30)*(f[k]*x+f[b])-10000, x)
price = [i for i in sol if 30<i<=70][0]
print(f"  (2){price}")
print("21、")
expr = "x^2-4x+5"
l, r = expr.split("x^2")
b, c = r.split("x")
linear, constant = float(b), float(c)
h = linear/2
k = constant-h**2
print(f"  (1){h};{k}")

expr1 = 2*x**2-1
expr2 = 4*x-3
f = expr1-expr2 # f(x)=2x^2-4x+2
min_point = sp.solve(sp.diff(f, x), x)[0] # f'(x)=4x-4
min_val = f.subs(x, min_point) # 当x=1时, f'(x)=0
if min_val>0:
    print("  (2)2x^2-1>4x-3")
if min_val==0:
    print("  (2)2x^2-1≥4x-3")
if min_val<0:
    print("  (2)2x^2-1<4x-3")

print("22、")
BP = 2*x
BQ = 4*x
AB = 12
BC = 24
SBPQ = BP*BQ/2
SABC = AB*BC/2
y = SABC-SBPQ
print(f"  (1)y={y}")
print(f"  (2)0≤x<{12/2}")
x = sp.Symbol("x", real=True)
sol = sp.solve(y-172, x)
print("  (3)不能" if len(sol)==0 else f"  (3){sol}")
