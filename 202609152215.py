from itertools import product
import sympy as sp
import rich
import numpy as np

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

a, b = sp.symbols("a b")
x1, x2 = -1, 1
y1, y2 = -26, -2
eq1 = a*x1**2+b*x1-15-y1
eq2 = a*x2**2+b*x2-15-y2
sol_ab = sp.solve([eq1, eq2], [a, b])
val_a, val_b = sol_ab[a], sol_ab[b]
x = sp.Symbol("x")
val_x = float(sp.solve(val_a*x**2+val_b*x-14, x)[0])
cond = [-1<val_x<1, 1<val_x<1.1, 1.1<val_x<1.2, -0.59<val_x<0.84]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if cond[i]:
        print(f"2、{choice[i]}")
        break
AC = 10
BD = AC
AO, DO = sp.Rational(1, 2)*AC, sp.Rational(1, 2)*BD
AE = sp.Rational(1, 2)*BD
EO = sp.sqrt(AE**2+AO**2)
DE = EO-DO
l = [2, 5*sp.sqrt(2)-5, 10-5*sp.sqrt(2), 10*sp.sqrt(2)-10]
for i in range(4):
    if DE==l[i]:
        print(f"4、{choice[i]}")
        break
a, b = sp.solve(x**2-3*x+1, x)
print(f"5、{sp.simplify(1/a+1/b)}")
k = sp.Symbol("k", real=True)
a = k
b = 1-2*k
c = k-2
domain = str(sp.solve(b**2-4*a*c>=0, k))
res = "("+domain+") & (k != 0)"
print(f"6、{res}")
data = {"摸球次数": [50, 100, 200, 500, 800, 1000], "摸到红球的频数": [11, 27, 50, 124, 201, 249], "摸到红球的频率": [0.22, 0.27, 0.25, 0.248, 0.251, 0.249]}
max_index = data["摸球次数"].index(max(data["摸球次数"]))
frequency = data["摸到红球的频率"][max_index]
res = int(round(40*frequency, 0))
print(f"7、{res}")
AC = BD = 7
res = AC**2
print(f"8、{res}")
data1 = ["R1", "R2", "R3", "B1", "B2", "B3"]
data2 = ["R1", "R2", "B1", "B2", "B3", "B4"]
comb = list(product(data1, data2))
avail = [i for i in comb if i[0][0]!=i[1][0]]
print(f"9、{len(avail)/len(comb)}")
# 以B为原点建立平面直角坐标系
A = sp.Point(4, 4*sp.sqrt(3)) # ∠ABC=60度
B = sp.Point(0, 0)
C = sp.Point(8, 0)
D = sp.Point(12, 4*sp.sqrt(3))
E = sp.Point(2, 0) # BE=2
F = sp.Point(x, sp.sqrt(3)/3*x) # F是BD上一动点
f = sp.expand(E.distance(F)+C.distance(F)) # f(x)=√(4*x^2/3-16x+64)+√(4x^2/3-4x+4)
zero_point = sp.solve(sp.diff(f, x), x) # 令f'(x)=0, 则x=12/5
min_val = f.subs(x, zero_point[0]) # 当x=12/5时, f有最小值2√13
print(f"10、{min_val}")

plt.plot([2, 0], [2, 0], 'k-', linewidth=2)
plt.plot([0, 3], [0, 0], 'k-', linewidth=2)
plt.plot([2, 3], [2, 0], 'k-', linewidth=2)
plt.scatter(2, 2, s=100, c='black')
plt.scatter(0, 0, s=100, c='black')
plt.scatter(3, 0, s=100, c='black')
plt.text(2, 2, "A", fontsize=24)
plt.text(0, 0, "B", fontsize=24)
plt.text(3, 0, "C", fontsize=24)
c1 = Circle((2, 2), 1, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c1)
c2 = Circle(((4-np.sqrt(2))/2, (4-np.sqrt(2))/2), 1, fill=False, edgecolor='blue', linewidth=2)
c3 = Circle(((10+np.sqrt(5))/5, (10-2*np.sqrt(5))/5), 1, fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c2)
plt.gca().add_patch(c3)
plt.plot([(-5*np.sqrt(2)+14*np.sqrt(5))/(5*np.sqrt(2)+4*np.sqrt(5)), 2], [-1, 2], 'b-', linewidth=2)
plt.scatter(12*np.sqrt(5)/(5*np.sqrt(2)+4*np.sqrt(5)), 0, s=100, c='blue')
plt.text(12*np.sqrt(5)/(5*np.sqrt(2)+4*np.sqrt(5)), 0, "E", fontsize=24)
c4 = Circle((2, 2), 4*np.sqrt(5*np.sqrt(10)+50)/(5*np.sqrt(2)+4*np.sqrt(5)), fill=False, edgecolor='blue', linewidth=2)
c5 = Circle((12*np.sqrt(5)/(5*np.sqrt(2)+4*np.sqrt(5)), 0), 4*np.sqrt(5*np.sqrt(10)+50)/(5*np.sqrt(2)+4*np.sqrt(5)), fill=False, edgecolor='blue', linewidth=2)
plt.gca().add_patch(c4)
plt.gca().add_patch(c5)
plt.plot([(-np.sqrt(10)-3)*(np.sqrt(3)*np.sqrt(19-6*np.sqrt(10))+1)+8, (-np.sqrt(10)-3)*(-np.sqrt(3)*np.sqrt(19-6*np.sqrt(10))+1)+8], [np.sqrt(3)*np.sqrt(19-6*np.sqrt(10))+1, -np.sqrt(3)*np.sqrt(19-6*np.sqrt(10))+1], 'b-', linewidth=2)
plt.scatter(16/3-4*np.sqrt(10)/3, 16/3-4*np.sqrt(10)/3, s=100, c='blue')
plt.text(16/3-4*np.sqrt(10)/3, 16/3-4*np.sqrt(10)/3, "D", fontsize=24)
plt.scatter(14/3-2*np.sqrt(10)/3, -10/3+4*np.sqrt(10)/3, s=100, c='blue')
plt.text(14/3-2*np.sqrt(10)/3, -10/3+4*np.sqrt(10)/3, "F", fontsize=24)
plt.plot([16/3-4*np.sqrt(10)/3, 12*np.sqrt(5)/(5*np.sqrt(2)+4*np.sqrt(5))], [16/3-4*np.sqrt(10)/3, 0], 'b-', linewidth=2)
plt.plot([12*np.sqrt(5)/(5*np.sqrt(2)+4*np.sqrt(5)), 14/3-2*np.sqrt(10)/3], [0, -10/3+4*np.sqrt(10)/3], 'b-', linewidth=2)
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.gca().set_aspect('equal')
plt.savefig("week3-T11.png")
plt.close()
rich.print("[dim white]Picture generated: ./week3-T11.png[/dim white]")
print("12、")
