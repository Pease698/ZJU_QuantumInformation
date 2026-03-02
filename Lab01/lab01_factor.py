"""
This is a simple program for lab01 factoring decision problem
"""

import random

max_num = 100   # you can set this to a larger number for more challenging cases

def factoring_decision(m, l): 
    assert l < m 
    
    for i in range(2, l):
        if m % i == 0:
            return True
    
    return False
     
if __name__ == '__main__':
    m = random.randint(2, max_num)
    l = random.randint(2, m - 1)
    print(f'm = {m}, l = {l}')

    print(f'factoring_decision({m}, {l}) = {factoring_decision(m, l)}')

