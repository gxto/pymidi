# encoding=utf-8
'''
绘制图形
'''
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

#names = ['5', '10', '15', '20', '25']
#x = range(len(names))
#y = [0.855, 0.84, 0.835, 0.815, 0.81]
#y1=[0.86,0.85,0.853,0.849,0.83]
##plt.plot(x, y, 'ro-')
##plt.plot(x, y1, 'bo-')
##pl.xlim(-1, 11)  # 限定横轴的范围
##pl.ylim(-1, 110)  # 限定纵轴的范围
#plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'y=x^2曲线图')
#plt.plot(x, y1, marker='*', ms=10,label=u'y=x^3曲线图')
#plt.legend()  # 让图例生效
#plt.xticks(x, names, rotation=45)
#plt.margins(0)
#plt.subplots_adjust(bottom=0.15)
#
#plt.xlabel(u"time(s)邻居") #X轴标签
#plt.ylabel("RMSE") #Y轴标签
#plt.title("A simple plot") #标题
#
#plt.show()

def plot_broken(name,data):
    '''
    通过传递一个数组,然后就可以绘制图形
    绘制的是一个折线图
    name: 传入的是,图片画布的名字
    data: 传入的是,一个一维数组
    '''
    plt.figure(name)
    x=range(len(data))
    plt.plot(x,data)  
    plt.show()
    
    
# 绘制饼状图    
def pit_chart(name,values_dic):
    # 传入的是字典,然后绘制成饼状图
    # 传入的第一个参数是name,代表画布的名字
    # 传入的values_dic是一个字典.也就是每个元素:及元素的在一首曲子中出现次数
    
    # 将画布设置成正方形,则绘制的饼图是正圆
    plt.figure(name,figsize=(6,6))
    # keys()函数作用:返回字典的键为list
    keys=values_dic.keys()
    # values()函数用法:返回字典的值为列表
    values=values_dic.values()
    # 绘制饼状图,每个扇形距离圆心的距离
    # 用for,有几个扇形,就有几个0.01,代表每个扇形都距离圆心是0.01
    explode=[]
    for i in keys:
        explode.append(0.01)

    # 绘制饼图,把设置好的参数都传进来.调用plt.pie()绘制饼状图.
    # autopct:自动添加百分比显示.
    plt.pie(values,explode=explode,labels=keys,autopct='%1.1f%%') 
    # 绘制标题
    plt.title(name)
    # 显示图片
    plt.show()
    
    
    
    
    
    

if __name__ == '__main__':
    name="data"
    data=[1,-2,3,-4,5,-6,7,-8]
    plot_broken(name,data)
    
    
    
    name='111'
    values_dic={"apple":6,"banana":8,"pear":6}
    pit_chart(name,values_dic)




























