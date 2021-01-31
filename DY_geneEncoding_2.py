# 0.0 coding:utf-8 0.0

"""
作用:
    用于生成midi文件的两个要素:
        一个是二维的音符序列;
        另一个是一维的时间序列;
    当然可以手动敲入,但是为了方便,
    我想让他自动生成.
    首先,自动生成就需要有个仿照,需要传入一对现成的 音符序列 和 时间序列 
    然后,根据这两个序列的格式,去随机生成新的数据,替代里面的数据.只是保留一样的格式.
    
    

当然,随机生成也不能乱生成,
最好能够遵守一定的乐理和概率规则:
[生成规则一]: 要有上下限,
[生成规则二]: 要按照预制,"卡农"的格式,
[生成规则三]: ......


术语:
    我们把别人写好的曲子midi文件叫做,成鱼,
    把我们生成的曲子叫做初代鱼.
    因为我们用的是遗传算法,把一首曲子对应成一条鱼,这样便于逻辑的理解!!!
    注: 如果你无法读懂这里的比喻,建议看一遍遗传算法的书籍.
    
    
注: 这个文档里面可能有多个函数,但是并非每个函数都有用的.    
    
"""


import matplotlib.pyplot as plt
import random
import numpy as np
import random
import copy


# 自己的库
import DY_plot_0 as Dp
import DY_list_calc as Dc


chord_dict = {
    'maj3': [0, 4, 7, 0],  # 大三和弦 根音-大三度-纯五度
    'min3': [0, 3, 7, 0],  # 小三和弦 根音-小三度-纯五度
    'aug3': [0, 4, 8, 0],  # 增三和弦 根音-大三度-增五度
    'dim3': [0, 3, 6, 0],  # 减三和弦 根音-小三度-减五度

    'M7': [0, 4, 7, 11],  # 大七和弦 根音-大三度-纯五度-大七度
    'Mm7': [0, 4, 7, 10],  # 属七和弦 根音-大三度-纯五度-小七度
    'm7': [0, 3, 7, 10],  # 小七和弦 根音-小三度-纯五度-小七度
    'mM7': [0, 3, 7, 11],  # 小大七和弦 根音-小三度-纯五度-大七度
    'aug7': [0, 4, 8, 10],  # 增七和弦 根音-大三度-增五度-小七度
    'augM7': [0, 4, 8, 11],  # 增大七和弦 根音-大三度-增五度-小七度
    'm7b5': [0, 3, 6, 10],  # 半减七和弦 根音-小三度-减五度-减七度
    'dim7': [0, 3, 6, 9]  # 减减七和弦 根音-小三度-减五度-减七度
}


#2021.01.17 
#capacity :容量 ,一个水池里,可以容纳多少条鱼.
#sample : 样本 是为了省事,其实应该无规则生成的.  音符的二维数组
#         sample是一首知名的曲子比如,"卡农",从曲子里面摘取出来的音符数组.
#         这里的初代"鱼",都是仿照这个sample写出来的.
# 初代生成


'''
.......................................................................................................................
# 第二种生成初代 鱼 的方法.
'''
#2021.01.17 
#capacity :容量 ,一个水池里,可以容纳多少条鱼.
#sample : 样本 是为了省事,其实应该无规则生成的.  音符的二维数组
#         sample是一首知名的曲子比如,"卡农",从曲子里面摘取出来的音符数组.
#         这里的初代"鱼",都是仿照这个sample写出来的.
# 初代生成
def primary_generation_2(capacity,sample):
    '''
    这个与第一代的生成方式是不一样的.
    第一个函数是,求根音的差,生成的字典,即用的是diff,但是这样有一个问题,就是会波动
    这个函数为了改善波动,从而,利用了平均值,在平均值上的波动,虽然这样生成的效率变低了,
    但是好处是,曲子比较直...
    '''
    # 输出样本二维序列sample的一些参数
    root_list,max_list,mean_list,row_float_list,diff_mean,diff_root=Dc.list_character(sample)
    min_num=min(root_list)
    max_num=max(root_list)
    # 返回整首曲子的diff 百分占比 返回的是字典
    diff_root_dic=Dc.list_percentage(diff_root)  # 这里是根音所占百分比的字典.
    # 传入的是一首曲子的根音序列.
    # 在这里,会求取平均值,并且会返回每个音符,相对于平均值的波动情况.
    # 最后会返回一个百分比的字典.
    song_root_mean,mean_float_dic=Dc.mean_and_float(root_list)           # 曲子在平均值附近的波动字典
    # 这里是我需要的字典,根据根音生成的diff
    print("字典",mean_float_dic)
    # 把这个根据根音生成的diff的键和值打印出来.
    # 这个是后续需要的.取出字典的键和值
    list_keys=mean_float_dic.keys()
    list_values=mean_float_dic.values()
    # 需要转化成list,才能运行???
    list_keys=list(list_keys)
    list_values=list(list_values)
    list_values_sum=sum(list_values)
    print("字典list",list_keys,list_values)

    # 绘制曲子diff
    # 整首曲子,根音的波动,和根音字典的饼状图
    Dp.plot_broken("DY_geneEncoding.py  diff_broken",diff_root)
    Dp.pit_chart("DY_geneEncoding.py  diff_pit",mean_float_dic)
    # print("diff_note",diff_note)
    
    # 深拷贝一个样本,防止损坏sample
    # 这里其实可以没有???
    sample_copy=copy.deepcopy(sample)
    
    # 准备一个二维序列,用于存储要生成的二维音符数组
    primary_note_ex=[]
    row_first_note_last=0
    row_cnt=0


    # 开始构建曲子............
    # 生成随机数,构建音符二维数组.
    # 仿照"成鱼" 循环相同的行数.
    # 首先取出sample_copy的行和列的数量.
    
    gene_root=[]
    for row in sample_copy:
        # 生成每一行的元素.
        # 也就是每一个元素.
        # 为了每一行的序列primary_not_in进行清零,生成一个新的行序列
        # 初代鱼二维序列的内部序列
        primary_note_in=[]
        
        # 上面是清空初代鱼的内部序列
        # 下面是向初代鱼内部序列中加入一个元素.
        
        # 如果是,第一行,row_cnt==0,也就是曲子的第一个元素,
        if row_cnt==0:
            row_first_note=random.randint(min_num,max_num) 
            row_cnt=1
            gene_root.append(row_first_note)
        else:
            # 如果不是曲子的第一个开头,

            # 还需要加一个,符合概率的,就是符合转轮法.    
            # 目前实现按照比例输出是按照这个字典:diff_root_dic  
            # 生成随机数, 这个随机数是从0-100 一个大概100个数据.然后根据随机生成的数据落在那个区间,就是那个数.
            #list_keys=diff_root_dic.keys()
            #list_values=diff_root_dic.values()
            #list_values_sum=sum(list_values)
            
            # 这个随机数落在那个区间,然后,就在上一个音符上波动多少...
            note_random_int=random.randint(0,list_values_sum) # 这里是闭环.

            sum_values=0
            for cnt_keys in range(len(list_keys)):
                # 分界点sum,这个sum呈阶梯状,增加的
                sum_values=sum_values+list_values[cnt_keys]
                
                # 这里的sum_values:就是求和的东西...用于求取它落在那个区间...
                print("上一个音符:",row_first_note)
                if note_random_int<=sum_values:
                    # 再上一个音符中,加入波动,生成新的音符...
                    # 这里是平均值上进行波动添加,这里要转换成整数...
                    row_first_note=int(song_root_mean+list_keys[cnt_keys])
                    # 这里还有一条,就是不要超过界线
                    if row_first_note>120:
                        row_first_note=120
                    if row_first_note<0:
                        row_first_note=0
                    
                    print("最终音符:",row_first_note,"随机数 :",note_random_int,"   小于:",sum_values,"    加键值:",list_keys[cnt_keys])
                    # 如果找到了范围.就跳出来.
                    gene_root.append(row_first_note)
                    break
                



        # 然后把每一行的一个元素放进去
        primary_note_in.append(row_first_note)    
        
        # 下面是对一行的一个元素,进行扩充,扩充成一行.
        # 这里用到了和声的东西.
        for element_cnt in range(len(row)-1):
            chord=[0, 4, 7, 0]
            primary_note_in.append(row_first_note+chord[element_cnt+1])       
            
        # 把整理完的一行数据,写入外围,构成二维数组
        primary_note_ex.append(primary_note_in)
        
    print("样本...:sample")    
    for i in sample:
        print("样本",i)
    print("初代...:primary_note_ex")
    for k in primary_note_ex:
        print("生成",k)
   

    Dp.plot_broken("DY_geneEncoding.py  diff_broken",gene_root)
    #Dp.pit_chart("DY_geneEncoding.py  diff_pit",diff_root_dic)     
    return primary_note_ex








if __name__ == '__main__':
    sample=[[6,6,6],[4,4,4],[1,1,1],[4,4,4]]
    s=primary_generation_2(1,sample)
               

    
