import math
import re
from decimal import Decimal
from sympy import*
print("第一章")
print("  1课时1")
print("    考点1")
BA = AD = 4.1
BM = 4
AM = math.sqrt(BA**2-BM**2)
MD = AD-AM
print(f"      变式: {MD}")
print("    考点2")
AB = 1
CD = AB
CM = CD
print(f"      变式: {CM}")
print("    考点3")
CAD = 45
F = (180-CAD)/2
print(f"      变式: {F}")
print("  2课时1")
print("    考点1")
C = (3, 4)
CO = math.sqrt(C[0]**2+C[1]**2)
A = (CO, 0)
B = (A[0]+C[0], C[1])
res = [A, B]
item = [[(4, 0), (7, 4)], [(4, 0), (8, 4)], [(5, 0), (7, 4)], [(5, 0), (8, 4)]]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if item[i]==res:
        print(f"      变式: {choice[i]}")
        break
print("    考点2")
AC = 6
BD = 8
AO = CO = 1/2*AC
BO = DO = 1/2*BD
a = math.sqrt(AO**2+BO**2)
S = 1/2*AC*BD
print(f"      典例: {a};{S}")
ang1 = 35
ABD = 90-ang1
ang2 = ABD
deg = [65, 55, 45, 35]
for i in range(4):
    if deg[i]==ang2:
        print(f"      变式: {choice[i]}")
        break
print("  2课时2")
print("    考点3")
A = 44
C = A
CBD = (180-C)/2
deg = [64, 66, 68, 70]
for i in range(4):
    if deg[i]==CBD:
        print(f"      典例: {choice[i]}")
        break
CE = 2
S = 8
BF = Rational(2*S, CE)
a, b = Rational(1, 2)*BF, Rational(1, 2)*CE
a = sqrt(a**2+b**2)
C = 4*a
print(f"      变式: {C}")
print("  3课时1")
print("    考点1")
DAE = 45
ang1 = 25
EAC = DAE-ang1
deg = [15, 20, 25, 30]
for i in range(4):
    if deg[i]==EAC:
        print(f"      变式: {choice[i]}")
        break
print("    考点2")
ADB = 28
CAD = ADB
AOB = ADB+CAD
deg = [52, 54, 56, 58]
for i in range(4):
    if deg[i]==AOB:
        print(f"      典例: {choice[i]}")
        break
AB = 6
AC = 10
BD = AC
BC = math.sqrt(AC**2-AB**2)
AD = BC
DE = 1/2*AD
EO = 1/2*AB
DO = 1/2*BD
C = DE+EO+DO
print(f"      变式: {C}")
print("    考点3")
AB = sqrt(10)
BC = 3*sqrt(2)
AC = sqrt(AB**2+BC**2)
BE = 1/2*AC
print(f"      典例: {BE}")
x = Symbol("x")
AD = BC = DE = x
AB = CD = 8
BE = AB/2
CE = BC-BE
res = solve(CE**2+CD**2-DE**2, x)[0]-4
print(f"      变式: {res}")
print("  3课时2")
print("    考点3")
print("      典例")
BAE = 30
BAO = 2*BAE
ABE = 90-BAE
AOE = 180-BAO-ABE
print(f"        (2){AOE}")
HF = 8
EG = HF
print(f"      变式: {EG}")
print("  4课时1")
DCE = 60
BCD = ABC = 90
BCE = BCD-DCE
CBE = (180-BCE)/2
ABE = ABC-CBE
deg = [10, 15, 20, 25]
for i in range(4):
    if deg[i]==ABE:
        print(f"    典例: {choice[i]}")
        break
p_B = Point(0, 0) # 以B为原点建立平面直角坐标系
p_A = Point(0, 3) # AB=3
# 四边形ABCD是正方形
p_C = Point(3, 0)
p_D = Point(3, 3)
a = Symbol("a")
p_E = Point(0, a) # 设BE=a
p_F = Point(3, a-sqrt(3)) # ∠EFD=60
x, y = symbols("x y")
l_EF = Line(p_E, p_F) # √3·x+3y-3a=0
l_EF_eq = l_EF.equation()
# 字符串拆解提取直线表达式A,B,C
expr_str = str(l_EF_eq.expand())
A = 0
B = 0
C = 0
terms = expr_str.replace('-', '+-').split('+')
for term in terms:
    if not term:
        continue
    if 'x' in term and 'y' not in term:
        coeff_part = term.replace('*x', '').replace('x', '').strip()
        if coeff_part == '' or coeff_part == '+':
            A += 1
        elif coeff_part == '-':
            A -= 1
        else:
            A += sympify(coeff_part)
    elif 'y' in term and 'x' not in term:
        coeff_part = term.replace('*y', '').replace('y', '').strip()
        if coeff_part == '' or coeff_part == '+':
            B += 1
        elif coeff_part == '-':
            B -= 1
        else:
            B += sympify(coeff_part)
    else:
        if term:
            C += sympify(term)
x0, y0 = p_B.x, p_B.y
# 点关于直线对称反射公式
# x'=x0-2A(Ax0+By+C)/(A^2+B^2)
# y'=y0-2B(Ax0+By+C)/(A^2+B^2)
x1 = x0-2*A*(A*x0+B*y0+C)/(A**2+B**2)
y1 = y0-2*B*(A*x0+B*y0+C)/(A**2+B**2)
p_B1 = Point(x1, y1) # B'(√3·a/2,3a/2)
x0, y0 = p_C.x, p_C.y # C'((3+√3·a)/2,(3a-3√3)/2)
x1 = x0-2*A*(A*x0+B*y0+C)/(A**2+B**2)
y1 = y0-2*B*(A*x0+B*y0+C)/(A**2+B**2)
p_C1 = Point(x1, y1)
res = solve(p_B1.y-3, a)[0]
print(f"    变式2: {res}")
print("  4课时2")
print("    变式")
AB = 7
AE = BF = 3
BE = AB-AE
a = math.sqrt(BE**2+BF**2)
C = 4*a
print(f"      (2){C}")
print("第二章")
print("  1课时1")
print("    考点1")
m = Symbol("m", real=True)
eq = abs(m+1)-2
sol = solve(eq, m)
res = [i for i in sol if i-1!=0]
print(f"      变式: {res}")
print("    考点2")
eq = (x+3)**2-3*x-5*x**2
simplified = simplify(eq)
quadratic = str(simplified).split("*x**2")[0]
if float(quadratic)<0:
    simplified = -simplified
linear = str(simplified).split("*x**2")[1].split("*x")[0]
print(f"      典例: {simplified};{linear}")
eq = x*(-x+1)-3
simplified = simplify(eq)
quadratic = str(simplified).split("x**2")[0]
if quadratic!="":
    simplified = -simplified
linear = str(simplified).split("x**2")[1].split("x")[0]
if linear.strip()=="-":
    linear = -1
coeff = [1, -1, 3, -3]
for i in range(4):
    if coeff[i]==linear:
        print(f"      变式: {choice[i]}")
        break
print("  1课时2")
print("    考点1")
x = 2
a = Symbol("a")
res = solve(x**2-a*x+6, a)[0]
val = [2, 3, 12, 5]
for i in range(4):
    if coeff[i]==linear:
        print(f"      典例: {choice[i]}")
        break
x = Symbol("x")
sol = solve(x**2-3*x+1, x)
val = [simplify(2025-m**2+3*m) for m in sol]
print(f"      变式: {val}")
print("    考点2")
sol = solve(x**2-3*x-5, x)
x1, x2 = float(sol[0]), float(sol[1])
domains = [
    (-3<x1<-2 and 4<x2<5),
    (-3<x1<-1 and 5<x2<6),
    (-3<x1<-2 and 5<x2<6),
    (-2<x1<-1 and 4<x2<5),
]
for i in range(4):
    if domains[i]:
        print(f"      典例: {choice[i]}")
        break
print("      变式")
f = lambda x: x**2-7*x+9
num = nsolve(f(x), x, 2)
print(f"""        (1)+--------+--+-+-+--+
           |    x   |-1|0|1| 2|
           +--------+--+-+-+--+
           |x^2-7x+9|17|9|{f(1)}|{f(2)}|
           +--------+--+-+-+--+
           {int(num)};{int(num)+1};{Decimal(str(round(num, 1)))-Decimal('0.1')};{round(num, 1)}
        (2)x≈{round(num, 1)}""")
print("  2课时1")
print("    考点1")
print("      典例")
x1, x2 = solve(81*x**2-25)
print(f"        (1)x1={x1} x2={x2}")
y = Symbol("y")
y1, y2 = solve((y-5)**2-64)
print(f"        (2)y1={y1} y2={y2}")
m = Symbol("m", real=True)
res = str(solve((m-1>=0), m))
domains = ["1 <= m", "1 < m", "-1 < m", "-1 <= m"]
for i in range(4):
    if res==domains[i]:
        print(f"      变式: {choice[i]}")
print("    考点2")
print("      变式")
x1, x2 = solve(x**2+4*x-2, x)
print(f"        (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2-3*x-Rational(7, 4), x)
print(f"        (2)x1={x1} x2={x2}")
print("  2课时2")
print("    典例")
x1, x2 = solve(Rational(1, 2)*x**2-6*x-7, x)
print(f"      (1)x1={x1} x2={x2}")
x1, x2 = solve(2*x**2-4*x-1, x)
print(f"      (2)x1={x1} x2={x2}")
print("    变式2")
x1, x2 = solve(2*x**2+5*x+3, x)
print(f"      (2)x1={x1} x2={x2}")
print("  2课时3")
a, b, c = symbols("a b c")
print(f"    知识点1: {solve(a*x**2+b*x+c, x)}")
print("    考点1")
print("      典例")
x1, x2 = solve(x**2+4*x-20, x)
print(f"        (1)x1={x1} x2={x2}")
x1, x2 = solve(3*x*(x+1)-2*x-2, x)
print(f"        (2)x1={x1} x2={x2}")
print("    考点2")
print("      典例")
x = -2
res = solve(x**2-m*x+m-3, m)[0]
print(f"        (1){res}")
x = Symbol("x", real=True)
sol = solve(x**2+17-8*x, x)
if len(sol)==0:
    print("      变式: 无实数根")
elif sol[0]==sol[1]:
    print("      变式: 有两个相等的实数根")
else:
    print("      变式: 有两个不等的实数根")
print("  2课时4")
print("    考点1")
print("      典例")
x1, x2 = solve(x**2-2026*x, x)
print(f"        (1)x1={x1} x2={x2}")
x1, x2 = solve(x*(x-3)+x-3, x)
print(f"        (2)x1={x1} x2={x2}")
x1, x2 = solve((2*x-1)**2-x**2, x)
print(f"        (3)x1={x1} x2={x2}")
print("      变式")
x1, x2 = solve(x**2-6*x+5, x)
print(f"        (1)x1={x1} x2={x2}")
x1, x2 = solve(6*(x-5)-2*x*(x-5), x)
print(f"        (2)x1={x1} x2={x2}")
print("    考点2")
print("      典例")
x1, x2 = solve(x**2+4*x-1, x)
print(f"        (1)x1={x1} x2={x2}")
x1, x2 = solve(Rational(1, 2)*(x+3)**2-18, x)
print(f"        (2)x1={x1} x2={x2}")
x1, x2 = solve(1-2*x+Rational(1, 2)*(2*x-1)**2, x)
print(f"        (3)x1={x1} x2={x2}")
print("  3课时1")
x1, x2 = solve(a*x**2+b*x+c, x)
print(f"    知识点1: {simplify(x1+x2)};{simplify(x1*x2)}")
print("    知识点2")
print("      1、")
print(f"        ①{simplify(x1**2+x2**2)}")
print(f"        ②{simplify(1/x1+1/x2)}")
print(f"        ③{simplify(x2/x1+x1/x2)}")
print(f"        ④{simplify((x1+1)*(x2+1))}")
print(f"        ⑤{simplify(a*x1**2+b*x1)}")
print(f"        ⑥{simplify(a*x2**2+b*x2)}")
f = a*x**2+b*x+c
print(f"      2、{f.subs(a, 1)}=0")
print("    考点1")
x1, x2 = solve(x**2-4*x+2, x)
res = simplify(x1+x2-x1*x2)
val = [2, 6, -2, 3]
for i in range(4):
    if res==val[i]:
        print(f"      典例: {choice[i]}")
        break
x1, x2 = solve(x**2-2*x-1, x)
res = simplify(1/x1+1/x2)
val = [2, 1, -1, -2]
for i in range(4):
    if res==val[i]:
        print(f"      变式1: {choice[i]}")
        break
m, n = solve(x**2+x-1, x)
res = simplify(m**2-n+2024)
val = [2027, 2026, 2025, 2024]
for i in range(4):
    if res==val[i]:
        print(f"      变式2: {choice[i]}")
        break
print("    考点2")
k = Symbol("k")
a, b, c = 1, k, -1
res = solve(-b/a, k)
val = [[0], [-4], [-4, 4], []]
for i in range(4):
    if res==val[i]:
        print(f"      典例: {choice[i]}")
        break
m, y = symbols("m y")
y1, y2 = solve(y**2-2*(m+1)*y+m**2-2, y)
val = solve(y1+y2+y1*y2, m)
print(f"      变式: {val}")
print("  4课时1")
print("    考点1")
a = solve((30-2*x)*(20-2*x)-200, x)
print(f"      变式2: {[i for i in a if i>0][0]}cm")
print("    考点2")
t = Symbol("t")
AB = 6
BC = 7
BP = 2*t
CQ = t
BQ = BC-CQ
SABC = AB*BC/2
SBPQ = BP*BQ/2
SAPQC = SABC-SBPQ
sol = solve(SAPQC-11)
print(f"      典例: {[i for i in sol if 2*i<AB][0]}")
AB = CD = 16
BC = AD = 6
AP = 3*t
CQ = 2*t
DQ = CD-CQ
a = DQ-AP
b = AD
print(f"      变式: {solve(a**2+b**2-100, t)}")
print("  4课时2")
print("    考点1")
delta = solve(Rational(9, 5)-Rational(5, 4)*(1+x)**2, x)[1]*100
print(f"      典例: {delta}%")
print("      变式")
sol = solve((1+x)**2-64, x)
delta = [i for i in sol if i>0][0]
print(f"        (1){delta}")
sol = (1+7)**3
print(f"        (2){sol>600}")
print("    考点2")
sol = solve((x-40)*(700-10*x)-2000, x)
res = [i for i in sol if 700-10*i<=180]
prices = [[50], [60], [50, 60], [100]]
for i in range(4):
    if res==prices[i]:
        print(f"      典例: {choice[i]}")
        break
sol = solve((58-2*x)*(x-12)-144, x)
price = sol[0] if sol[0]<sol[1] else sol[1]
delta = 25-price
print(f"      变式: {delta}")
print("    考点3")
sol = solve(x*(x+8)-180)
smallest = [i for i in sol if i>0][0]
biggest = smallest+8
print(f"      变式: {biggest};{smallest}")
print("练习1")
x1, x2 = solve(x**2-4*x-2, x)
print(f"  1、x1={x1} x2={x2}")
x1, x2 = solve(2*x**2-x-15, x)
print(f"  2、x1={x1} x2={x2}")
x1, x2 = solve(2*x*(x+3)-6*(x+3), x)
print(f"  3、x1={x1} x2={x2}")
a, b, c = 1, -8, 3*m+1
delta = b**2-4*a*c
val = solve(delta, m)[0]
x = -b/(2*a)
print(f"  4、{val};x1=x2={x}")
print("练习2")
x = Symbol("x")
x1, x2 = solve((x-2)**2-1, x)
print(f"  1、x1={x1} x2={x2}")
x1, x2 = solve(x**2-12*x-5, x)
print(f"  2、x1={x1} x2={x2}")
x1, x2 = solve(x*(x+5)-3, x)
print(f"  3、x1={x1} x2={x2}")
a, b, c = 1, 6, m+2
delta = b**2-4*a*c
val = solve(delta, m)[0]
x = -b/(2*a)
print(f"  4、{val};x1=x2={x}")
print("  5、")
AB = 2*sqrt(10)
EF = 1
BC = DF = 2*EF
AC = sqrt(AB**2-BC**2)
AF = Rational(1, 2)*AC
AD = sqrt(AF**2+DF**2)
print(f"    (2){AD}")
print("练习3")
print("  1、")
a, b, c = 1, -4, 2*m-1
delta = b**2-4*a*c
domain = str(solve(delta>=0, m))
print(f"    (1){domain[13:-1]}")
delta = delta.subs(m, 1)
print(f"    (2)x1={(-b+sqrt(delta))/(2*a)} x2={(-b-sqrt(delta))/(2*a)}")
x = Symbol("x")
x1, x2 = solve((2*x-1)**2-16, x)
print(f"  2、x1={x1} x2={x2}")
x1, x2 = solve(x*(x+4)+5*(x+4), x)
print(f"  3、x1={x1} x2={x2}")
x1, x2 = solve(2*x**2+3*x-1, x)
print(f"  4、x1={x1} x2={x2}")
x1, x2 = solve((x+1)*(x+8)+2, x)
print(f"  5、x1={x1} x2={x2}")
print("  6、")
AB = AC = 5
BC = 6
BE = CE = 1/2*BC
AE = CF = sqrt(AC**2-CE**2)
print(f"    (2){CF}")
print("练习4")
print("  1、")
x1, x2 = solve(x**2-6*x-2, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(3*x*(x-5)-2*(5-x))
print(f"    (2)x1={x1} x2={x2}")
print("  2、")
x1, x2 = solve((x-1)**2-9, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2-6*x-4, x)
print(f"    (2)x1={x1} x2={x2}")
print("练习5")
print("  1、")
x1, x2 = solve(x*(2*x-7)-2*x, x)
print(f"    (1)x1={x1} x2={x2}")
x = solve(4*x**2+9-12*x, x)[0]
print(f"    (2)x1=x2={x}")
x = Symbol("x", real=True)
print("  2、")
x1, x2 = solve(x**2-2*x-5, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(2*x**2-x-2+4*x, x)
print(f"    (2)x1={x1} x2={x2}")
print("  3、")
DF = EG = 5
AC = 8
AE = EO = FO = CF = 1/4*AC
EF = EO+FO
C = 2*(EF+DF)
print(f"    (2){C}")
print("练习6")
print("  1、")
try:
    x1, x2 = solve(3*x**2-5*x+4, x)
    print(f"    (1)x1={x1} x2={x2}")
except Exception:
    print("    (1)无实数解")
m1, m2 = solve((m+1)**2-4*(m+1), m)
print(f"    (1)m1={m1} m2={m2}")
print("  2、")
x1, x2 = solve(x**2+2*x-4, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(2*x*(x-3)+x-3, x)
print(f"    (2)x1={x1} x2={x2}")
print("练习7")
print("  1、")
x1, x2 = solve(4*x**2-8*x+1, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(3*x**2-5*(2*x+1), x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve(x**2-7*x-18, x)
print(f"    (3)x1={x1} x2={x2}")
x = solve(4*x**2+1-4*x, x)[0]
print(f"    (4)x1=x2={x}")
print("  2、")
AB = CD = 5
DN = b = 4
MO = NO = sqrt(CD**2-DN**2)
a = MO+NO
S = a*b
print(f"    (2){S}")
print("练习8")
print("  1、")
x = Symbol("x")
x1, x2 = solve(3*x**2+6*x-1, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(2*x**2-1-4*x, x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve(2*x**2-3*x+1, x)
print(f"    (3)x1={x1} x2={x2}")
x1, x2 = solve(Rational(1, 3)*x**2-4*x+Rational(4, 3), x)
print(f"    (4)x1={x1} x2={x2}")
print("练习9")
print("  1、")
x1, x2 = solve((x-3)**2-49, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2-4*x-9, x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve(3*x*(x-2)-5*(x-2), x)
print(f"    (3)x1={x1} x2={x2}")
x1, x2 = solve(x**2-7*x-44, x)
print(f"    (4)x1={x1} x2={x2}")
print("练习10")
print("  1、")
x1, x2 = solve(x**2+x-6, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve((x+1)**2-6*x-6, x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve(3*x**2-6*x+2, x)
print(f"    (3)x1={x1} x2={x2}")
x1, x2 = solve(4*x**2-6*x, x)
print(f"    (4)x1={x1} x2={x2}")
print("  2、")
C = Point(0, 0) # 以C为原点建立平面直角坐标系
A = Point(0, 4) # 四边形ABCD是菱形, AB=4
B = Point(-2*sqrt(3), 2) # ∠BAD=120度
D = Point(2*sqrt(3), 2)
E = Point(x, -sqrt(3)/3*x) # E在BC上滑动
# A(x1,y1), B(x2,y2), 将线段AB绕A逆时针旋转θ度得AB', B'坐标求解公式
# t=πθ/180
# dx=x2-x1
# dy=y2-y1
# dx'=dx cos t-dy sin t
# dy'=dy sin t-dx cos t
# B'(x1+dx',y1+dy')
theta = 60 # △AEF为正三角形
rad = theta*pi/180 # 角度转弧度公式Rad=πθ/180
dx = E.x-A.x
dy = E.y-A.y
dxp = dx*cos(rad)-dy*sin(rad)
dyp = dx*sin(rad)+dy*cos(rad)
F = Point(A.x+dxp, A.y+dyp)
AECF = simplify(Polygon(A, E, C, F).area)
print(f"    (2){'x' in str(AECF)}")
print("练习11")
print("  1、")
x1, x2 = solve(x**2-3*x, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2-sqrt(3)*x-Rational(1, 4), x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve((2*x+1)**2-(x-1)**2)
print(f"    (3)x1={x1} x2={x2}")
x1, x2 = solve(x**2+2*x+1-4, x)
print(f"    (4)x1={x1} x2={x2}")
print("  2、")
BD = 6
AB = BC = 5
BO = DO = 1/2*BD
AO = math.sqrt(AB**2-BO**2)
OG = AO*BO/AB
BF = 1/2*BC
SOBFE = BF*OG
print(f"    (2){SOBFE}")
print("练习12")
print("  1、")
x1, x2 = solve(2*(x+3)**2-4, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(Rational(1, 4)*(x+1)**2-25, x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve((2*x-1)**2-(3-x)**2)
print(f"    (3)x1={x1} x2={x2}")
x1, x2 = solve(3*x**2-6*x+1, x)
print(f"    (4)x1={x1} x2={x2}")
print("练习13")
print("  1、")
x1, x2 = solve(2*x**2+2*x-1, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(2*(x-3)**2-x**2+9, x)
print(f"    (2)x1={x1} x2={x2}")
x1, x2 = solve(x**2-4*x+3, x)
print(f"  2、x1={x1} x2={x2}")
x1, x2 = solve(x**2+4*x+3, x)
print(f"  3、x1={x1} x2={x2}")
print("练习14")
x1, x2 = solve(2*x**2-4*x-3, x)
print(f"  1、x1={x1} x2={x2}")
x1, x2 = solve((2*x-1)**2-(3-x)**2)
print(f"  2、x1={x1} x2={x2}")
print("  3、")
x1, x2 = solve(x**2-4*x-3, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(3*x*(x-2)-4+2*x, x)
print(f"    (2)x1={x1} x2={x2}")
print("练习15")
print("  1、")
x1, x2 = solve(x**2-5*x-6, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2-4*x+1, x)
print(f"    (1)x1={x1} x2={x2}")
x1, x2 = solve(x**2+2*x-3, x)
print(f"  2、x1={x1} x2={x2}")
x1, x2 = solve(x**2-6*x, x)
print(f"  3、x1={x1} x2={x2}")
