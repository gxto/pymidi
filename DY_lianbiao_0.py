# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:43:06 2020

@author: python


这个是 "链表"  目前是我想到的最好的代表音乐的方式. 我也不知道二维数组好不好用.
总之,这个让我想起来了,操作系统中,每个优先级节点下面都挂有任务...???


关于链表,参考的是:https://www.cnblogs.com/king-ding/p/pythonchaintable.html
还参考了之前自己写的Python链表东西.
"""



class Node():                   #node实现,每个node分为两部分:一部分含有链表元素,成数据域;另一部分为指针,指向下一个
  """
  这里是建立链表的一个节点类
  """
  #__slots__=['_item','_next']   #限定node实例的属性???   这个元素就是有两部分组成,,,一个指针一个数据,,,但是链表头就不是这样了
  def __init__(self,item):
    self._item=item             #这里是节点的数据部分. 
    #下面是音乐的几个参数
    self._data_channel=0 
    self._data_note=60
    self._data_velocity=64
    self._data_time=240
    self._next=None             #node的指针部分默认指向none,这个是单链表,所以每个元素只有一个指针
  def getItem(self):      
    return self._item
  #下面是获取参数的方法
  def getDataChannel(self):      
    return self._data_channel
  def getDataNote(self):      
    return self._data_note
  def getDataVelocity(self):      
    return self._data_velocity
  def getDataTime(self):      
    return self._data_time

  def getNext(self):
    return self._next
  def setItem(self,newitem):
    self._item=newitem
  #下面是设置参数的方法
  #这里newnext是节点类
  #因为_next扮演的是指针,指针就要指向节点类的
  def setNext(self,newnext):
    self._next=newnext
     
    
    
    
class SingleLinkedList():   #单链表,,,,python支持在函数中间定义变量,而且还不用定义类型,随用随取,所以你看见一个变量的时候,就表明此刻就有这个变量了
  """
  创建链表的类
  类一创建,就会调用构造函数init
  """
  def __init__(self):
    #这里链表的类,只有一个内部参数,就是指针,
    #这个指针,指向了当前在哪个节点.
    self._head=None         #初始化为空链表,空链表实际上不包含node,,只有一个空的头 头里面有head指针(用于指向第一个node),有current指针(用于遍历node)???
  def isEmpty(self):        #检测链表是否为空,
    return self._head==None       
  def size(self):
    current=self._head
    count=0
    while current!=None:
      count+=1
      current=current.getNext()
    return count
  def travel(self):        #输出每个node的值
    current=self._head
    while current!=None:
      print (current.getItem())
      current=current.getNext()
  def add(self,item):            #在链表端段添加元素
    #这里调用了Node这个class
    #这里temp,就是一个类啦.
    temp=Node(item)              #创建一个node,
    #temp这个节点类,调用了自己的setNext函数.
    temp.setNext(self._head)     
    #这里_head是链表类的唯一参数,起到了指针的作用.
    #这里的参数_head被赋值了temp这个类,模拟了链表的"指针"_head指向了temp这个节点
    #这里_head并不是真正的指针,只是扮演了指针的角色
    self._head=temp              
 
  def append(self,item):         #在链表尾部添加元素
    #创建了一个节点的类temp,
    #这个节点一开始是离散的,它的下一个是None
    temp=Node(item)              
    if self.isEmpty():
      #这里_head是链表类的唯一参数,起到了指针的作用.
      #这里的参数_head被赋值了temp这个类,模拟了链表的"指针"_head指向了temp这个节点
      #这里_head并不是真正的指针,只是扮演了指针的角色  
      #如果链表为空,就让链表的指针指向唯一的,刚建立的节点temp
      self._head=temp            
    else:
      #如果不是空的, 就创建一个current变量,用来扮演指针.
      current=self._head        
      #current用来查它自己是不是最后的节点(最后的节点指向None),因为要找最后一个节点,
      #找到最后节点,然后创建加入一个新的节点.
      while current.getNext()!=None:
        current=current.getNext() 
      #把新建立的节点类temp加入这里.  
      #此时temp就是链表中最后一个节点了.
      current.setNext(temp)       
  def search(self,item):          #检索元素是否在链表中
    current=self._head
    founditem=False
    while current!=None and not founditem:   #如果我想在a>0或者b>0且a,b不同时大于0的情况下返回True:(a>0 or b>0) and not (a>0 and b>0)
      if current.getItem()==item:
        founditem=True
      else:
        current=current.getNext()
    return founditem
  def index(self,item):         #索引元素在链表中的位置
    current=self._head
    count=0
    found=None
    while current!=None and not found:  #not优先级大于and大于or  and两个都为真才是真
      count+=1
      if current.getItem()==item:
        found=True
      else:
        current=current.getNext()
    if found:
      return count
    else:
      raise (ValueError,'%s is not in linkedlist'%item )      
  def remove(self,item):        #删除链表中的某项元素
    current=self._head
    pre=None
    while current!=None:
      if current.getItem()==item:
        if not pre:
          self._head=current.getNext()
        else:
          pre.setNext(current.getNext())
        break
      else:
        pre=current
        current=current.getNext()           
  def insert(self,pos,item):    #链表中插入元素
    if pos<=1:
      self.add(item)
    elif pos>self.size():
      self.append(item)
    else:
      temp=Node(item)
      count=1
      pre=None
      current=self._head
      while count<pos:
        count+=1
        pre=current
        current=current.getNext()
      #节点temp加入了链表了.
      #关于链表中的赋值,还是有点问题
      pre.setNext(temp)
      temp.setNext(current)
 
if __name__=='__main__':
  a=SingleLinkedList()    #建立类的对象,,,实际上就是用 SingleLinkedList类扣出了一个蛋糕a,,,就是建链表头的过程
  for i in range(1,10):
    print("DY_lianbiao_0:","输出循环的次数:",i)
    a.append(i)
  print (a.size())
  a.travel()
  print (a.search(6))
  print (a.index(5))
  a.remove(4)
  a.travel()
  a.insert(4,100)
  print("输出")
  a.travel()

    
    
    
    
    
    
    
    
    
    
    
    