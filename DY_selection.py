# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:39:48 2021

@author: python

作用:
    输出最优的解
    这里是遗传算法的入口.
    针对不同的遗传算法,应该有不同的遗传算法入口.
"""

import copy

import DY_cor_0 as Dco
import DY_decode as Dde
import DY_crisscross as Dcr # 交叉
import DY_mutation as Dmu # 变异
import DY_global as Dgl

def selection(mat,A):
    '''
    需要输入什么:
        输入参数1: 要进行遗传算法的序列.(2维)
        输入参数2: 遗传算法的评判标准序列(1维)
    '''
    # 用于保存每一轮的筛选结果,最终组成一首曲子.
    song=[]
    first_list=mat[0]
    cor_list=[]
    song.extend(first_list)
    
    # 用于取出每个元素的标准
    cnt_i=0
    for A_i in A:
        # 轮的最大筛选次数是100
        mat_copy=copy.deepcopy(mat)
        for cnt in range(100):
            # cor_list就是从优到劣排好顺序的二维序列了
            # 这里可以进行优化的.
            # 经过交叉,变异和排序筛选
            # 这里有个问题,加上交叉和变异,就会导致内存溢出...直到99%然后电脑死机...
            if cnt==0:
                pass
            else:
                mat_copy=cor_list
                for mat_cnt in range(len(mat_copy)-1):
                    mat_copy[mat_cnt]=cor_list[mat_cnt]
                    
            # 下面是遗传算法的核心: 交叉,变异,解码,筛选
            Dcr.crossover_2(mat_copy,0.3)
            Dmu.mutation_2(Dgl.crossover_new_2d,0.01)
            cor_list=Dde.decode(Dgl.mutation_new_2d,first_list,A_i)
            print(len(A),"第几段音符串:",cnt_i,   " 第",cnt,"轮最好的一段,目前默认100轮:",cor_list[0])
            Dgl.mutation_new_2d=[]
            Dgl.crossover_new_2d=[]
        # 把最好的一个部件,组装到一条鱼上.    
        song.extend(cor_list[0])
        cnt_i=cnt_i+1
    #print("song根音输出",song)        
    return song
    
    
    
    
    
    

if __name__ == '__main__':
    pass

    
    
    
    
    
    