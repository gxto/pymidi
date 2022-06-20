# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:26:58 2021

@author: python
"""
# 变异
# 基因突变
""" 
遍历每一个个体，基因的每一位发生突变（0变成1,1变成0）的概率为0.001.
突变可以增加解空间，以目标式子：y=10*sin(5x)+7*cos(4x)为例，计算其最大值
首先是初始化，包括具体要计算的式子、种群数量、染色体长度、交配概率、变异概率等。
并且要对基因序列进行初始化。
"""

#一直以为这个变异是有问题的，但是现在看来，好像也没有什么问题。？？？


import random
import copy
import numpy as np

import DY_cor_0 as Dco
import DY_read_midi_0 as Dre
import DY_global as gl
import DY_geneEncoding_2 as Dge

def mutation(pop, pm,ii,xin_pop,sheng_cnt):
    px = len(pop)
    py = len(pop[0])
    
    for i in range(px):                       #这个可以认为是pop有多少行
        if i==ii:
            continue
        if(random.random() < pm):
            sheng_cnt+=1                      #一个新的种类的个体诞生
            mpoint = random.randint(0, py-1)  #这个是产生一定范围的随机数，然后看一下是否进行变异。
            if(pop[i][mpoint] == 1):
                pop[i][mpoint] = 0
            else:                             #这句话实际上不是很需要的。
                pop[i][mpoint] = 1
            #if sheng_cnt<100                  #这里如果严格的话应该加上这一句的。
            if sheng_cnt<(xin_pop.shape[0]-1):
                xin_pop[sheng_cnt]=pop[i]         #把新生成的个体交给存储的xin_pop

    return xin_pop,sheng_cnt



# 下面是进行本土化改良
def mutation_2(list_2d,pm):
    '''
    传入参数1:list_2d,代表着传入的鱼的各个部件,是一个二维的序列.
    传入参数2:pm,代表比例.
    
    这里可能会存在bug,变异可能会带来不和谐
    交叉实际上更容易带来不和谐.
    '''
    # 计算行和列
    px = len(list_2d)
    py = len(list_2d[0])
    
    for i in range(px):
        # 如果小于这个数,就进行变异
        if(random.random() < pm):             
            # 先把变异前的数据保存下来.
            list_old=copy.deepcopy(list_2d[i])
            gl.mutation_new_2d.append(list_old)
            # 生成变异的位置,这个是产生一定范围的随机数
            mpoint = random.randint(0, py-1)
            # 目前是基于在平均值上的摆动产生的.
            song_root_mean=gl.midi_root_mean_num
            diff_root_dic=gl.midi_mean_float_dic
            note=Dge.generate_one_note(song_root_mean,diff_root_dic)
            list_2d[i][mpoint]=note
            # 把变异后的保存下来
            Dgl.mutation_new_2d.append(list_2d[i])
            #print("变异")
      
        else:
            # 把变异前的所有数据都保存下来
            Dgl.mutation_new_2d.append(list_2d[i])
            
    #return Dgl.mutation_new_2d

    



# 变异
def mutation_5(fish_pond,pm):
    '''
    传入参数1:fish_pond,代表鱼池,是一个三维的序列,里面的每一条鱼都是一个二维的序列.
    传入参数2:pm,代表变异的比例.
    
    这里可能会存在bug,变异可能会带来不和谐
    交叉实际上更容易带来不和谐.
    '''
   
    for fish_num in range(gl.fishs_number):
        for part_num in range(gl.fish_parts_number):
            # 如果小于这个数,就进行变异
            if(random.random() < pm):             
                # 生成变异的位置,这个是产生一定范围的随机数
                mpoint = random.randint(0, gl.fish_part_window-1)
                # 目前是基于在平均值上的摆动产生的.
                song_root_mean=gl.midi_root_mean_num
                diff_root_dic=gl.midi_mean_float_dic
                note=Dge.generate_one_note(song_root_mean,diff_root_dic)
                fish_pond[fish_num][part_num][mpoint]=note
                print("变异",fish_pond)
            else:
                pass
    return fish_pond
            


if __name__ == '__main__':

    midi_name="DY_doudizhu.mid"
    gl.global_parameter(midi_name)
    
    gl.fishs_number=2
    gl.fish_parts_number=5
    gl.fish_part_window=6    
    
    list_3=[[[1,2,3,4,5,6],
            [2,3,4,5,6,7],
            [3,4,5,6,7,8],
            [4,5,6,7,8,9],
            [5,6,7,8,9,10]],
    
            [[1,1,1,1,1,1],
            [2,2,2,2,2,2],
            [3,3,3,3,3,3],
            [4,4,4,4,4,4],
            [5,5,5,5,5,5]]
           ]
            
    fish_pond=mutation_5(list_3,10)
    print("fish_pond",np.array(fish_pond))
    
