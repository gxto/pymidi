# -*- coding: utf-8 -*-
"""
作用:
    解码和排序
    主要按照各个的适应度.进行从强到弱的排序.
    为轮盘转法去做筛查依据. 
    也要防止过拟合的问题.
"""

import numpy as np


import DY_cor_0 as Dco
import DY_global as gl
import DY_selection as sel



# 这里是解码的部分,主要是一个筛选的功能.
# 这里实际上等价于轮转法.
def decode(list_2d,first_window_list,set_fit_num):
    '''
    传入参数1:list_2d,鱼的各个部分的二维数组,(传入的是经过交叉,变异后的数组)
    传入参数2:first_window_list,曲子的第一部分
    传入参数3:set_fit_num想要的适应度.(这里是一个数字)
    主要是求取两者的相似度.
    '''
    # 变成list
    array_2d=np.array(list_2d)
    # 下面是去重复的行.
    # 参考:https://www.jb51.net/article/155244.htm 
    # 什么哈希之类的...才能排序...
    list_2d=np.array(list(set([tuple(t) for t in array_2d])))
    
    # 求取适应度序列
    fitness_1=[]
    # 与第一个求取相似度.
    fitness=Dco.cor_mat_A(list_2d,first_window_list)   
    #print("适应度的值:",fitness)
    
    # 对比一下,如果与传进来的相似度合适,与set_fit_num接近,
    # 就说明是合适的,把负数都变成正的.
    for i in range(len(fitness)-1):
        sub=fitness[i]-set_fit_num
        if sub<0:
            sub=-sub
        fitness_1.append(sub)
        
    # 这里的sub就是得分基准
    # 可以认为有很多项的标准,这里相似度只是评分的一项.
    # 以100分为满分,得分越高越好.sub是越小越好.所以需要转换一下
    fitness_achievement=[]
    for i in range(len(fitness)-1):
        sub=fitness[i]-set_fit_num
        if sub<0:
            sub=-sub
        fitness_achievement.append(100-sub)
    

    
    # 下面是从小到大的排序.
    # 误差越小的越优良,返回排好序的角标,即返回索引.
    array_fitness=np.array(fitness_1)
    index=np.argsort(array_fitness)
    
    ii_0=index[0]
    ii_1=index[1]
    ii_2=index[2]
    
    
    #print("适应度:",array_fitness)
    #print("set_fit_num;输出前三个,误差率,越小越好:",set_fit_num,"ii_0:",ii_0,fitness_1[ii_0],"ii_1:",ii_1,fitness_1[ii_1],"ii_2:",ii_2,fitness_1[ii_2])
    
    #print(index)
    #index=index[::-1]
    #print(index)
    
    # 下面开始组装序列
    # 组装成排好序的list
    list_2d=list_2d.tolist()
    sort_list=[]
    for i in index:
        sort_list.append(list_2d[i])
    # 输出排好序的list
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
        if add_cnt>=(len(sort_list)-5):  # 后面5个不要了,一共有30个应该是...
            add_cnt=0
        
        
    return sort_list_500
    




# 这是一个评分函数
def decode_3(list_2d,first_window_list,set_fit_num):
    '''
    传入参数1:list_2d,一条完整的鱼.
    传入参数2:first_window_list,曲子的第一部分,鱼头.
    传入参数3:set_fit_num想要的适应度.(这里是一个数字)
    主要是求取两者的相似度.
    '''
    # 变成list
    array_2d=np.array(list_2d)
    # 下面是去重复的行.
    # 参考:https://www.jb51.net/article/155244.htm 
    # 什么哈希之类的...才能排序...
    list_2d=np.array(list(set([tuple(t) for t in array_2d])))
    
    # 求取适应度序列
    fitness_1=[]
    # 求取一条鱼,与,鱼头的相似度
    fitness=Dco.cor_mat_A(list_2d,first_window_list)   
    #print("适应度的值:",fitness)
    
    # 对比一下,如果与传进来的相似度合适,与set_fit_num接近,
    # 就说明是合适的,把负数都变成正的.
    for i in range(len(fitness)-1):
        sub=fitness[i]-set_fit_num
        if sub<0:
            sub=-sub
        fitness_1.append(sub)
        
    # 这里的sub就是得分基准
    # 可以认为有很多项的标准,这里相似度只是评分的一项.
    # 以100分为满分,得分越高越好.sub是越小越好.所以需要转换一下
    fitness_achievement=[]
    for i in range(len(fitness)-1):
        sub=fitness[i]-set_fit_num
        if sub<0:
            sub=-sub
        fitness_achievement.append(100-sub)
    

    
    # 下面是从小到大的排序.
    # 误差越小的越优良,返回排好序的角标,即返回索引.
    array_fitness=np.array(fitness_1)
    index=np.argsort(array_fitness)
    
    ii_0=index[0]
    ii_1=index[1]
    ii_2=index[2]
    
    
    #print("适应度:",array_fitness)
    #print("set_fit_num;输出前三个,误差率,越小越好:",set_fit_num,"ii_0:",ii_0,fitness_1[ii_0],"ii_1:",ii_1,fitness_1[ii_1],"ii_2:",ii_2,fitness_1[ii_2])
    
    #print(index)
    #index=index[::-1]
    #print(index)
    
    # 下面开始组装序列
    # 组装成排好序的list
    list_2d=list_2d.tolist()
    sort_list=[]
    for i in index:
        sort_list.append(list_2d[i])
    # 输出排好序的list
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
        if add_cnt>=(len(sort_list)-5):  # 后面5个不要了,一共有30个应该是...
            add_cnt=0
        
        
    return sort_list_500






# 赌轮 轮转法
def decode_5(fishpond_root_parts,one_fish_root_part,window_cor):
    '''
    传入参数1:list_2d,一条完整的鱼.
    传入参数2:first_window_list,曲子的第一部分,鱼头.
    传入参数3:set_fit_num想要的适应度.(这里是一个数字)
    主要作用是实现赌轮法,
        赌轮的目的,是更新鱼池;
        标准就是适应度误差,根据适应度误差来决定鱼的去留.误差越大,越容易被去除.
        就是淘汰一部分不适应的鱼,然后重新构造或者复制一些适应环境的鱼.
        
    '''    
    #fitness_err=[1,5,1]
    # 返回的是误差,也就是适应度的倒数,是一个err的list. 对所有的鱼进行评测.
    fitness_err=sel.fishpond_correlation_evaluation(fishpond_root_parts,one_fish_root_part,window_cor)   
    print("适应度的值:",fitness_err)
    
    
    # 下面是从小到大的排序.
    # 误差越小的越优良,返回排好序的角标,即返回索引.
    array_fitness=np.array(fitness_err)
    index=np.argsort(array_fitness)
    print("index",index)

    
    # 下面开始组装序列
    # 组装成排好序的list
    sort_list=[]
    for i in index:
        sort_list.append(fishpond_root_parts[i])
    # 输出排好序的list
    print("根据适应度误差,排序后的list",sort_list)  
    
    # 重新组成鱼池,让鱼池里的鱼的数量达到.gl.fishs_number
    fish_pond=[]
    add_cnt=0
    for cnt in range(gl.fishs_number):
        fish_pond.append(sort_list[add_cnt])
        add_cnt=add_cnt+1
        # 后面5条鱼适应度不够,就不加入鱼池了,标号add_cnt从新从头,选择适应度较高的鱼复制到鱼池.
        if(len(sort_list)>gl.eliminate_num):
            if add_cnt>=(len(sort_list)-gl.eliminate_num):  
                add_cnt=0
        # 如果长度不够,就轮流添加,这里需要优化
        else:
            if(add_cnt>=len(sort_list)):
                add_cnt=0;
        print("    输出add_cnt ",add_cnt,sort_list[add_cnt])
    first_fish=sort_list[0]
    print("输出最后的结果,更新后的鱼池",fish_pond)
    return fish_pond,first_fish


if __name__ == '__main__':
    gl.fishs_number=5;
    gl.eliminate_num=0;
    mat=[
        [[1,2],[3,4]],
        [[1,2],[3,4]],
        [[5,5],[5,5]]        
        ]
    print("mat",mat)
    A=[1,2,3,4,5,6]    
    decode_5(mat,A,0.3)
    
# 如果是下面这样,那么应该不是len(A)就是6
# 然后循环也是6次    
#    A=[1,2,3,4,5,6]
#    for i in range(len(A)):
#        print(len(A))




