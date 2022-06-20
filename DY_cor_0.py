# -*- coding: utf-8 -*-

"""
这个算法是计算两个序列相似度的.
这个文档是关于相关系数的算法

来源：https://www.cnblogs.com/ryuham/p/4764015.html

皮尔逊相关系数是：  协方差  和  标准差  的商。
皮尔逊相关系数 范围是 -1 到 1 
-1:代表负相关
0:代表不相关
1:代表正相关

协方差实际上是：Cov(X，Y)=E(XY)-E(X)E(Y)  = E[(X-E(X))(Y-E(Y))]
上面公式中,X和Y都是矩阵的.
标准差，又叫做均方差  ：中文环境中又常称均方差，是离均差平方的算术平均数的平方根，用σ表示。
标准差是方差的算术平方根，标准差能反映一个数据集的离散程度。平均数相同的两组数据，标准差未必相同。


"""


from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import copy

import DY_global as Dgl
import DY_geneEncoding_2 as Dge
import DY_selection as Dse



 
def multipl(a,b):
    """
    传入的是两个序列
    传出的是这两个序列的乘积之和。
    要求:
        这两个序列是等长的.
    """
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab




def corrcoef(x,y):                                                             
    """
    传入的是两个1维序列，得到的是两个序列的相关系数
    
    # 求两个序列的相似度,
    # 如果相同,那么是1....    
    """
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    # 为了防止分母为0,这里,如果分母为0,就让分母等于一个特别小的数:0.0000001
    if den==0:
        den=0.0000001
    value=round(num/den,2)
    return value


# 相关系数
# 作用是,求各条鱼与样本鱼之间的相似度.
def cor_mat_A(mat,A):                                                          #传入的一个是光谱矩阵mat，一个是浓度A
    """
    光谱矩阵，浓度
    相关系数
    还是有很多问题，，，
    """
    cor=[]                                                                     #用于保存，每个波长和浓度之间的相关系数 A：浓度 mat：光谱矩阵
    shape=mat.shape
    #print(shape[0],shape[1])
    for i in range(shape[0]):                                                  #其实这里是循环波长的次数。
        cor.append(corrcoef(A,mat[i,:]))                                       #mat[:,i])表示所有行，第i列；  [][]这一层出错，有可能导致下一行有错误提示。
    return cor





# 下面是,编写自身相似度对比的函数,一首曲子,分成好几段,自身各段之间的对比.
# 有两种方式,一种是窗口平滑滑动; 另一种是窗口阶段的滑动
# 其实这两种方法是相似的,第二种方法,只不过是取了第一种方法中的某几个值.
def window_own_cor(song_list,size=5):
    '''
    song_list: 一维序列,比如midi的根音序列
    '''
    window=[]
    first_window=[]
    # 滑动窗口相似度
    slide_cor=[]
    first_list_flage=1
    # 默认窗口宽度是5,但实际上因为从0开始计,所以真实的窗口宽度是6
    window_size=size
    # 因为是从头到尾,窗口是滑动的,所以需要计算出有多少个音符,
    # 有多少个音符,就需要滑动多少次.
    for i in range(len(song_list)):
        # 如果是1,代表初始的窗口还没有建立好;如果是0,代表建立好了.
        if first_list_flage==1:
            window.append(song_list[i])
            first_window=copy.deepcopy(window) 
            # 这里不能直接用相等,不能用等号,这里是浅copy
            if i==window_size:
                first_list_flage=0
                # round 是四舍五入,保留小数位数的.
                slide_cor.append(round(corrcoef(window,first_window),2))
        else: 
            # 第一次已经计算过了,
            # 下面串口滑动的实现
            for cnt in range(window_size): 
                window[cnt]=window[cnt+1]
            window[window_size]=song_list[i]
            slide_cor.append(round(corrcoef(window,first_window),2))
            #print(cor,"\t",window,"\t",first_window)
    
    
    # 从滑动窗口中取出截断相似度
    window_cor=[]
    data_cnt=0
    for data in slide_cor:
        if data_cnt % (window_size+1)==0:
            window_cor.append(data)
        data_cnt=data_cnt+1
        
    
    return slide_cor,window_cor              




def window_own_cor_5(song_list,first_window,window_size=5):
    '''
    作用:
    # 下面是,编写自身相似度对比的函数,一首曲子,分成好几段,自身各段之间的对比.
    # 有两种方式,一种是窗口平滑滑动; 另一种是窗口阶段的滑动
    # 其实这两种方法是相似的,第二种方法,只不过是取了第一种方法中的某几个值.  
    
    song_list: 一维序列,比如midi的根音序列
    first_window: 一段鱼,就是相对位置的目标点,一整条鱼,都要对这个求相似度.
    '''
    window=[]
    # 滑动窗口相似度
    slide_cor=[]
    # 如果是0,代表初始的窗口还没有建立好;如果是1,代表建立好了.
    first_list_flage=1
    window_size=len(first_window)
    
    
    # 因为是从头到尾,窗口是滑动的,所以需要计算出有多少个音符,
    # 有多少个音符,就需要滑动多少次.
    for i in range(len(song_list)):
        # 默认窗口宽度是5,但实际上因为从0开始计,所以真实的窗口宽度是6
        if i<(window_size-1):
            first_list_flage=1
            window.append(song_list[i])
        elif i==(window_size-1):
            slide_cor.append(round(corrcoef(window,first_window),2))
            first_list_flage=0
            print("window",window)
        else: 
            # 下面窗口滑动的实现,更新一次窗口内容
            for cnt in range(window_size-2): 
                window[cnt]=window[cnt+1]
                print(window[cnt],window[cnt+1])
            # 取下一个新的元素,添加入窗口
            window[window_size-1]=song_list[i]
            slide_cor.append(round(corrcoef(window,first_window),2))
            print("\t",window,"\t",first_window)
    
    
    # 从滑动窗口中取出截断相似度
    window_cor=[]
    data_cnt=0
    for data in slide_cor:
        if data_cnt % (window_size+1)==0:
            window_cor.append(data)
        data_cnt=data_cnt+1
        
    
    return slide_cor,window_cor  
        

# 下面写一个函数,这个函数的作用是,用于改善自身的相关度.
# 一首和谐的曲子,自身的某一段,会有循环的效果.
# 也就是有相关度较高的部分,怎样这个函数是产生自身相关度的.
# 传入参数是: 音符序列 和 所要想达到的相关度序列.
# 目前打算用遗传算法实现这一部分.目前,音符序列这一部分,就先用root音符序列吧,是为了简化....
# note_list这里也可以是一小段音符,
    
# 传入参数1:note_list,6个音符的序列
# 传入参数2:window_cor,样本自身相关度的序列
# 传入参数3:
def cor_correct(note_list,window_cor):
    '''
    既然是自身的相关度,
    那么研究的目标就是自身这个序列才是.
    需要把自身都给分开,分成一段一段的,然后各自部分去用遗传算法.
    那就有必要设置一些全局的变量了.
    '''
    # 第一步,截取一段音符,默认窗口宽度是6,所以截取一段长度是6的音符.
    # 只截取头6个音符.
    cnt =0
    window=[]
    for i in note_list:
        window.append(i)
        cnt=cnt+1
        if cnt==6:   # 这里默认窗口宽度是6
            break
    
    # 第二步,随机生成几段段音符,也是窗口宽度的音符.用于遗传算法.
    # 生成一系列的音符段,也就是初代鱼的各个零件...
    fish_part=[]
    fish_part_num=30
    for i in range(fish_part_num):      
        long=6
        min_num=Dgl.midi_min_num
        max_num=Dgl.midi_max_num
        song_root_mean=Dgl.midi_root_mean_num
        diff_dic=Dgl.midi_mean_float_dic
        note_6_list=Dge.generate_root_note_list(long,min_num,max_num,song_root_mean,diff_dic)
        fish_part.append(note_6_list)
     
    # 上面这一步,生成了一个二维的序列,fish_part.这是一个30行,6列的二维序列.把他们拼接起来,代表了一首曲子的根音序列.

    
    # 第三步,用于交叉和变异.
    # 第四步,求取交叉和变异后的相关系数,然后再进行排序筛选,选择最优的.
    # 把第三步和第四步组合到了一起,放入了selection中.
    song_root_list=Dse.selection(fish_part,Dgl.midi_root_window_cor_list)
    
    # 输出通过遗传算法得到的midi序列
    return song_root_list
    
    
    



def try_global():
    Dgl.list_try.append(2)    

if __name__ == '__main__':
 
    
    x = [1,2,3,4,5,6   ,7,8,9,10,11,12,   13,14,15,16,17,18  ,19,20,21,22,23,24]
    y = [1,2,3,4,5,6]
        
    # 求取皮尔逊相关系数
    #cor=corrcoef(x,y)
    #cor=corAmat(x,y)
    cor,wcor=window_own_cor_5(x,y)
    print(cor)
    print(wcor)
    
    
    
