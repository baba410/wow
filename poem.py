# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import choice
from numpy.random import randint
words='''輕輕的
我走了
正如
來
招手
作別
西天的
雲彩
河畔的
金柳
夕陽中的
新娘
波光裡的
艷影
心頭
蕩漾
軟泥
青荇
悠悠的
在水底招搖
康河
柔波
水草
榆蔭
清泉
天上虹
揉碎
浮藻
沉澱
彩虹似的夢
'''
phrase=words.split('\n')
n=randint(3,6)

for i in range(n):
    k=randint(5,8)
    egg=choice(phrase,k)
    ham=' '.join(egg)
    print(ham)
