from sympy import*

# 定义变量
x, y, z, w = symbols('x y z w', real=True)
l1, l2, l3 = symbols('lambda1 lambda2 lambda3', real=True)

# 目标函数
f = (48 + x*w - w*z - x*y + y*z) / 2

# 约束函数
g1 = sqrt(36 - 12*x + x**2 + w**2) - sqrt(x**2 + y**2)
g2 = sqrt(36 - 12*x + x**2 + w**2) - sqrt(100 - 16*w + w**2 - 12*z + z**2)
g3 = sqrt(36 - 12*x + x**2 + w**2) - sqrt(64 - 16*y + y**2 + z**2)

# 拉格朗日函数
L = f + l1*g1 + l2*g2 + l3*g3

# 7 个偏导
vars_ = [x, y, z, w, l1, l2, l3]
grad = [diff(L, var) for var in vars_]

print(solve(grad, vars_))
