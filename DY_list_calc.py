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






def list_character(list_2dim):
    """
    传入参数: 二维的list,比如传入的是midi的二维音符序列
    
    作用: 计算二维序列的一些特征
          1.二维序列里面,根序列
          2.二维序列里面,最大值序列
          3.二维序列里面,平均值序列
          4.二维序列里面,行内的浮动范围序列
          5.二维序列里面,每行求平均值后,之间的微分
          6.二维序列里面,每行根音,之间的微分
    
    """
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






# 返回的是一个字典,占比字典
def list_percentage(list_data):
    list_to_set=set(list_data)
    dict_proportion={}
    for item in list_to_set:
        # update,是把括号里的东西放入到字典里面, (键):(值)
        # count,是list的用法,用于统计某个元素在list中出现的次数.
        dict_proportion.update({item:list_data.count(item)})
    # 上面得到的是dict_proportion并不是真正的占比,而是简单的个数统计.
    # 下面是计算占比.
    keys=dict_proportion.keys()
    values=dict_proportion.values()
    # 需要转化成list,才能运行......
    keys_list=[]
    values_list=[]
    for key in keys:
        keys_list.append(key)
    for value in values:
        values_list.append(value) 
        
    value_sum=sum(values_list)
    i_cnt=0
    for i in keys_list:
        dict_proportion.update({i:(values_list[i_cnt]/value_sum)})
        i_cnt=i_cnt+1
    return dict_proportion




def mean_and_float(note_1dim):
    """
    传入参数: 一维序列,比如根音序列
    
    作用: 求取一维序列的平均值
          求取一维序列相对于平均值的波动范围,并且求取各波动的占比
    """
    sub=[]
    mean=np.mean(note_1dim)
    for i in note_1dim:
        sub.append(i-mean)
    mean_dict=list_percentage(sub)
    # 返回平均值和占比字典,
    # 字典的键,是与平均值的差值,
    # 字典的值,是差值所占个数.
    return mean,mean_dict



# 按照某种比例,产生一定的数据.
    





if __name__ == '__main__':
    #调用
    list=[1,1,1,1, 2,2,2,2, 2,2,1,1]
    dic=list_percentage(list)
    Dp.pit_chart("饼状图",dic)
    print(dic)

































