import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 906914964  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pv = ttest_ind(x, y, equal_var=False).pvalue
    res = False
    if pv < 0.06:
      res = True
    return res # Ваш ответ, True или False
