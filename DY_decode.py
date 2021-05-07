# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:55:32 2021

@author: python

作用:
    解码和排序
    主要按照各个的适应度.进行从强到弱的排序.
    为轮盘转法去做筛查依据. 
    也要防止过拟合的问题.
"""

import numpy as np




import DY_cor_0 as Dco







def decode(list_2d,first_window_list,set_fit_num):
    '''
    传入参数1:list_2d,鱼的各个部分的二维数组
    传入参数2:first_window_list,曲子的第一部分
    传入参数3:set_fit_num想要的适应度.(这里是一个数字)
    主要是求取两者的相似度.
    '''
    array_2d=np.array(list_2d)
    # 下面是去重复的行.
    # 参考:https://www.jb51.net/article/155244.htm 
    # 什么哈希之类的...才能排序...
    list_2d=np.array(list(set([tuple(t) for t in array_2d])))
    
    # 求取适应度序列
    fitness_1=[]
    fitness=Dco.cor_mat_A(list_2d,first_window_list)   
    #print("适应度的值:",fitness)
    for i in range(len(fitness)-1):
        sub=fitness[i]-set_fit_num
        if sub<0:
            sub=-sub
        fitness_1.append(sub)

    
    # 下面是从小到大的排序.
    # 误差越小的越优良
    array_fitness=np.array(fitness_1)
    index=np.argsort(array_fitness)
    
    ii_0=index[0]
    ii_1=index[1]
    ii_2=index[2]
    
    
    print("适应度:",array_fitness)
    print("set_fit_num;输出前三个,误差率,越小越好:",set_fit_num,"ii_0:",ii_0,fitness_1[ii_0],"ii_1:",ii_1,fitness_1[ii_1],"ii_2:",ii_2,fitness_1[ii_2])
    
    #print(index)
    #index=index[::-1]
    #print(index)
    
    # 下面开始组装序列
    list_2d=list_2d.tolist()
    sort_list=[]
    for i in index:
        sort_list.append(list_2d[i])
    #print(sort_list)
    
    # 排完序之后.进行筛选,
    # 通过轮盘赌法筛选.
    # 这个是另一个函数的作用了.
    
    
    # 进行简单的处理,让他达到50行吧
    sort_list_500=[]
    add_cnt=0
    for set_cnt in range(500):
        sort_list_500.append(sort_list[add_cnt])
        add_cnt=add_cnt+1
        if add_cnt>=(len(sort_list)-5):  # 后面三个不要了
            add_cnt=0
        
        
    return sort_list_500
    









if __name__ == '__main__':
    mat=[[1,2,3,4,5,6],
        [2,2,2,2,2,2],
        [3,0,3,3,9,3],
        [2,2,2,2,2,2],
        [4,4,4,4,4,4],
        [5,5,5,5,5,5],
        [4,4,4,4,4,4]]
    
    A=[1,2,3,4,5,6]    
    decode(mat,A)
    
# 如果是下面这样,那么应该不是len(A)就是6
# 然后循环也是6次    
#    A=[1,2,3,4,5,6]
#    for i in range(len(A)):
#        print(len(A))




