from sympy import*
from itertools import product
AC = 4
BD = AC
DO = BO = 1/2*BD
AO = CO = 1/2*AC
CE = DO
DE = CO
CDOCE = CO+DO+DE+CE
C = [4, 8, 12, 16]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if CDOCE==C[i]:
        print(f"1、{choice[i]}")
        break
ACD = 45
ACP = DCP = 1/2*ACD
ang = [22.5, 25, 30, 45]
for i in range(4):
    if ACP==ang[i]:
        print(f"2、{choice[i]}")
        break
AB = 4
AC = 2*AB
print(f"3、{AC}")
AB = AC = 2*sqrt(5)
BC = 8
AD = BD = 1/2*AB
BE = CE = 1/2*BC
EO = BO = 1/2*BE
DO = sqrt(BD**2-BO**2)
DF = 2*DO
S = 1/2*BE*DF
print(f"4、{S}")
B = Point(0, 0) # 以B为原点建立平面直角坐标系
D = Point(1, 1) # 正方形ABCD的边长等于1
E = Point(Rational(1, 2), sqrt(3)/2) # △BCE是正三角形
S = Polygon(B, D, E).area
print(f"7、{S}")
x = Symbol("x")
AB = AG = FG = 1
AF = sqrt(2)
FH = x
GH = FG-x
# 角平分线定理: 
# 在△ABC中, AD平分∠BAC
# 则AB/BD=AC/CD
res = solve(AG/GH-AF/FH)[0]
print(f"8、{res}")
print("9、")
red = 3
blue = 2
total = red+blue
print(f"  (1){red/total}")
balls = ["R1", "R2", "R3", "B1", "B2"]
comb = list(product(balls, repeat=2))
avail = [i for i in comb if not i[0]==i[1]]
counter = 0
for i in avail:
    if i[0][0]!=i[1][0]:
        counter+=1
total = len(avail)
win = counter/total
lose = 1-win
print("  (2)公平" if win==lose else "  (2)不公平")
print(f"10、")
x1, x2 = solve((x+2)**2-4, x)
print(f"  (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2-4*x+2, x)
print(f"  (2)x1={x1} x2={x2}")
res = solve(x**2-1+2*(x+1), x)[0]
print(f"  (3)x1=x2={res}")
x1, x2 = solve(2*x**2-3*x+1, x)
print(f"  (4)x1={x1} x2={x2}")
print("11、")
# 以C为原点建立平面直角坐标系
A = Point(9, 3*sqrt(3))
B = Point(6, 0)
C = Point(0, 0)
D = Point(3, 3*sqrt(3))
c = Circle(D, 2*sqrt(7)) # 以D为圆心画一个半径为2√7的圆c
sol_M = c.intersection(Line(B, C))
M = sol_M[0] if sol_M[0].x<sol_M[1].x else sol_M[1] # c与BC的左侧交点为M
sol_N = c.intersection(Line(A, B))
N = sol_N[0] if sol_N[0].x<sol_N[1].x else sol_N[1] # c与AB的左下方交点为N
S = Polygon(A, D, N).area
print(f"  (2){S}")
