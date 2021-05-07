# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:48:32 2021

@author: python


作用:
    这里是list的处理.
    用来,计算list的.
"""
# 调用官方的库
import numpy as np

# 调用绘图的库,这个是自己编写的
import DY_plot_0 as Dp


# 计算list的最大值,最小值,平均值
# 计算二维序列的一些特性
def list_character(list_2dim):
    # 查找每一行的最大值和最小值,组成序列
    max_list=[]
    min_root_list=[]
    mean_list=[]
    #二维序列里面每一行的波动
    row_float_list=[] 
    # list_2dim是二维的序列
    for i in list_2dim:
        max_list.append(max(i))
        min_root_list.append(min(i))
        mean_list.append(np.mean(i))
        # 一行里面的浮动范围
        row_float_list.append(max(i)-min(i))
    # 整个序列的最大值和最小值.    
    max_num=max(max_list)
    min_num=min(min_root_list)
    
    #print("list_calc.py 整个序列的最大值,最小值",max_num,min_num)
    
    # 一行里面的最大值和最小值.
    max_row_float=max(row_float_list)
    min_row_float=min(row_float_list)
    #print("list_calc.py 一行里面的最大波动,最小波动",max_row_float,min_row_float)
    
    
    diff_mean_note=[] # 查找样本中,每个音符的音阶相差多少
    diff_root_note=[] # 这里是根音的序列
    
    for index in range(len(mean_list)):
        if index==0:
            # 第一个元素,默认填写0了......
            diff_mean_note.append(0) 
            diff_root_note.append(0)
        else:
            diff_mean_note.append(mean_list[index]-mean_list[index-1])
            diff_root_note.append(min_root_list[index]-min_root_list[index-1])
    # 整个曲子的diff        
    diff_max=max(diff_mean_note)
    diff_min=min(diff_mean_note)
    #print("list_calc.py 整个曲子求导的最大值,最小值",diff_max,diff_min)
    
    return min_root_list,max_list,mean_list,row_float_list,diff_mean_note,diff_root_note    






# 计算list中每个元素的数量占的个数(实际上这里转换成比例是比较合理的).
def list_percentage(list_data):
    list_to_set=set(list_data)
    dict_lt={}
    for item in list_to_set:
        # update,是把括号里的东西放入到字典里面, (键):(值)
        # count,是list的用法,用于统计某个元素在list中出现的次数.
        dict_lt.update({item:list_data.count(item)})
    #print(dict_lt)
    return dict_lt



# 传入的是根音序列,是个一维序列
# 以及这首曲子,每个音符,相对于平均值的波动范围
# 以及,波动范围的占比.
def mean_and_float(note_1dim):
    sub=[]
    mean=np.mean(note_1dim)
    for i in note_1dim:
        # 求出这首曲子,每个音符相对于平均值漂移了多少.
        sub.append(i-mean)
    # 从这里sub序列就完成了,
    mean_dict=list_percentage(sub)
    # 返回平均值和占比字典,
    # 字典的键,是与平均值的差值,
    # 字典的值,是差值所占个数.
    return mean,mean_dict



# 按照某种比例,产生一定的数据.
    


if __name__ == '__main__':
    #调用
    list=[1,1,1,1, 1,1,1,1, 1,1,1,1]
    dic=list_percentage(list)
    Dp.pit_chart("饼状图",dic)
    mean_dict=mean_and_float(list)
    print(mean_dict)

































