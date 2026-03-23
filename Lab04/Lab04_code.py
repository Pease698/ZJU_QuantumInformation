import numpy as np

# 定义裁判可能给出的问题组合(r, s)，共四种
questions = [(0, 0), (0, 1), (1, 0), (1, 1)]

# 使用字典定义玩家的经典“确定性策略”空间，根据收到问题给出对应答案
strategies = [
    {0: 0, 1: 0},
    {0: 0, 1: 1},
    {0: 1, 1: 0},
    {0: 1, 1: 1}
]

max_win_rate = 0.0

# 模拟所有可能的策略组合，两人分别有四种策略，共 16 种
for alice_strategy in strategies:
    for bob_strategy in strategies:
        wins = 0
        
        for r, s in questions:
            a = alice_strategy[r]
            b = bob_strategy[s]
            
            if (a ^ b) == (r & s):
                wins += 1
                
        win_rate = wins / len(questions)
        
        if win_rate > max_win_rate:
            max_win_rate = win_rate

print(f"模拟 16 种经典策略组合")
print(f"最高胜率: {max_win_rate * 100}%")

