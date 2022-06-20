# -*- coding: utf-8 -*-
"""
作用:
    输出最优的解
    这里是遗传算法的入口.
    针对不同的遗传算法,应该有不同的遗传算法入口.
"""

import copy
import numpy as np

import DY_cor_0 as Dco
import DY_decode as Dde
import DY_crisscross as Dcr # 交叉
import DY_mutation as Dmu # 变异
import DY_global as Dgl

def selection(fish_parts,window_cor):
    '''
    输入参数1: 要进行遗传算法的序列.(2维比如: [[],[],[],......]的类型)  这里是一个曲子根音序列,但是还没有进行组装
    输入参数2: 遗传算法的评判标准序列(1维) 这里是曲子的 自身相似度的 序列
    '''
    # 用于保存每一轮的筛选结果,最终组成一首曲子.
    song=[]
    first_list=fish_parts[0]
    cor_list=[]
    song.extend(first_list)
    
    # 用于取出每个元素的标准
    cnt_i=0
    for cor_value in window_cor:
        # 轮的最大筛选次数是100
        fish_parts_copy=copy.deepcopy(fish_parts)
        for cnt in range(100):
            # cor_list就是从优到劣排好顺序的二维序列了
            # 这里可以进行优化的.
            # 经过交叉,变异和排序筛选
            if cnt==0:
                pass
            else:
                fish_parts_copy=cor_list
                for mat_cnt in range(len(fish_parts_copy)-1):
                    fish_parts_copy[mat_cnt]=cor_list[mat_cnt]
                    
            # 下面是遗传算法的核心: 交叉,变异,解码,筛选
            Dcr.crossover_2(fish_parts_copy,0.3)                               # 把fish_parts_copy,也就是根音符序列,进行0.3概率的交叉,生成全局变量crossover_new_2d
            Dmu.mutation_2(Dgl.crossover_new_2d,0.01)                          # 把上面交叉的根音符序列,crossover_new_2d进行突变变异,生成全局变量mutation_new_2d
            cor_list=Dde.decode(Dgl.mutation_new_2d,first_list,cor_value)          # 把经过,交叉,变异之后的序列,进行选优处理,得到cor_list这个序列,是二维的.
            print(len(window_cor),"第几段音符串:",cnt_i,   " 第",cnt,"轮最好的一段,目前默认100轮:",cor_list[0])
            Dgl.mutation_new_2d=[]
            Dgl.crossover_new_2d=[]
        # 把最好的一个部件,组装到一条鱼上.    
        song.extend(cor_list[0])
        cnt_i=cnt_i+1
      
    # 目前如果用的是doudizhi.midi那么相似度序列是:
    #  [1.0, -0.86, 0.08, 0.78, 0.48, -0.81, 0.55, 0.04, 0.08, -0.66, -0.8, 0.85, 0.64, -0.58] 
    # 先把这个建立一个字典,字典的key是相似度的值; 字典的value是每个音乐片段;
    # 然后重新生成一遍曲子.用相似度序列,进行循环,然后查找字典里面比较合适的key值,就对应添加key对应的音符序列进生成曲子里面.
    
#    cor_dic={} # 创建一个相似度的字典
#    cor_dic.fromkeys(window_cor)
    return song
    
    
    
    
# 相对与selection,有了一点变化,
# 主要的变化就是根据相似度,列出几个等级,相似度特别接近的,就不再分开赋值了,
# 相似度接近的,就用前面产生的值.
# 目的是把特别相近的两个部分,弄成一个部分,这样就有了完全一样的段落了. (可以有循环的效果).
# 这里面也有很多全局的条参需要设置.
# 需要优化,不一定要只传入相似度.还可以进行其他的序列的遗传算法筛选.
def selection_2(fish_parts,window_cor):
    '''
    输入参数1: 要进行遗传算法的序列.(2维比如: [[],[],[],......]的类型 鱼头,鱼身,鱼尾...)  
              这里是一个曲子根音序列,但是还没有进行组装
    输入参数2: 遗传算法的评判标准序列(1维) 这里是曲子的 自身相似度的 序列
    '''
    # 目前如果用的是doudizhi.midi那么相似度序列是:
    #  [1.0, -0.86, 0.08, 0.78, 0.48, -0.81, 0.55, 
    #  0.04,0.08, -0.66, -0.8, 0.85, 0.64, -0.58] 
    # 先把这个建立一个字典,字典的key是相似度的值; 字典的value是每个音乐片段;
    # 然后重新生成一遍曲子.用相似度序列,进行循环,
    # 然后查找字典里面比较合适的key值,添加该key对应的音符序列进入新生成的曲子里面.
    
    
    # 创建一个相似度的字典
    cor_dic={} 
    # 相似度字典的keys进行赋值.
    cor_dic.fromkeys(window_cor) 
    print("赋值前的相似度字典",cor_dic)
    window_cor_set=set(window_cor)
    window_cor_set_list=list(window_cor_set)
    print("输出window_cor_set和window_cor_set_list",window_cor_set,window_cor_set_list)
    # 用于保存每一轮的筛选结果,最终组成一首曲子.
    song=[]
    first_list=fish_parts[0]
    cor_list=[]
    song.extend(first_list)
    
    # 用于取出每个元素的标准
    cnt_i=0
    for cor_value in window_cor:
        
        fish_parts_copy=copy.deepcopy(fish_parts)
        # cor_list就是从优到劣排好顺序的二维序列了
        # 这里可以进行优化的.
        # 经过交叉,变异和排序筛选 
        # 轮的最大筛选次数是100,100次过后,无论有没有找到最优的,都把当前最优的留下来.
        for cnt in range(100):
            if cnt==0:
                pass
            else:
                fish_parts_copy=cor_list
                for mat_cnt in range(len(fish_parts_copy)-1):
                    fish_parts_copy[mat_cnt]=cor_list[mat_cnt]
                    
            # 下面是遗传算法的核心: 交叉,变异,解码,筛选
            # 下面是交叉,把fish_parts_copy,也就是根音符序列,进行0.3概率的交叉,生成全局变量crossover_new_2d.
            Dcr.crossover_2(fish_parts_copy,0.3)                               
            # 下面是变异,crossover_new_2d进行突变变异,生成全局变量mutation_new_2d.
            Dmu.mutation_2(Dgl.crossover_new_2d,0.01)                     
            # 把经过,交叉,变异之后的序列,进行选优处理,得到cor_list这个序列,是二维的.
            cor_list=Dde.decode(Dgl.mutation_new_2d,first_list,cor_value)     
            print(len(window_cor),"第几段音符串:",cnt_i,   " 第",cnt,"轮最好的一段,目前默认100轮:",cor_list[0])
            Dgl.mutation_new_2d=[]
            Dgl.crossover_new_2d=[]
        # 把最好的一个部件,组装到一条鱼上.
        cor_dic[cor_value]=cor_list[0]
        song.extend(cor_list[0])
        cnt_i=cnt_i+1
    print("完成内容的相似度字典",cor_dic)
    
    # 下面重新创建一首新的曲子
    song2=[]
    song2.extend(first_list)
    for cor_data in window_cor:
        for cor_set_data in window_cor_set_list:
            if abs(cor_data-cor_set_data)<0.7:       # 分辨率
                song2.extend(cor_dic[cor_set_data])
                break 

    return song2
    



# 一条鱼的,相似度评测
def fish_correlation_evaluation(fish_root_parts,one_fish_root_part,window_cor):
    '''
    输入参数1: 一个二维数组,一条鱼的根序列段集合,包括鱼头序列,鱼身序列,鱼尾序列等.
    输入参数2: 一维序列,鱼的某一部分序列.
    输入参数3: 相似度序列,样本鱼的相似度序列.
    '''
    # 鱼头与鱼头,鱼身,鱼尾...的相似度. [完成这个函数,剩下的就是套用.]
    # 鱼身与鱼头,鱼身,鱼尾...的相似度.
    # 鱼尾与鱼头,鱼身,鱼尾...的相似度.
    # 生成只负责生成
    # 评分只负责评分
    # 筛选只负责筛选
    
    
    fitness=[]
    fitness_0=[]
    fish_root_parts_array=np.array(fish_root_parts)
    one_fish_root_part_array=np.array(one_fish_root_part)
    fitness_0=Dco.cor_mat_A(fish_root_parts_array,one_fish_root_part_array) 
    print("fitness_0;",fitness_0)
    fitness_0_array=np.array(fitness_0)
    window_cor_array=np.array(window_cor)
    print("fitness_0_array",fitness_0_array)
    print("window_cor_array",window_cor_array)
    # 越是接近,这个值就是越小.这个可以认为是误差
    # 这个window_cor_array也需要建造一个函数,求出来才是.
    err_fitness_array=(fitness_0_array-window_cor_array)
    print("fitness:",err_fitness_array)
    fitness=abs(err_fitness_array)
    print("abs fitness:",fitness)
    err_sum_array=sum(fitness)
    print("err_sum_array:",err_sum_array)
    
    # 最终返回一个数值,这个err代表一个误差的大小
    return err_sum_array



def fishpond_correlation_evaluation(fishpond_root_parts,one_fish_root_part,window_cor):
    '''
    作用,对鱼池中鱼的评估.并返回err的list.
    '''
    err_list=[]
    for fish_root_parts in fishpond_root_parts:
        err=fish_correlation_evaluation(fish_root_parts,one_fish_root_part,window_cor) 
        err_list.append(err)
    print("err_list:",err_list)
    return err_list



# 当前文档的验证代码
if __name__ == '__main__':
    
    fish=[[1,1,3,1,1],[2,2,2,4,2],[3,3,3,3,5],[1,3,4,5,6]]
    fishpond=[
              [[1,1,1,1,1],[2,2,2,2,2]],
              [[3,3,3,3,3],[4,4,4,4,4]]
             ]
    window_cor=[0.8,1]
    #Dgl.global_parameter("DY_doudizhu.mid")
    #fish_correlation_evaluation(fish,fish[0],window_cor)
    fishpond_correlation_evaluation(fishpond,fish[0],window_cor)

    
    
    
    
    
    