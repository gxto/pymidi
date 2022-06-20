# -*- coding: utf-8 -*-
"""
用于查找midi音乐的周期
这个周期可能是变动的
"""
import DY_plot_0 as Dplot




def get_cycle(list_1D):
    list_diff=[]
    for i in range(len(list_1D)-1):
        list_diff.append(list_1D[i+1]-list_1D[i])
    print("输出diff序列",list_diff)
    Dplot.plot_broken("diff序列",list_diff)
        
    




if __name__ == '__main__':
    a=[1,2,3,4,5]
    get_cycle(a)
    