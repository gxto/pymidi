import numpy as np

a=[1,2,3]
#print("输出list:",a)
#b=np.array(a)
#print("输出转换后的array",b)
#print("输出array的一个元素",b[1])
#c=b.tolist()
#print("输出转换成的list",c)



# 关于for的一些用法
#for i in range(7):
#    print(i)
#
#print()
#
#for i in range(len(a)):
#    print(i)


# 关于list的行列数
a=[] #一维
b=[
   [[1,1],[3,3]],
   [[3],[4]]
  ]#二维
print(b)
print(np.array(b).shape)#List a 的维数（输出为1）
#print(len(np.array(b).shape(1)))#List b 的维数（输出为2） 


c=[1,2,3,4,5,6,7,8]
print("输出c切片",c[0:5])