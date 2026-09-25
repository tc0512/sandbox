import sympy as sp
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
