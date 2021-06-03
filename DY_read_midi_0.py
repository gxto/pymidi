# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:36:48 2020

@author: GXTon (bilibili 和 博客园)

作用: 把一个midi文件转换成
      二维音符序列和一维时间序列


要以什么样的形式表示midi, 是要用二维数组吗???
我是这样想的,让他输出下面的格式:
1,第一时刻的音符序列
2,第二时刻的音符序列
3,第三时刻的音符序列
4,第四时刻的音符序列
...


总是用他原来的库输出的是音轨,但是我想最终输出数组,这样是最好处理的.
总之感觉用链表是好的,用链表可以让每个音符的所有元素都好调用起来.


"""

import mido
import copy

import DY_global as Dgl

'''
输出每个midi文件中的每个动作
'''
def send_msg():
    mid=mido.MidiFile("DY_kanong.mid")                 # 返回midi对象
    for i, track in enumerate(mid.tracks):             # 用于遍历,组合成索引序列.
        print('Track {}: {}'.format(i, track.name))    # 输出:Track 0: Piano 1
        for msg in track: 
            print(msg)


# 默认传入的曲子是:卡农
def midi_read(midi_file="DY_kanong.midi"):
    '''
    输入:midi_file,midi文件的名字及扩展名 是字符串格式才行.
    输出:midi文件的音符二维序列 和 midi文件每个音符对应的时间一维序列
    目前还是不很完善,
    这样建模不能完美复原曲子,因为会有 note_on 和 note_off 不是紧挨着成对出现的情况.
    关于时间序列,记录的是每个音符占用的时长.而不是相对于原点的时间点.
    '''
    mid=mido.MidiFile(midi_file) # 返回的是midi对象
    hang=0  # 行
    lie=0   # 列
    note_list_in=[]    # 先初步建立一个序列，用于存储一行音符数据。(某一时刻的音符,存在这行一维序列里面)
    note_list_ex=[]    # 先初步建立一个序列，用于存储整个音符数据。(整首曲子的音符都存在这个二维序列里面)
    # 存储时间的序列
    time_list=[]
    action_last=0   # 上轮动作状态，0 表示没有按下； 1 表示按下；
    action=0        # 本轮动作状态， 0 表示没有按下； 1 表示按下；
    print("位于:DY_read_midi_0.py中midi_read函数")
    for i, track in enumerate(mid.tracks):             # 用于遍历,组合成索引序列.
        print('Track {}: {}'.format(i, track.name))    # 输出:Track 0: Piano 1
        for msg in track:
  
            #print("########")
            # 用于显示midi文件的每个动作
            print(msg)
            # 这里msg可以认为是，每一条动作，就代表了对钢琴键盘的一次操作。
            # 可以是按下，也可以是松开。
            # 例如下面是输出的东西：
            # note_on channel=0 note=77 velocity=80 time=0
            # note_off channel=0 note=77 velocity=64 time=12
            # 这里的msg,是：class 'mido.messages.messages.Message'类型的
            # msg里面不只包括 note_on 和 note_off 还会包含其他的信息.这里解码的时候要注意!!!
            # 读取msg中的参数:
            #print("type",msg.type)
            #print("channel",msg.channel)
            #print("note",msg.note)
            #print("velocity",msg.velocity)
            #print("time",msg.time)            
            '''
            这个是以后的方向了:
            按下和松开是两种操作,
            但是有四种组合,
            上轮为按下+本轮为按下  :连续两轮按下,即为连着,同时按下两个钢琴按键
            上轮为按下+本轮为松开  :代表从开了某个钢琴按键
            上轮为松开+本轮为松开  :代表连续松开了两个钢琴按键
            上轮为松开+本轮为按下  :松开了某个钢琴按键,但是有按下了其他的钢琴按键,即切换按键,开始新的一个音符.
            然后根据上面的四种操作,分别对上面四种情况进行编程.
            
            目前bug
            假设按下,都按下,松开都松开,这里很规则,那么用下面这个,比较好用.
            但是有时候,会出现连续按下三个按键,下一轮松开的时候只松开了两个按键,另一个按键在多轮之后才松开,
            这个程序就会出问题...
            另一个情况是,有空键出现的时候.也就是note on 按下的时候有时间,通常情况下,这里是没有时间的,
            代表着按下和上次松开没有间隔,但是如果有间隔,就说明,之前有一个空的音符输入...
            
            '''
            # 按下了note_on类型,就把action赋值为1
            if msg.type=="note_on":   
                action=1
                # 连着两个都按下了,就是和弦,在本轮序列中添加一个音符.
                if action ==action_last:
                    note_list_in.append(msg.note)
                # 如果上轮没有按下,本轮按下了.
                # 就要开启新的一个序列.
                if action !=action_last:
                    # 如果是曲子的开头,就是第0行
                    if hang!=0:
                        # 开启新的一行前，先要保存上次的数据(序列)到二维序列note_list_ex.最终的曲子的所有音符是存在note_list_ex
                        # note_list_ex是二维序列.二维序列的每一行是note_list_in,这个是一维序列,代表某一时刻的按下的按键
                        # 保存上次的序列,加入到二维中(就是外层中)
                        note_list_ex.append(note_list_in)
                    # 要清空内部序列，以便存入新一行的数据
                    # 把本轮的音符note存入新的一行.
                    # 并且行号要加一
                    # 如果要是有时间间隔,就说明有空音符的存在...
                    note_list_in=[] 
                    note_list_in.append(msg.note)
                    hang=hang+1
   
                    
                    
            '''
            只有在松开 note_off 的时候才会有时间参数.
            每条note_on信息通常是不带时间参数的,也就是这个时候通常是time=0的,
            只有在松开即note_off的时候,才会知道我按下钢琴按键用了多长时间.
            '''
            # 第三种情况,上面是按下钢琴键的两种情况.
            # 下面就是松开钢琴键的两种情况.
            # 松开钢琴键action参数被赋值为0
            if msg.type=="note_off":
                action=0
                # 本轮松开，上一轮也是松开，
                # 就是同一行序列的处理操作了,这个时候应该进行时间的保存了
                # 也就是说,这里是一组钢琴键"松开"操作,如果是一组,只有第一个松开是有时间参数的,其他为了简化起见,就不再处理了.
                # (bug:这里默认所有钢琴键一起松开,实际是不合理的,因为有的时候一起按下的钢琴键,并不一定一起松开...)
                if action == action_last:
                    # 其实这里还是有改进的空间的,
                    # 需要把时间序列也改装成二维的序列.
                    pass

                # 就是本轮为松开,上一轮是按下.
                # 那么这本轮的松开,一定是带有时间参数的.把时间参数取出来.
                # 为了简单起见,就不在弄二维序列了,先把时间弄成一维序列
                if action !=action_last:
                    time_list.append(msg.time)
                
                    
            # 更新一下按键状态。
            action_last=action
            
    # 千万不要忘了把最后一行,放入二维序列里面!!!  
    # 因为我们是检测到note_on才会进行上一时刻的音符序列保存到二维序列当中.
    # 最后一个on之后,就是off了,就没有on再存入二位序列了,所以需要把最后时刻的音符序列存入到二维序列中
    note_list_ex.append(note_list_in)             
            
    '''    
    # 上面是数组的生成,下面要对数组进行规整
    # 整首midi文件的音符是存入在了二维序列note_list_ex里面,每一时刻的音符是存在了note_list_ex的每一行,即note_list_in里面
    # 每一时刻对应的时长是存在了一维序列time_list里面
    '''
    note_list_ex_sort=[]
    for note_list_in  in  note_list_ex:
        note_list_in_set = set(note_list_in)  # 把序列转换成集合,目的是为了去除里面重复的元素.去除每一时刻,重复按下的按键.
        note_list_in = list(note_list_in_set) # 去重后,把集合转换成序列.从小到大的排序.
        note_list_in = sorted(note_list_in)   # 排序
        note_list_ex_sort.append(note_list_in)# 排完序后的二维音符序列.

    # 函数有点长,有什么可以很好的弄缩进的东西吗...
    Dgl.midi_note_2_list=copy.deepcopy(note_list_ex_sort)
    Dgl.midi_time_1_list=copy.deepcopy(time_list)
    return note_list_ex_sort,time_list
        

    
    
def try_global():
    Dgl.list_try.append(1)
    
    
    
if __name__ == '__main__':
    send_msg()
    # 要注意这里传入的是字符串才行!!!
    note_list,time_list=midi_read("DY_newSong.mid")
    print(note_list)
    print(time_list)