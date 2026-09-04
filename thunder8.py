from sympy import symbols, sqrt, diff, solve, simplify

# 定义变量
x, y, z, lam = symbols('x y z lam', real=True)

# p 和 q
p = (4*x**2*z**2 + 16*x*z**2 - 4*x**3*z - 16*x**2*z - 16*x*z
     + x**4 + 4*x**3 + 4*x**2 + 4*y**2*z**2 + x**2*y**2
     + 4*y**2 - 4*x*y**2*z + 4*x*y**2 - 8*x**2*z)

q = (4*x**2*z**2 + 16*x*z**2 + 16*z**2 + x**4 - 6*x**3
     + 16*x**2 + 24*x + 16 - 2*x**3*z + 4*x**2*z - 24*x*z
     - 16*z + 4*y**2*z**2 + 4*x**2*y**2 + 16*y**2
     - 4*x*y**2*z + 8*x*y**2 - 8*y**2*z)

# 目标函数
f = (sqrt(p) + sqrt(q)) / (2*x + 4)

# 约束
g = sqrt(x**2 + y**2) - 2

# 拉格朗日函数
L = f + lam * g

# 梯度（4 个方程）
grad = [diff(L, var) for var in (x, y, z, lam)]

# 打印梯度方程
print("梯度方程组：")
for i, eq in enumerate(grad):
    print(f"∂L/∂{['x','y','z','λ'][i]} = {simplify(eq)}")
    print()

# 求解
print("求解中...")
sol = solve(grad, (x, y, z, lam))
print("解：", sol)
