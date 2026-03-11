import numpy as np
import matplotlib.pyplot as plt

# 生成自变量 ζ 的采样点（从 0 到 π/2，共 1000 个点）
zeta = np.linspace(0, np.pi/2, 1000)

# 计算对应的函数值 P(ζ)
P = (2 + np.sqrt(2) * np.sin(2*zeta + np.pi/4)) / 4

# 绘制原始曲线
plt.plot(zeta, P, linewidth=2, color='b', label=r'$P(\zeta)$')

# 添加水平基准线 P = 0.75
plt.axhline(y=0.75, color='r', linestyle='--', linewidth=2, label=r'$P=0.75$')

# 添加标签和标题（支持 LaTeX 格式的数学表达式）
plt.xlabel(r'$\zeta$', fontsize=12)
plt.ylabel(r'$P(\zeta)$', fontsize=12)
plt.title(r'Plot of $P(\zeta)=\frac{2+\sqrt{2}\sin(2\zeta+\frac{\pi}{4})}{4}$ with baseline $P=0.75$', fontsize=14)

# 显示网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(fontsize=12)

# 显示图形
plt.show()