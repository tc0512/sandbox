from sympy import*
x, m = symbols("x m")
res = solve((x+1)**2-m, x)
sol = [[m - 1], [sqrt(m) - 1], [-m - 1, m - 1], [-sqrt(m) - 1, sqrt(m) - 1]]
choice = ["A", "B", "C", "D"]
for i in range(4):
    if res==sol[i]:
        print(f"1、{choice[i]}")
        break
expr = "x^2-8x-20"
l, r = expr.split("x^2")
linear, constant = r.split("x")
b, c = int(linear), int(constant)
h = b/2
k = h**2-c
res = [h, k]
changed = [[4, 24], [8, 44], [4, 36], [-4, 36]]
for i in range(4):
    if res==changed[i]:
        print(f"2、{choice[i]}")
        break
x1, x2 = solve(2*x**2-8*x+7, x)
c = simplify(sqrt(x1**2+x2**2))
l = [sqrt(3), 3, 6, 9]
for i in range(4):
    if c==l[i]:
        print(f"3、{choice[i]}")
        break
res = solve((x**2-5*x-6)/(x+1), x)
sol = [[6], [-1, 6], [-1], [-6]]
for i in range(4):
    if res==sol[i]:
        print(f"4、{choice[i]}")
        break
a = Symbol("a", real=True)
domain = solve((a-1>=0), a)
print(f"6、{domain}")
sol = solve(x*(x-4)-5, x)
res = [i for i in sol if i>=0][0]
print(f"7、{res}")
print("9、")
x1, x2 = solve(x**2+4*x-4, x)
print(f"  (1)x1={x1} x2={x2}")
x1, x2 = solve(2*x**2-4*x+1, x)
print(f"  (2)x1={x1} x2={x2}")
x1, x2 = solve(3*x**2-2*x-3, x)
print(f"  (3)x1={x1} x2={x2}")
x1, x2 = solve(x**2+4*x-7, x)
print(f"  (4)x1={x1} x2={x2}")
res = solve(x**2-13*x+12+4*x**2-18, x)
print(f"10、{res}")
print("12、")
x1, x2, x3, x4 = solve(x**4-5*x**2+4, x)
print(f"【探索】x1={x1} x2={x2} x3={x3} x4={x4}")
x = Symbol("x", real=True)
x1, x2 = solve((x**2-2*x)**2+(x**2-2*x)-6, x)
print(f"【应用】x1={x1} x2={x2}")
