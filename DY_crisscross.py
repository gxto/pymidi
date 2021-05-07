# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:15:25 2021

@author: python

作用:
    交配,交叉文档



以上代码主要进行了3个操作，首先是计算个体适应度总和，然后在计算各自
的累积适应度。这两步都好理解，主要是第三步，转轮盘选择法。这一步首先是
生成基因总个数0-1的小数，然后分别和各个基因的累积个体适应度进行比较。
如果累积个体适应度大于随机数则进行保留，否则就淘汰。这一块的核心思想在于：
一个基因的个体适应度越高，他所占据的累计适应度空隙越大，也就是说他越容易被保留下来。

选择完后就进行交配和变异，这个两个步骤很好理解。就是对基因序列进行改变，只不过改变的方式不一样。
"""
import random

# 自己的库
import DY_global as Dgl


#难就难在，复制也是增加，交叉也是增加。如何才能够统一起来，然后控制这个量呢？？？控制这个增加的量=减少的量  目的是维持鱼池里鱼的数量是不变的.
#交叉产生的增量是不固定的，变异带来的增量也是不容易控制的，复制产生的增量尚且能够控制（但是也要选取，哪些量要去控制才行。）
#交叉产生的增量+变异产生的增量+复制产生的增量=总增量  计算完总的增量之后，然后再根据增量确定减的量。减少也是有学问的，减少哪些才是科学的呢？
#对于减来说，除了有数量的规定之外，是不是还应该有其他的规定呢？？比如减是按照种类什么的，或者按照一个标准阈值进行减的操作。这样就是加被动了。？？？

def crossover(list_2d, pc,ii,new_2d,new_cnt):
    """
    传入的是pop和交叉概率pc。
    list_2d:就是种群,是一个二维数组
    pc:就是交差概率
    ii:最优的那个,最优的进行交配的概率应该提高，同时也应该保留父代才是。为了防止最优秀的被破坏,需要进行保存.
    new_2d:传进去是为了让新生成的个体存入到xin_pop中
    new_cnt:是为了记录有多少个新个体的生成
    过程:
        随机生成一个数,如果这个数字小于pc,就说明要进行交叉,
        交叉的时候是,第i个和第i+1个,分别切成两段,然后进行互换.
        
    # 这里实际上也是有bug的因为他这里的交叉是从pop中相邻的两个行进行的交叉，但谁又知道这两个是不是优秀的呢？
    # 解决方法是,最好进行一个排序.
    """
    list_2d_len = len(list_2d)                                                 # 这里大致可以理解为list_2d有多少行。
    for i in range(list_2d_len - 1):                                           # 这里还是有很多函数没有经过验证的，虽然是从网上下载的。这里为什么要减1呢？？？
        if i==ii:                                                              # 最优的没有进行交叉，这也是一个失误的。
            continue                                                           # 这里是为了防止把最优的解因为交叉而导致破坏，所以如果是最优的，那么就不进行改变。
        if(random.random() < pc):
            
            cpoint = random.randint(0,len(list_2d[0]))
            temp1 = []
            temp2 = []
            temp1.extend(list_2d[i][0:cpoint])                                 # extend方法是,在temp1序列的尾部追加list_2d的一部分序列.
            temp1.extend(list_2d[i+1][cpoint:len(list_2d[i])])
            temp2.extend(list_2d[i+1][0:cpoint])
            temp2.extend(list_2d[i][cpoint:len(list_2d[i])])
            list_2d[i] = temp1
            new_cnt+=1                                                         # 代表有一个新式个体诞生
            if new_cnt<(new_2d.shape[0]-1):
                new_2d[new_cnt]=list_2d[i]
            
            list_2d[i+1] = temp2
            new_cnt+=1                                                         # 代表有一个新式个体诞生
            if new_cnt<(new_2d.shape[0]-1):
                new_2d[new_cnt]=list_2d[i+1]
    return new_2d,new_cnt




# 进行精简之后
def crossover_2(list_2d, pc):
    """
    传入的是pop和交叉概率pc。
    list_2d:就是种群,是一个二维数组
    pc:就是交差概率
    
    过程:
        随机生成一个数,如果这个数字小于pc,就说明要进行交叉,
        交叉的时候是,第i个和第i+1个,分别切成两段,然后进行互换.
        
    # 这里实际上也是有bug的因为他这里的交叉是从pop中相邻的两个行进行的交叉，但谁又知道这两个是不是优秀的呢？
    # 解决方法是,最好进行一个排序.,默认最优的是在第一个,就是这样... 也可以把所有的都保存下来,不淘汰,淘汰有专门的函数.
    
    # 还需要控制鱼池里面鱼的总数.但是总数的控制是需要在排完序之后进行去除的,
      这里能生成多少个,就生成多少个.不进行数量的限制,所以不需要传入数据什么的.
      
    # 这里可能有个bug,就是交叉之后,连接处,是否能够和谐,还是一个问题呀...
    """
    
    
    list_2d_len = len(list_2d)                                                 # 这里大致可以理解为list_2d有多少行。
    for i in range(list_2d_len - 1):                                           # 这里还是有很多函数没有经过验证的，虽然是从网上下载的。这里有减一
        if(random.random() < pc):
            
            cpoint = random.randint(0,len(list_2d[0]))
            temp1 = []
            temp2 = []
            temp1.extend(list_2d[i][0:cpoint])                                 # extend方法是,在temp1序列的尾部追加list_2d的一部分序列.
            temp1.extend(list_2d[i+1][cpoint:len(list_2d[i])])
            temp2.extend(list_2d[i+1][0:cpoint])
            temp2.extend(list_2d[i][cpoint:len(list_2d[i])])
            Dgl.crossover_new_2d.append(list_2d[i])
            Dgl.crossover_new_2d.append(temp1)
            Dgl.crossover_new_2d.append(temp2)
        else:
            # 这样的话,无论有没有交叉,所有的都会保存在全局变量里面了.
            Dgl.crossover_new_2d.append(list_2d[i])
    # 其实没有必要返回值的...
    #return Dgl.crossover_new_2d

if __name__ == '__main__':
    list_2=[[1,1,1,1,1,1],
            [2,2,2,2,2,2],
            [3,3,3,3,3,3],
            [4,4,4,4,4,4],
            [5,5,5,5,5,5]]
    crossover_2(list_2, 0)
    print(Dgl.crossover_new_2d)
    Dgl.crossover_new_2d=[]
    print(Dgl.crossover_new_2d)