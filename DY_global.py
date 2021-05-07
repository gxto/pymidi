# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:21:49 2021

@author: python

作用:
    用于保存全局变量. 比如一些曲子的特征.
    还有计算一些全局变量的函数.
    
"""


import DY_list_calc as Dc
import DY_geneEncoding_2 as Dg
import DY_read_midi_0 as Dr


# 这里设置一些全局变量

# midi文件的根音序列
midi_root_list=[]
# midi文件的最大值序列
midi_max_list=[]
# midi文件的平均值序列
midi_mean_list=[]
# midi文件的每一行的浮动
midi_row_float_list=[]
# midi文件每一行的平均值,然后平均值构成序列的diff
midi_diff_mean_list=[]
# midi文件根音的diff序列
midi_diff_root_list=[]
# midi文件中出现的最大值 最小值 平均值
midi_min_num=0
midi_max_num=0
midi_root_mean_num=0
# midi中平均值序列的波动字典
midi_mean_float_dic={}
# midi字典的keys和valuse序列
midi_dic_keys_list=[]
midi_dic_values_list=[]
# 字典的values求和
midi_dic_values_sum_num=0
# midi文件的根音的相似度组成的序列
midi_root_cor_list=[]
midi_window_cor_list=[]
# midi文件的名字
midi_name_str='DY_dalabeng.mid'
# midi文件的音符二维列表
midi_note_2_list=[]
# midi文件的时间序列列表
midi_time_1_list=[]



# 交叉函数中生成的新的2维序列
crossover_new_2d=[]
# 变异函数中生成的新的2维序列
mutation_new_2d=[]


# 测试全局变量
list_try=[]




    
if __name__ == '__main__':
    # 为什么这里全局变量是失败的???
    # 关于这种模块化的全局变量,这里有个问题....
    # 就是在本文档内使用时,会不起作用,在其他文档的时候是正常的...
    midi_name_str='DY_dalabeng.mid'
    Dr.midi_read(midi_name_str)
    print(midi_note_2_list)
#    Dg.calc_midi_parameter(midi_note_2_list)
#    print(midi_dic_keys_list)
    
