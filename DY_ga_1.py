# 0.0 coding:utf-8 0.0


""" 

根据网上的解读，这篇才是真正的主文档main，，，

【】【】【】【】其实还有个最后的办法，就是枚举法，我们把所有的可能都列出来，一个一个试，这样固然很慢，但是一定会有结果。

此程序是用遗传算法来计算一个式子的最大值
一般遗传算法分为下面几步：
1、种群初始化：根据特定问题设计合理的初始化（初始化操作应尽量简单，时间复杂度不宜过高）
2、个体评价：根据优化的目标函数计算种群中所有个体的适应值
3、迭代设置：设置种群中最大的迭代次数，从1开始迭代
4、个体选择：设计合适的选择算子来对种群个体进行选择，选择的个体用于产生后代
5、交叉算子：父代是否要进行交叉操作
6、变异算子：父代是否变异。变异算子的主要作用是保持种群的多样性，防止种群陷入局部最优，

父代种群进行交叉变异后产生子代，然后进入下一轮迭代操作。


目前要做的是把 “偏最小二乘法” 嵌入到 “遗传算法” 里面。
要修改如下：（修改工程，就从主函数开始修改。）
1，编码：遗传算法里一个染色体就是一个解决方案，我们的问题是波长配比，所以每种解决方案就是一个波长集合。
2，解码：似乎不需要解码，解码就是生成RON的过程，根据所选的波长，选取对应的数组，组成RON文件。
3，个体评估：这里的个体评估是带入方程，我们要改成“偏最小二乘法”建模。
4，剩下的挑选，进化，迭代都是差不多的。



#首先一些概念要熟悉：基因，染色体（里面包含多个基因），种群



修改：
【】这一版的程序中把输入光谱要加上后缀才行，，，，其实我心里也不知道这样改是不是正确的。
需要修改波长统计部分，每一轮都要统计一次。
需要修改原始的种群数量，因为2的247次方很大，，226156424291633194186662080095093570025917938800079226639565593765455331328种可能 就需要我们扩大撒点数，，繁衍次数也要变大。
需要修改，关于评估那里不是很明了。
需要修改，这2018.10.25版的pls还是有点问题，主成分提取的数有点少。只有2个感觉上是不太合理的。？？？可以从评判标准上入手去改进。
需要修改，就是遗传算法用的是需要大的数，偏最小二乘法是需要小的数，这两者之间转换的问题虽然已经处理，但是没有达到最佳状态。
需要修改，差分等各个函数的输入如果是数组就好了。
需要修改，要有  range（）的规范。
需要修改，如何解决强行拟合噪声。
需要修改，这里的变异是否合理，，，这里的转轮淘汰机制是否合理，不是很合理。
需要修改，关于图片的关闭和显示。
需要修改，导入数据，最好通通导入的是源文件，
需要修改，怎样让pop种群中，某个染色体占据大部分，比如90%的时候停下来？？？？
需要修改，感觉没有循环几次，就已经把种群都变成了相同的染色体。
需要修改，划分测试集和训练集，为了公平起见，都要划分成一致的。  但是不知道主成分需要需要变？？？
需要修改，图为什么会有锥子的形状，可能是因为固定划分了测试集范围。
需要修改，遗传算法参数调节依据。
需要修改，不能把不需要的填充成0，应该完全抹去，否则会影响建模，就如calobjValue.py文档中一样：一个简单的模型需要耗费大量的主成分。，，关于这里的例子测试。
需要修改，为什么统计出的波长，总是一层一层的，这有点不太合理。
需要修改，除了要选出最好的波长组合之外，还要选择，最优的主成分个数，然后再根据这两个去建模。
需要修改，calobjValue.py文档中，用很规则的数据进行建模，8个1和9个1的问题，有的时候主成分数目，超出了，x的列数。。。所以主成分选取的方法还是有待考虑的？？？
需要修改，不知道py_pls_PLSR7.py 中的误差计算，返回的误差是不是准确的。,,,,这里Qh可能有分母是0的情况？？？？？？？
需要修改，轮盘选择，selection.py文件中轮盘的没有深拷贝，，也没有彻底释放内存？？？但是在测试的时候没有关系？？？
需要修改，从目前效果来看，存在着早熟的现象，，，因为建模的拟合图形之后的几轮都没有变化。。。。？？？？
需要修改，作为一个合格优秀的函数，每个变量应该有明确的意义，名字要言简意赅。
需要修改，在pop中，如果只有一个1或者两个1，其他都是0，那么就会导致在建模的时候主成分的个数超出？？？
需要修改，一些参数的确需要修改的地方很多，可以用程序运行的时候进行提示然后根据提示输入相应的信息，，，
需要修改，关于种群扩张的问题30个总是感觉太少了
需要修改，再出现pls拟合的同时，也要有波长选择的图配合出来，这样比较直观。

【2018.10.30】需要修改，关于矩阵大小一致性的问题（最好不要规定，而是用python自己读取矩阵的大小，自己只规定第一回。）【】【】程序的中间传递变量，最好自己不要去赋值。
【2018.10.30】需要修改，消除了出现拟合竖线的问题。
【2018.10.31】需要修改，划分测试集和训练集，为了公平起见，都要划分成一致的。  可以随机，也可以固定。
【2018.10.31】需要修改，把主函数规范化



【心得】程序大概分为两部分，一个是参数设置部分，另一个是执行部分。
【心得】对于图像的分析：
        1，主要是找理想与现实之间的差距
        2，理想中图像应该是怎样的，
        3，现实中又是什么样的
        4，噪声有哪些，怎样区分信息和噪声。，，，根据噪声的特点怎样去除。  是否归一化，是否预筛选。
        5，图像有的特定，为什么会有这些特点
【心得】从省内存的角度看，浅拷贝也挺好的。
"""

#共有的库
import copy
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.cross_validation import train_test_split                          #用于随机划分训练集和测试集。
import random
import gc
from memory_profiler import profile                                            #内存检查的库。



#自己的库
from py_xunzhao_bochang import xunzhao_bochang                                 #寻找波长
from py_zaoshengjuzhen import load_zaoshengjuzhen                              #这个是噪声矩阵。
from calobjValue_1 import calobjValue                                          #解码建模，，，过滤光谱矩阵
import calobjValue_1
from calfitValue import calfitValue                                            #淘汰，阈值淘汰。
from selection import selection                                                #复制，选择，轮转选择
from crossover import crossover                                                #交叉
from mutation import mutation                                                  #变异
from best import best,best_2                                                          #选择本轮最优染色体。
from geneEncoding import geneEncoding,geneEncoding1,geneEncoding2,pop_sum_hang              #这个是自己写的库，自己去引入。
from geneEncoding import pop_tongji
import py_pls_PLSR7 as PLS                                                     #我要引入偏最小二成法的文件。这里有个天大的漏洞，需要把PLSR4程序规整一下。
from py_cor import corrcoef                                                    #相关系数的计算。 
from guiyihua import autoNorm0,autoNorm1                                       #关于横纵轴的归一化。
import py_OSC as OSC
#np.set_printoptions(threshold='nan')  #全部输出                                #其全部输出，防止有省略号？？？
#np.set_printoptions(threshold=np.inf)


#@profile                                                                      #对于这个修饰器，还是没有搞太明白。
def yichuan_xunhuan(pop,x_train,x_test,y_train,y_test,tongji1,A0,switch,pc,pm):              
    """
    虽然取名叫做 遗传循环，但是这里只是，每次循环中的内容罢了，这个函数里没有循环。
    
    遗传算法的核心部分，遗传算法的循环部分，每次循环要执行的东西。：生和死。
    遗传算法的循环：解码【这个里面是有建模的】，选择（生和死的抉择），交配，变异（后面两个是生），
    
    这个函数还是要进行改进的。【关于生和死的调节。需要做精细的调节】
    
    """
    
    newobj_value,b = calobjValue(pop, x_train, x_test, y_train, y_test,A0,switch)     # 解码，建模，求误差          ；   【这里有建模过程】（把2进制变成10进制）然后带入目标方程计算式子结果，obj_value中显示。 个体评价
    best_individual, best_fit,ii = best(pop, newobj_value)		                        # 寻找最优                    ；    第一个存储最优的基因, 第二个存储最优解。不过这个要改成返回一个，pop的行号。，以便保留最优解，防止最优解在后面的过程中被改变掉。
    #newobj_value = calfitValue(newobj_value)                                         # 【按照阈值淘汰，感觉这个没有什么用途】淘汰，阈值法进行标记        ；    根据结果，淘汰一部分的不合理解。淘汰的速率也应该斟酌一下，什么样才是最好，淘汰速度，决定了收敛速度，决定了循环的代数。
    pop=selection(pop, newobj_value,b,pc,pm,ii)		                                  #【生和死都在这里面，生和死就是对pop的操作】 新种群复制，真正淘汰，【种群一直再生长才对】        ；    【】【】应该在这里加上一个检验种群是否进化完全了。
#    print("本轮最优染色体:")
#    print(best_individual)
#    print("染色体长度：")
#    print(len(best_individual))
    pop_sum_hang(pop)                                                          #【这里也是一个出bug的地方呀】检测次轮pop有没有空的。[][]【】【】这里是要改的。。。
    return pop,best_individual                                                 # 返回进化后的种群,和最优的解（即最优的特征波长）



def yichuan_xunhuan_gang(pop,x_train,x_test,y_train,y_test,tongji1,A0,switch,pc,pm):  #【缸循环】循环函数的一个变种。从循环函数改编而来              
    """
    【缸】遗传算法循环，的变形
    虽然取名叫做 遗传循环，但是这里只是，每次循环中的内容罢了，这个函数里没有循环。
    
    遗传算法的核心部分，遗传算法的循环部分，每次循环要执行的东西。：生和死。
    遗传算法的循环：解码【这个里面是有建模的】，选择（生和死的抉择），交配，变异（后面两个是生），
    
    这个函数还是要进行改进的。【关于生和死的调节。需要做精细的调节】
    
    """
    
    newobj_value,b = calobjValue(pop, x_train, x_test, y_train, y_test,A0,switch)     # 解码，建模，求误差          ；   【这里有建模过程】（把2进制变成10进制）然后带入目标方程计算式子结果，obj_value中显示。 个体评价
    best_individual, best_fit,ii = best(pop, newobj_value)                            # 寻找最优
    best_individual2, best_fit2,ii2 = best_2(pop, newobj_value)		                  # 寻找次优                    ；    第一个存储最优的基因, 第二个存储最优解。不过这个要改成返回一个，pop的行号。，以便保留最优解，防止最优解在后面的过程中被改变掉。
    #newobj_value = calfitValue(newobj_value)                                         # 【按照阈值淘汰，感觉这个没有什么用途】淘汰，阈值法进行标记        ；    根据结果，淘汰一部分的不合理解。淘汰的速率也应该斟酌一下，什么样才是最好，淘汰速度，决定了收敛速度，决定了循环的代数。
    pop=selection(pop, newobj_value,b,pc,pm,ii)		                                   # 【生和死都在这里面，生和死就是对pop的操作】 新种群复制，真正淘汰，【种群一直再生长才对】        ；    【】【】应该在这里加上一个检验种群是否进化完全了。
    print("本轮最优染色体:")
    print(best_individual)
    print("染色体长度：")
    print(len(best_individual))
#    print("最优解对应的效果【这里应该是相对的，并不是绝对的误差】：")             #通过最优染色体得到的效果。
#    print(best_fit)
    pop_sum_hang(pop)                                                          #【这里也是一个出bug的地方呀】检测次轮pop有没有空的。[][]【】【】这里是要改的。。。
    
    print()
    print()
    print()
    return pop,best_individual,best_fit,best_individual2,ii2                   # 返回进化后的种群,和最优的解（即最优的特征波长）







def yichuan_tongji(pop,tongji1):                                               #这里本来设定了一个提前跳出的函数，但是没有用上。迭代次数是50次，这个是人为设定的，这样真的有很大的改进空间。
    """
    遗传算法中的统计
    用于统计每一次进化后pop的波长。
    
    输入：pop，tongji1  每一代种群的波长选择，统计数据结果的全局list
    """
    tongji=pop_tongji(pop)                                                     #用于统计pop的每个基因数，也就是每一列的求和。【】【】【感觉这个是最有价值的，比tongji1更加有价值。】
    
#    print("pop[0]:::",pop[0])
#    print("pop[1]:::",pop[1])
#    print("pop[2]:::",pop[2])
    
    print("此轮的pop各个基因的统计结果：")                                       #####################################################################################################################################
    print(tongji)                                                              #有必要看一下统计的结果。【】【】【】
    for k in range(len(tongji)):                                               #####################################################################################################################################
        tongji1[k]+=tongji[k]                                                  #tongji1是统计所有轮数的结果。【这个的价值不太高，而且随着轮数的增加，这个也会在逐渐变大。】
#        plt.figure("tongji de pop")
#        plt.bar(range(len(tongji1)),tongji1)
#        plt.pause(0.001)
    #[][]有一个进化完成的标志，就是，每次统计出来，增长都是一样的。，，，所以要在这里加一个进化完成的标志，进化完成，就不需要接下来的遗传，就直接跳出。
    #cha=[(tongji2[i]-tongji[i])*(tongji2[i]-tongji[i]) for i in range(len(tongji))]
    #tongji2=copy.deepcopy(tongji)                                             #更新统计
#        if sum(cha)<5:
#            wancheng+=wancheng
#            if wancheng==10:
#                break
    return tongji




#这里是遗传算法的本体了.
#应该独立为一个文件夹的.
def yichuanSF(pop, x_train, x_test, y_train, y_test,A0,switch,xin_pop_hang,pop_cir,pc,pm):
    """
    遗传算法
    下面是遗传算法主体循环部分。并有一些变量的统计
    
    pop第一代种群（其实可以放进这个函数里生成），
    x 训练集
    x 测试集
    y 训练集
    y 测试集 
    A0            共同的Y向量，可以认为是浓度向量
    switch        适应度函数的开关
    xin_pop_hang  种群在迭代中要维持在多少行，即种群的稳定数量
    pop_cir       种群繁衍的代数
    pc            交配概率
    pm            变异概率
    """ 

    chrom_length=pop.shape[1]                                                       #pop这个矩阵的列，也就是波长的个数                                                    #这里chrom_length是全局变量。
    tongji1=[]                                                                      #是用来累计统计的，，，这里是创建一个列表，用于求和统计的各个列的和。
    for j in range(chrom_length):
        tongji1.append(0)                                                           #这个是把上面创建的列表初始值为0
       
        
    tongji2=[]                                                                      #是用来保存上一个统计的，，，这里是创建一个列表，用于求和统计的各个列的和。
    for j in range(chrom_length):
        tongji2.append(0)                                                           #这个是把上面创建的列表初始值为0，通过这句话，就能感受到你的程序并不是很熟练。

    
    #在这里加入pop的扩建，因为第一轮生成的pop总是过小的。所以要进行复制到较大的新pop里这样就能够扩大种群了。
    #因为条件限制,采集的光谱数据量是有限的.
    #xin_pop_hang=100   这里xin_pop_hang是传进来的参数.我们可以人为更改的.            #这个量应该是在主函数开头规定好的.
    xin_pop=np.zeros(shape=(xin_pop_hang,pop.shape[1]))                              #新建的这个pop是100行的
    cnt=0
    for i in range(xin_pop_hang):                                                  #通过一遍一遍的复制,达到想要的数量.  这里是实际上应该放到数据导入那里,放在这里有点麻烦.
        if cnt>=pop.shape[0]:
            cnt=0
        xin_pop[i]=pop[cnt]                                                          #实际上就是通过复制完成了扩建。
        cnt+=1
        
#    print("pop")
#    print(pop)
#    print("xin_pop")
#    print(xin_pop)

    #wancheng=0                                                                     #是否完成进化的标志位。   
    for i in range(pop_cir):                                                        #这里传入的是种群的繁衍代数，，，，这里是循环多少代【】【】我感觉这里应该有一个迭代次数才行。这里是不是错了【】【】这里的迭代次数是认为规定的吗？？？
        #def yichuan_xunhuan(pop,x_train,x_test,y_train,y_test,tongji1,A0,switch,pc,pm):   
        print("当前循环次数：",i)
        xin_pop,best_individual=yichuan_xunhuan(xin_pop,x_train,x_test,y_train,y_test,tongji1,A0,switch,pc,pm)           #遗传算法的每一轮循环要执行的函数。
        tongji=yichuan_tongji(xin_pop,tongji1)                                      #【目前统计没有什么大的用处】遗传算法每一轮循环之后要进行的统计成分。
    return best_individual,xin_pop,tongji                                               #返回最优的特征波长（即最优的解） ,当然也要返回最后一次的种群（因为下一次的迭代是根据最后一次的种群中的波长进行的。）                   



def yichuanSF_gang(pop, x_train, x_test, y_train, y_test,A0,switch,xin_pop_hang,pop_cir,pc,pm): #【缸】遗传算法的缸变异
    """
    遗传算法【缸】变异版本
    
    下面是遗传算法主体循环部分。并有一些变量的统计
    
    pop第一代种群（其实可以放进这个函数里生成），
    x 训练集
    x 测试集
    y 训练集
    y 测试集 
    A0            共同的Y向量，可以认为是浓度向量
    switch        适应度函数的开关
    xin_pop_hang  种群在迭代中要维持在多少行，即种群的稳定数量
    pop_cir       种群繁衍的代数,也就是在循环多少次，这里已经有了。可以把它改小
    pc            交配概率
    pm            变异概率
    """ 

    chrom_length=pop.shape[1]                                                       #pop这个矩阵的列，也就是波长的个数                                                    #这里chrom_length是全局变量。
    tongji1=[]                                                                      #是用来累计统计的，，，这里是创建一个列表，用于求和统计的各个列的和。
    for j in range(chrom_length):
        tongji1.append(0)                                                           #这个是把上面创建的列表初始值为0，通过这句话，就能感受到你的程序并不是很熟练。
       
        
    tongji2=[]                                                                      #是用来保存上一个统计的，，，这里是创建一个列表，用于求和统计的各个列的和。
    for j in range(chrom_length):
        tongji2.append(0)                                                           #这个是把上面创建的列表初始值为0，通过这句话，就能感受到你的程序并不是很熟练。

    #在这里加入pop的扩建，因为第一轮生成的pop总是过小的。所以要进行复制到较大的新pop里这样就能够扩大种群了。
    #xin_pop_hang=100                                                               #这里需要人为设置
    xin_pop=np.zeros(shape=(xin_pop_hang,pop.shape[1]))                             #新建的这个pop是100行的
    cnt=0
    for i in range(xin_pop_hang):
        if cnt>=pop.shape[0]:
            cnt=0
        xin_pop[i]=pop[cnt]                                                         #实际上就是通过复制完成了扩建。
        cnt+=1
        
    print("当前这一缸的数据（输出缸中的每一条鱼）：")
    print(pop)
    print("循环中的缸xin_pop：")                                                     #遗传算法中的缸。每代用于填充这个。
    print(xin_pop)

    #wancheng=0                                                                     #是否完成进化的标志位。   
    for i in range(pop_cir):                                                        #这里传入的是种群的繁衍代数，，，，这里是循环多少代【】【】我感觉这里应该有一个迭代次数才行。这里是不是错了【】【】这里的迭代次数是认为规定的吗？？？
        #def yichuan_xunhuan(pop,x_train,x_test,y_train,y_test,tongji1,A0,switch,pc,pm):   
        print("当前循环次数：",i)

        tongji=yichuan_tongji(xin_pop,tongji1)                                      #【目前统计没有什么大的用处】遗传算法每一轮循环之后要进行的统计成分。
        xin_pop,best_individual,best_fit,best_individual2,ii2=yichuan_xunhuan_gang(xin_pop,x_train,x_test,y_train,y_test,tongji1,A0,switch,pc,pm)           #遗传算法的每一轮循环要执行的函数。
    return best_individual,best_fit,xin_pop,tongji,best_individual2,ii2             #【查找best_fit来源】返回最优的特征波长（即最优的解） ,当然也要返回最后一次的种群（因为下一次的迭代是根据最后一次的种群中的波长进行的。）                   



def xin_ceshi():        
    """                               
    #下面是从新测试一下：
    #下面是导入"新的"Y   
    #这一段没有启用。     所以这个暂且可以不用管。
    """                                                                             #下面这一段是导入x和y，用于建模，x就是光谱矩阵，y就是各个光谱对应的浓度
    A = np.loadtxt('A4.csv',delimiter=',')                                          #读入数据（相当于读入y），   #读了这么多的数据？？？哪个是x，，哪个又是y呢？？？
    
    #下面是导入"新的"矩阵X
    mat=PLS.load_Xjuzhen()
    
    #这里是随机划分训练集和测试集
    #x_train, x_test, y_train, y_test=train_test_split(mat,A,test_size=0.5)        #从新导入全新的数据，从新预测一遍
    
    #固定划分训练集和测试集
    x_train=mat[:12]
    x_test =mat[12:]
    y_train =A[:12]
    y_test  =A[12:]
    
    matcopy=copy.deepcopy(x_train)                                                 #产生一个源光谱矩阵的副本。深拷贝。
    shi=0
    for j in best_individual:                                                      #最优的一个基因进行过滤光谱。
        for k in range(matcopy.shape[0]):                                          #把mat的每一行都按照pop的一行进行过滤,这里是mat的行数。
            matcopy[k][shi]=(matcopy[k][shi])*j                                    #把mat按照模板，一列一列的进行过滤。     
        shi=shi+1                                                                  #[][]很重要，要记得清零，尤其是在内层循环，因为会跳出到外层，再跳进去这时就报错了【】【】进行下一个波长的扫描，并替换。用于过滤下一列
    print ("过滤后的光谱矩阵：")                                                                   
    print (matcopy)                                                               
    error=PLS.pls(matcopy, x_test, y_train, y_test)
    print("min_error:",error)






#normDataSet,ranges,minVals=autoNorm1(mat)                                     #normDataSet是把mat纵轴归一化的 
#normDataSet2,ranges2,minVals2=autoNorm0(mat)                                  #normDataSet2是把mat横轴归一化的。
#normDataSet1,ranges1,minVals1=autoNorm0(normDataSet)                          #normDataSet1是把mat先纵轴归一化，在横轴归一化的
##相关系数
#def cormat():
#    
#    corAmat=[]
#    plt.figure("cor_A_mat")
#    for cor in range(len(y0)):
#        corAmat.append(corrcoef(A,mat[:,cor]))                                #mat[:,i])  [][]这一层出错，有可能导致下一行有错误提示。
#        
#    plt.bar(range(len(corAmat)),corAmat)
#    #plt.plot(range(len(corAmat)),y0)





    

 





if __name__ == '__main__':  

    #按照原有的意思，我是想把所有的调节参数都放到函数的最前面，便于统一管理。
    #参数需要调节，要有经验依据才可以。
    
    
    #这里是不同的筛选标准,有的时候是按照斜率,有的时候是按照误差,有的时候是按照截距.
    #分不同阶段进行的.
    #0:("斜率")
    #1:("误差")
    #2:("截距")    
    
    
    #下面是基因的长度,也可以认为是,光谱的长度.
    chrom_length = 246      #[][在这里赋值只是形式，是没有用的。] 染色体长度，即基因的个数，【】【】【这个就不要自己规定了。】决定了结果的精度。【根据一组光谱的宽度和光谱仪的分辨率来定】，染色体上有几个基因,,光谱是247个数据。
    fit_value = []		    #个体适应度
    fit_mean = []		    #平均适应度，这里是不是查看有没有进化。
    

    #斜率
    #第一阶段
    pop_size = 50           #50【这个主要是生成第一代的时候用到。】 种群数量，【可改】，染色体个数，这个的设置应该依据什么去做呢？？？    
    switch1=0               #0,斜率适应度是斜率
    xin_pop_hang1=100       #100用于控制种群维持在多少个，即pop维持在多少行
    pop_cir1=50             #50种群繁衍的代数，原定默认为50次。，，这个繁衍代数该依据什么去设置呢？？？
    pc1=0.5                 #0.6交配概率原来是0.6 
    pm1=0.03                #0.01变异概率原来是0.01，改成0.1后能够看到一些变异带来的影响，也许能够看到影响才是最佳的状态吧。
    
    
    #截距
    #第二阶段
    pop_size2=50           #50【这个是用来生成第一代初始种群的】种群数量，【可改】，染色体个数，这个的设置应该依据什么去做呢？？？
    switch2=2              #2，截距
    xin_pop_hang2=100       #100用于控制种群维持在多少个，即pop维持在多少行
    pop_cir2=50             #50循环的代数。默认值是50次
    pc2=0.4                #0.6
    pm2=0.03               #0.01
    
    
    #误差
    #第三阶段
    pop_size3=20            #20【这个实际上是缸的数目，它要和下面的数保持一致。】【这个是用来生成第一代初始种群的】种群数量，【可改】，染色体个数，这个的设置应该依据什么去做呢？？？    
    pop_cir3=20             #20【这个实际上是缸的脚标】，多少个缸是相同的。
    switch3=1               #1：误差适应度是误差
    xin_pop_hang3=50        #50【他要与下面的参数一致】用于控制种群维持在多少个，即pop维持在多少行，这个必须和缸的里面一致才行。 
    cnt=50                  #50【每个缸里可以容纳多少条鱼】这个参数可以向前提。这个数值要等于上面的数值。
    pc3=0.5
    pm3=0.03       
    gang_xunhuan=50         #100【这个才是循环的代数】【这个是缸循环，表示让鱼儿跳的次数】种群之间的对比循环。

    


    #导入数据【这里的数据导入我写了很多函数，但是目前用到的就是这一个。应该整理和查看一下才是】    
    yy,mat,bochang,bochang0,AA,A=PLS.load_XXY_juzhen()
    yuan_bochang_00=bochang0
    
    #下面是导入矩阵X
    #mat,bochang=PLS.load_XXjuzhen()                                                #也应该输出一个“波长”的刻度。
    mat=np.array(mat)
    #print(bochang)                                                                 #输出波长刻度
   
    
    #下面是导入Y       y也就是浓度标签列                                                                 #下面这一段是导入x和y，用于建模，x就是光谱矩阵，y就是各个光谱对应的浓度
    #A = np.loadtxt('A.csv',delimiter=',')                                          #读入数据（相当于读入y），   #读了这么多的数据？？？哪个是x，，哪个又是y呢？？？
    #A= PLS.load_YY()
    #print("A:",A)
    A=np.array(A)
    
    
    
    
    
    
    
    
    
    
#################################数据与处理部分    
#是否归一化： 
                     
#    normDataSet1,ranges1,minVals1=autoNorm0(normDataSet)                      #normDataSet1是把mat先纵轴归一化，在横轴归一化的
    mat,ranges2,minVals2=autoNorm0(mat)                                        #normDataSet2是把mat横轴归一化的。
#    mat,ranges,minVals=autoNorm1(mat)                                         #normDataSet是把mat纵轴归一化的 
#进行正交信号校正
    B=[A]
    mat=OSC.osc(mat,B)
#    #用噪声矩阵替代X光谱矩阵,目前是（5，5）的一个噪声矩阵。
#    mat=load_zaoshengjuzhen() 
#    print("mat:",mat)
    chrom_length=mat.shape[1]                                                       #【】基因的个数等于mat的列数，中间的变量最好不要自己去赋值，要让程序自己找到合适的上下文参数【】【】
    print("染色体中基因的个数chorm_length：",chrom_length)

    
    
    #产生第一代种群，这个是用窗口迭代平移的方法。。
    pop = geneEncoding2(pop_size, chrom_length)                                     #用于产生第一代，也就是初始化，pop_size是染色体的数量，chrom_length是染色体有几个基因组成
    #print("第一代种群pop:",pop)       
    
    



#    ##随机划分训练集和测试集
#    x_train, x_test, y_train, y_test=train_test_split(mat,A,test_size=0.5)         #【】【】划分训练集测试集，这一次随机划分后，以后都不再变。。，，，这个是一个库函数？？ ，，，，这里能够看出是A和RON进行建模的。
    #训练集和测试集通过切片固定划分
    huafen = input("输入训练集划分个数（剩下的归测试集所有）例如：10：") 
    huafen=int(huafen)
    x_train=mat[:huafen]                                                            #【】【】【】如果切片是[:2] 则只是0，1，却不包含2.              
    x_test =mat[huafen:]
    y_train=A[:huafen]
    y_test =A[huafen:]
    #转化格式
    x_train=np.array(x_train)
    x_test =np.array(x_test)
    y_train=np.array(y_train)
    y_test=np.array(y_test)
    

    
    
    
    
    A0=A
    #第一轮遗传算法开始
    best_individual,pop,tongji=yichuanSF(pop, x_train, x_test, y_train, y_test,A0,switch1,xin_pop_hang1,pop_cir1,pc1,pm1)                                              #这里是遗传算法主体，这里应该有返回最优的值才对呀。就是返回最优的 染色体。  0：斜率 1：误差 2：截距
    taotai_1=copy.deepcopy(best_individual)                                    #深度复制，第一次淘汰，即 淘汰_1
        
#    plt.figure('zuiyou_fangan_1')
#    plt.bar(yuan_bochang_00, best_individual)                                    #这里便是画图了，前面的是波长坐标，后面的是0和1代表着是否选中。
#    plt.xlabel(u'波长')
#    plt.ylabel(u'是否选中，其实是是否没有选中？')
#    #plt.show()       
    
#这里是第二轮搜索 ，，，我希望把第二轮的搜索放到与第一轮同等地位，
#也就是每次搜索，都是在全谱的基础上去做。，都只做出一个滤网，然后在第三轮的时候去过滤。【2019.03.07】
    


##   创建第一个滤网的过程。     
#    #要记住pop实际上是种群，也就是一个群组，好几个染色体构成的。
#    #根据pop的有无，从新过滤，然后创建初始的种群，之后进行迭代。在这种情形下，是不是应该设置一个开关，用来调整遗传算法中的适应度函数是哪一个？？？
#    
#    youxuan_bochang1=[]                                     #创建新一轮的滤网。
#    
#    #pop就是种群，应该找pop各个基因的统计结果做滤网才好使。
#    #滤网的阈值选定过程：
#    tongji_cnt=0
#    tongji_sum=0
#    for i in tongji:
#        tongji_sum+=i
#        tongji_cnt+=1
#    tongji_pingjun=tongji_sum/tongji_cnt
#    tongji_pingjun=3                                        #【需要人为改动】
#    print("第一个滤网阈值大小",tongji_pingjun)
#    
#    
#    
#    #滤网的创建过程：    
#    youxuan_bochang1_len=0    
#    for i in tongji:
#        if i>tongji_pingjun:                                #这个是种群的统计，这里设置的阈值(平均值)有点低。应该按实际需求去设置才好。
#            youxuan_bochang1.append(0)
#            
#        else:
#            youxuan_bochang1.append(1)
#            youxuan_bochang1_len+=1                         #这个是为了确定优选波长内有几个1
#        
#    print("第一个滤网")
#    print(youxuan_bochang1)
            
    
    
    
#########################################################################################################  
#第二轮开始了。 

        
    
    #产生第一代种群，这个是用窗口迭代平移的方法。。
    pop_2 = geneEncoding2(pop_size2, chrom_length)                                     #用于产生第一代，也就是初始化，pop_size是染色体的数量，chrom_length是染色体有几个基因组成
    #print("第一代种群pop:",pop)       
            

    #重新调用遗传算法，并根据另一个适应度函数去计算 ，斜率
    best_individual,pop,tongji=yichuanSF(pop_2, x_train, x_test, y_train, y_test,A0,switch2,xin_pop_hang2,pop_cir2,pc2,pm2)                                             #这里是遗传算法主体，这里应该有返回最优的值才对呀。就是返回最优的 染色体。  0：斜率 1：误差 2：截距
    taotai_2=copy.deepcopy(best_individual)                                    #这个也是深度复制，淘汰_2
  
        
#    plt.figure('zuiyou_fangan_2')
#    plt.bar(yuan_bochang_00, best_individual)                                  #这里便是画图了，前面的是波长坐标，后面的是0和1代表着是否选中。
#    plt.xlabel(u'波长')
#    plt.ylabel(u'是否选中，其实是是否没有选中？')
    
  
    
##############################################################################################################################    
#这里是第三轮搜索了。【这是最后一轮了】
    print("第三轮开始：")
    print()
    print()    
    
    
#    现在全部注释掉，这里是创建滤网的过程。
#    #要记住pop实际上是种群，也就是一个群组，好几个染色体构成的。
#    #根据pop的有无，从新过滤，然后创建初始的种群，之后进行迭代。在这种情形下，是不是应该设置一个开关，用来调整遗传算法中的适应度函数是哪一个？？？
#    
#    youxuan_bochang1=[]                                                            #【其实我在想，要不要创建最优？？？】创建新一轮的滤网。
#    
#    #pop就是种群，应该找pop各个基因的统计结果做滤网才好使。
#    #寻找滤网阈值：
#    tongji_cnt=0
#    tongji_sum=0
#    for i in tongji:
#        tongji_sum+=i
#        tongji_cnt+=1
#    tongji_pingjun=tongji_sum/tongji_cnt
#    tongji_pingjun=3                                                               #【因为不知道收敛的度，所以设置成这个。这个是一个保守的值，并不是最好的值。将来可以改成2或者改成1也是可以的。】【需要人为改动】，目前种群中最优的染色体至少是3个。
#    print("第一个滤网阈值大小",tongji_pingjun)
#     
#        
#    #创建滤网过程：
#    youxuan_bochang1_len=0    
#    for i in tongji:
#        if i>tongji_pingjun:                                #这个是种群的统计，这里设置的阈值(平均值)有点低。应该按实际需求去设置才好。
#            youxuan_bochang1.append(0)
#        else:
#            youxuan_bochang1.append(1)
#            youxuan_bochang1_len+=1                         #这个是为了确定优选波长内有几个1
#        
#    print("滤网")
#    print(youxuan_bochang1)
#            
#    
#    
    #过滤这个要进行保留的。
    #但是今天先不用。
    #xtrain_guolu1,xtest_guolu1=calobjValue_1.guolu(youxuan_bochang1,x_train,x_test)  #【现在想想，这个也是有问题的】根据新的滤网，把训练集合测试集都过滤一遍。
                                                                                      #如果用滤网直接滤掉，那么就会只在这个小的范围内进行搜索了。因为其他的数据真的就不存在了。
    

    
    #产生第一代种群，这个是用窗口迭代平移的方法。。
    pop_2 = geneEncoding2(pop_size3, chrom_length)                                     #用于产生第一代，也就是初始化，pop_size是染色体的数量，chrom_length是染色体有几个基因组成
    #print("第一代种群pop:",pop)  



    print("pop_size3",pop_cir3)
    print("cnt",cnt)
    print("chrom_length",chrom_length)
    #造缸的过程：                                                               #这个要重现编写一下？？？
    gang=np.zeros(shape=(pop_size3,cnt,chrom_length))                          #参数1：有几种鱼，就有几个缸； 参数2：每个缸盛放的鱼数； 参数3：鱼身体有多长。【也就是染色体长度】
    for i in range(pop_size3):                                                  
        for k in range(cnt):
            gang[i][k]=pop_2[i]                                                #把每种鱼装入各自的缸里面。
            print("i",i)
            print("k",k)
            
            
            
            
            
#这里应该编写一个排序函数，要把每一轮的结果都排一下。   
#对每一缸的鱼都进行遗传算法，遗传算法的循环次数可以设置少一些，定位10
#把每一缸都进化完成之后进行相应的对比，要把最优秀的一缸里的第二优异的鱼放到其他各个缸中，然后
#再次进行遗传算法，然后就是这样。  循环上面的操作，只到找到较为优秀的解为止。【或者各个缸的数据相差不大时，就可以停止了。】


    for xunhuan in range(gang_xunhuan):                                            #这个是人为控制的，用于进行鱼的跳跃次数。                                        
        print("当前gang_xunhuan:",xunhuan)                                         #这个是当前的大循环所处次数，也就是鱼儿跳了几次。
        plt.close('all')
        
        #用于盛放每一缸里的最优结果
        gang_yichuanxunhuan=[]
        yu_ciyou=[]                                                                #用于存放每轮次优的鱼，是为了得到最终的鱼。
        yu_zuiyou=[]                                                               #这个是最优的鱼集合（每一缸里最优的鱼。）
        cnt_xulie_error=[]                                                         #这个是每个缸里最优鱼，所建模表现出来的误差。【然后是根据这个的误差，挑选出最优的缸。【需要先找到最优缸，才能在缸中找到最优的鱼】】
        
        for gangshu in range(pop_cir3):                                            #这里是有多少个缸，，，其实如果想让每个缸多循环，就需要在下面的函数中加一个循环才对。
            #多循环，应该把下面的函数循环？？
#            print("当前xunhuan值                    ",xunhuan)
#            print("当前循环gangshu的值,应该等于，缸数",gangshu)                      #为什么一开始总是0呢？？
            best_individual,best_fit,gang[gangshu],tongji,best_individual2,ii2=yichuanSF_gang(gang[gangshu], x_train, x_test, y_train, y_test,A0,switch3,xin_pop_hang3,5,pc3,pm3)         #这里是遗传算法主体，这里应该有返回最优的值才对呀。就是返回最优的 染色体。  0：斜率 1：误差 2：截距
            gang_yichuanxunhuan.append(best_fit)                                   #【这个是有问题的，因为未必是误差？？？？】把每个缸中最优的表现值保存起来。
            yu_ciyou.append(best_individual2)                                      #把每一缸中次优的鱼保存气来。
            yu_zuiyou.append(best_individual)                                      #把每一缸中最优的鱼保存起来。
            
        for souxun_you in yu_zuiyou:
            xtrain_guolu,xtest_guolu=calobjValue_1.guolu(souxun_you,x_train,x_test)   #这里面本不应该包含建模的。但是guolu里面有建模。编程习惯不太好呀，之所以是这样，原因在于guolu里面有了循环。
            score_r2_1,score_r2,e1,e,error,n_components,pls_k,pls_b=PLS.pls(xtrain_guolu, xtest_guolu, y_train, y_test,A)         
            cnt_xulie_error.append(e1[0])                                             #【这里加上脚标的原因也很不明白，是以前程序遗留的问题】把每条鱼儿的误差都放进去，然后把误差组成序列。
            print("每条最优鱼儿的误差：",e1)
            print("当前xunhuan值                   ",xunhuan)                           #为了查看进度
            print("当前循环gangshu的值,应该等于，缸数",gangshu) 
        
        cnt_xulie_error=np.array(cnt_xulie_error)
        index=np.argsort(cnt_xulie_error)                                          #这里是对序列排序了，从小到大的排序。【返回的是索引，实际上就是在找最优的缸。】    这里是误差，所以， 误差越小，就是最优的。                            
                                       
                                        
        
#        print("输出排序大小的脚标：")
#        print(index)                            
        
#        print("输出次优鱼的序列：")
#        for i in yu_ciyou:
#            print(i)
    
        
        #找到最优的鱼，
        yu_zui=yu_zuiyou[index[0]]
        
        #找到次好的鱼,找到你想要的那个。
    
        yu=yu_ciyou[index[1]]
#        print("鱼")
#        print(yu)
        #把这条鱼复制到每一个缸里面,这里也就是gang “缸” 的更新过程。 但是缸的交叉和变异似乎没有保留下来？？？
        for i in gang:
            i[-1]=yu
#            print("查看每一个鱼缸：是不是由了跳过来的鱼呢：")
#            print(i)
        print("当前xunhuan值                    ",xunhuan)
        print("当前循环gangshu的值,应该等于，缸数",gangshu)                      #为什么一开始总是0呢？？
    




##   关于如何获取最后的答案，我们可以先去搜索，然后在最后阶段进行去除，这个来说是比较方便的。【也就是三个搜索方面都是相对独立的，在最后搜索的结果中去除前面两轮的结果就行了】
     ##所以这个是在最优鱼中，去除前面两个的滤网，这样对于编程时最好实现的。   
    #绘图部分，绘图部分，绘图部分，绘图部分。
    
    #下面这里的绘图还是有些问题的，然后就是重新建模部分了，评估之后一切都可以好过了。
    
    #这里是最优波长（yuan_bochang0）的绘制图，也就是筛选结果
    plt.figure('yu_zui')
    plt.bar(yuan_bochang_00, yu_zui)  
    plt.xlabel(u'波长')
    plt.ylabel(u'是否选中')
    plt.show()      



##   反过滤，这里先注释掉。
#    yuan_bochang0=calobjValue_1.fan_guolu(youxuan_bochang1,yu_zui)            #反过滤，第一个系数是滤网，第二个系数是最优的个体。
#    print("原波长：")
#    print(yuan_bochang0)
#    print("原波长长度yuan_bochang0",len(yuan_bochang0))
    
    
    
    
#    print("滤网长度:")  
#    print(youxuan_bochang1)
#    print("滤网长度：",len(youxuan_bochang1))
    
    

    
    
    
    
    
    
    
#    #绘图部分，绘图部分，绘图部分，绘图部分。
#    
#    #下面这里的绘图还是有些问题的，然后就是重新建模部分了，评估之后一切都可以好过了。
#    
#    #这里是最优波长（yuan_bochang0）的绘制图，也就是筛选结果
#    plt.figure('youxuanbochang_3')
#    plt.bar(yuan_bochang_00, yuan_bochang0)  
#    plt.xlabel(u'波长')
#    plt.ylabel(u'是否选中')
#    plt.show()     
    
    

    
    
    
    
    plt.close('all')
    
    #下面是从新建模的了。
    xtrain_guolu,xtest_guolu=calobjValue_1.guolu(yu_zui,x_train,x_test)                     #这里面本不应该包含建模的。但是guolu里面有建模。编程习惯不太好呀，之所以是这样，原因在于guolu里面有了循环。
    score_r2_1,score_r2,e1,e,error,n_components,pls_k,pls_b=PLS.pls(xtrain_guolu, xtest_guolu, y_train, y_test,A)    
    print("score_r2_1:",score_r2_1)
    print("score_r2:",score_r2)
    print("RMSEC:",e1)
    print("RMSEP:",e)
    print("min_error:",error)
    print("n_components,pls_b,pls_k:",n_components,pls_b,pls_k)
    
    xunzhao_bochang(yu_zui,yuan_bochang_00)                                   #前一个参数是滤网，后一个参数是波长矩阵，查找过滤后的波长。
    
     
    
    
    
    #这里是最优波长（yuan_bochang0）的绘制图，也就是筛选结果
#    plt.figure('yu_zui')
#    plt.bar(yuan_bochang_00, yu_zui)  
#    plt.xlabel(u'波长')
#    plt.ylabel(u'是否选中')
#    plt.show()      
    
    
    plt.figure("youxuan")
    plt.title("优选波长",size=23)
    plt.tick_params(labelsize=20)                                              #这个是调整坐标字体大小的。
    plt.xlabel(u'各个波长',size=25)
    plt.ylabel(u'是否选中',size=25)
    plt.bar(yuan_bochang_00,yu_zui)   
    
  
    
    plt.figure('taotai1')
    plt.title("淘汰波长1",size=23)
    plt.bar(yuan_bochang_00, taotai_1)                                         #这里便是画图了，前面的是波长坐标，后面的是0和1代表着是否选中。
    plt.xlabel(u'波长',size=25)
    plt.ylabel(u'是否选中，其实是是否没有选中？',size=25)
    
    
    plt.figure('taotai2')
    plt.title("淘汰波长2",size=23)
    plt.bar(yuan_bochang_00, taotai_2)                                         #这里便是画图了，前面的是波长坐标，后面的是0和1代表着是否选中。
    plt.xlabel(u'波长',size=25)
    plt.ylabel(u'是否选中，其实是是否没有选中？',size=25)
    
    
"""    
    很奇怪的一点，为什么这里的注释符号" 不能缩进，一缩进，就会报错。
    
    #下面是重新建模的了。
    youxuan_bochang=best_individual
    xtrain_guolu,xtest_guolu=calobjValue_1.guolu(youxuan_bochang,x_train,x_test)                     #这里面本不应该包含建模的。但是guolu里面有建模。编程习惯不太好呀，之所以是这样，原因在于guolu里面有了循环。
    score_r2_1,score_r2,e1,e,error,n_components,pls_k,pls_b=PLS.pls(xtrain_guolu, xtest_guolu, y_train, y_test,A)    
    print("score_r2_1:",score_r2_1)
    print("score_r2:",score_r2)
    print("RMSEC:",e1)
    print("RMSEP:",e)
    print("min_error:",error)
    print("n_components,pls_b,pls_k:",n_components,pls_b,pls_k)
    
    xz.xunzhao_bochang(youxuan_bochang,bochang0)                               #查找过滤后的波长。这里会打印出过滤后的波长来的。
    
"""
    
    
    
"""    
    print("遗传算法统计波长结果tongji1")
    print(tongji1)
    print("最好的波长组合best_individual")                                      #除了要返回最好的波长组合之外，，还要返回最优的主成分的个数。##################################################################################################################
    print(best_individual)
    print("最好的误差best_fit")                                                 #print(obj_value[1])
    print(best_fit)
    
    
    
    plt.figure("tongji de pop")
    plt.bar(range(len(tongji1)),tongji1)                                       #这里的tongji1是返回来的累积值             
    

    
    plt.figure("best_individual")                                              #画一个最佳染色体的图。
    plt.bar(range(len(best_individual)),best_individual)
    plt.show()
    
    #xin_ceshi()                                                               #开始新一轮的测试。

"""

#其实算法可以有多种改进的。比 如加入刺激-反馈。