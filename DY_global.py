# -*- coding: utf-8 -*-
"""
作用:
    作用一:用于保存全局变量. 比如一些曲子的特征.
           还有计算一些全局变量的函数.
    作用二:用于担任config文件,一些配置参数,也都是全局变量.
    
    
    
需要优化:
    这么多的变量,实际上应该弄一个结构体
"""


import DY_list_calc as Dc
import DY_geneEncoding_2 as Dg
import DY_read_midi_0 as Drd
import DY_cor_0 as cor     # 用于求取相似度.
import DY_plot_0 as Dp


# 关于一些config的参数

# 一个鱼池中,鱼的数量
fishs_number=30
# 一个鱼由几部分组成
fish_parts_number=30
# midi文件的根音的相似度组成的序列
# 因为是相似度,所以会比长度少一个.       
midi_cor_window_size=29

# 一个鱼段由几个音符构成
fish_part_window=6

# 遗传算法中,交叉的概率
pc=0.3
# 遗传算法中,变异的概率
pm=0.3


# 求相似度的基准,一段鱼,也就是某个位置点.
# 它的长度取决于窗口的长度.默认就选择样本midi文件的第一个窗口
first_window=[]

# 鱼池
fish_pond=[]
# 原始鱼,第一条被生成的鱼
original_fish=[]


# 有关赌轮的全局变量
# 被淘汰的数量,从整个鱼池中,去除后5条适应度不够的鱼.
eliminate_num=5
# 最好的一条鱼
first_fish=[]


# 这里设置一些全局变量
# midi文件的音符二维列表
midi_note_list_2D=[]
# midi文件的时间序列列表
midi_time_list_1D=[]
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
                                                       
# midi自身各段的滑动相似度,和窗口相似度
midi_root_slide_cor_list=[]   
midi_root_window_cor_list=[]
# midi文件的名字
midi_name_str='DY_dalabeng.mid'
# 交叉函数中生成的新的2维序列
crossover_new_2d=[]
# 变异函数中生成的新的2维序列
mutation_new_2d=[]
# 测试全局变量
list_try=[]





def global_parameter(sample_name):
    '''
    作用: 用于计算一首midi的所有参数,并且赋值给全局变量.
    传参: sample_name是一个字符串格式,midi的名字.例如:"DY_doudizhu.mid"
    '''
    # 下面sampl是一首曲子的二维音符序列,time_list是一维时间序列.
    sample,time_list=Drd.midi_read(sample_name)
    # 要想传入到全局变量里面,就需要用关键字global
    global midi_note_list_2D
    global midi_time_list_1D
    midi_note_list_2D=sample
    midi_time_list_1D=time_list
    print("midi文件的音符二维数组\n",midi_note_list_2D)
    print("midi文件的时间序列\n",midi_time_list_1D)
    global midi_root_list
    global midi_max_list
    global midi_mean_list
    global midi_row_float_list
    global midi_diff_mean_list
    global midi_diff_root_list
    # 函数的功能应该尽量专一,
    # 函数的代码应该尽量短
    midi_root_list,midi_max_list,midi_mean_list,midi_row_float_list,midi_diff_mean_list,midi_diff_root_list=Dc.list_character(sample)
    
    global fish_part_window
    for i in range(fish_part_window):
        print("i",i)
        first_window.append(midi_root_list[i])
    print("第一个节点,first_window",first_window)
        
    global midi_min_num
    global midi_max_num
    midi_min_num=min(midi_root_list)
    midi_max_num=max(midi_root_list)
    print("midi文件中最大音符和最小音符\n",midi_max_num,midi_min_num)
    # 传入的是一首曲子的根音序列.
    # 生成字典,占比字典
    global midi_root_mean_num
    global midi_mean_float_dic
    midi_root_mean_num,midi_mean_float_dic=Dc.mean_and_float(midi_root_list)           
    # 求取根音序列的相似度
    # 这里应该有个,窗口宽度才对
    global midi_root_slide_cor_list
    global midi_root_window_cor_list
    global midi_cor_window_size
    midi_root_slide_cor_list,midi_root_window_cor_list=cor.window_own_cor(midi_root_list)

    # 整首曲子,根音的波动,和根音字典的饼状图
    Dp.plot_broken("DY_global.py  midi_diff_root_list",midi_diff_root_list)
    Dp.plot_broken("DY_global.py  midi_root_list",midi_root_list)
    Dp.pit_chart("DY_global.py  样本根据平均值的波动得到的字典",midi_mean_float_dic)
    Dp.plot_broken("DY_global.py  midi_root_window_cor_list",midi_root_window_cor_list)
    print("midi_root_window_cor_list\n",midi_root_window_cor_list)


    
if __name__ == '__main__':
    midi_name_str='DY_dalabeng.mid'
    Drd.midi_read(midi_name_str)
    global_parameter(midi_name_str)


    
