
### dropout 实现

import numpy as np

def dropout(x, p):
    remain = 1 - p
    is_active = np.random.binomial(1, p=remain, size=*x)
    x *= is_active
    x /= remain
    return x
