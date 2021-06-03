# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:23:07 2021

@author: GXTon (哔哩哔哩 和 博客园)


"""

# 参考文档
# 关于和弦的文档:https://blog.csdn.net/TruedickDing/article/details/101997574
# 能够弹出声音的.
# 是否能够通过链表,而不是序列......

'''
作用:
目前这个程序的作用,就是接收两个序列
序列一:音符二维列表
序列二:时间一维列表
然后根据两个序列,创造midi文件.

注:这里面的函数并没有都用上
'''
# 官方库
from mido import Message, MidiFile, MidiTrack,MetaMessage
import random

# 自己的库
import play_midi as pm
import DY_read_midi_0 as rd
import DY_geneEncoding_2 as Dge
import DY_global as Dg
import DY_cor_0 as Dco
import DY_plot_0 as Dpl


def get_chord_arrangement(name):
    chord_dict = {
        'maj3': [0, 4, 7, 12],  # 大三和弦 根音-大三度-纯五度
        'min3': [0, 3, 7, 12],  # 小三和弦 根音-小三度-纯五度
        'aug3': [0, 4, 8, 12],  # 增三和弦 根音-大三度-增五度
        'dim3': [0, 3, 6, 12],  # 减三和弦 根音-小三度-减五度

        'M7': [0, 4, 7, 11],  # 大七和弦 根音-大三度-纯五度-大七度
        'Mm7': [0, 4, 7, 10],  # 属七和弦 根音-大三度-纯五度-小七度
        'm7': [0, 3, 7, 10],  # 小七和弦 根音-小三度-纯五度-小七度
        'mM7': [0, 3, 7, 11],  # 小大七和弦 根音-小三度-纯五度-大七度
        'aug7': [0, 4, 8, 10],  # 增七和弦 根音-大三度-增五度-小七度
        'm7b5': [0, 3, 6, 10],  # 半减七和弦 根音-小三度-减五度-小七度
        'augM7': [0, 4, 8, 11],  # 增大七和弦 根音-小三度-减五度-减七度
        'dim7': [0, 3, 6, 9]  # 减减七和弦 根音-小三度-减五度-减七度
    }

    chord = chord_dict[name]

    return chord # 返回值是一个长度为4的一维数组，每一个值表示这个音符与根音相差的半音数


# 分解和弦
def add_broken_chord(root, name, format, length, track, root_base=0, channel=0):
    root_to_number={
        'C':60,
        'D':62,
        'E':64,
        'F':65,
        'G':67,
        'A':69,
        'B':71
        }
    root_note = root_to_number[root] + root_base*12
    chord = get_chord_arrangement(name)
    time = (length * 480) / len(format)
    for dis in format:
        note = root_note + chord[dis]
        track.append(Message('note_on', note=note, velocity=56, time=0, channel=channel))
        track.append(Message('note_off', note=note, velocity=56, time=round(time), channel=channel))



# 柱式和弦
# 下面这里是添加和弦.
# 调用下面依次,就会生成一个和弦.
# 比如实参:'C','maj3',format,2,track
# 第一个实参: root,代表根音.
# 第二个实参: name,代表 和弦类型 
# 第三个实参: format,就是一个序列,[1,2,3]
# ......
def add_column_chord(root, name, format, length, track, root_base=0, channel=0):
    root_to_number={
        'C':60,
        'D':62,
        'E':64,
        'F':65,
        'G':67,
        'A':69,
        'B':71
        }
    #notes_position = [0, 2, 2, 1, 2, 2, 2, 1]  #这个是音阶,CDEFGAB.7个音. 这里也正好是12个.(钢琴从D-B一共有12个键,其中包括黑键和白建)
    #后面的root_base代表了音阶.一个阶是12
    #root_to_number的作用是,利用字典,把根音转换成数字
    #一个8度,12个半音
    root_note = root_to_number[root] + root_base*12
    #下面也是调用了另一个自己的函数,这个函数的作用是返回和弦种类的序列
    #比如大三和弦,名字叫做,'maj3' 返回的序列是:[0, 4, 7, 12]
    #这里的chord就是序列了.是一个音阶的序列
    chord = get_chord_arrangement(name)
    #480是一拍(这里是程序里默认的),约等于4,所以,这是四分之一拍
    time = length * 480
    
    #下面就是添加音符的开始和结束.
    
    #下面是添加音符的开始
    #format就是[1,2,3]
    for dis in format:
        note = root_note + chord[dis]
        track.append(Message('note_on', note=note, velocity=56, time=0, channel=channel))
    #下面是添加音符的结束
    #注意!!!!
    #如果是第一个,就是需要,time时间长度.其他的就都是0了.  
    for dis in format:
        note = root_note + chord[dis]
        if dis == format[0]: 
            track.append(Message('note_off', note=note, velocity=56, time=round(time), channel=channel))
        else:
            track.append(Message('note_off', note=note, velocity=56, time=0, channel=channel))
        








# 这里是添加和声的一种方法.
# 添加一系列柱式和弦.
def chord1(track):
    format = [1,2,3]
    #下面这里调用了6次,然后生成的音乐就响6个音.
    
    #重要!!!!
    #要注意构造函数,看一下,需要传入哪些参数,这些参数是否合理.
    #函数的原型是:def add_column_chord(root, name, format, length, track, root_base=0, channel=0):
    #参数1: 根音
    #参数2: 和弦类型
    #参数3: 播放方式
    #参数4: 长度 2 拍
    #参数5: 音轨 track
    #参数6: 音阶(音所在的组)
    #参数7: channel
    add_column_chord('C','maj3',format,0.5,track)
    add_column_chord('C','maj3',format,0.5,track)
    add_column_chord('A','min3',format,0.5,track,-1)
    add_column_chord('A','min3',format,0.5,track,-1)
    add_column_chord('F','maj3',format,0.5,track,-1)
    add_column_chord('F','maj3',format,0.5,track,-1)
    add_column_chord('G','maj3',format,0.5,track,-1)
    add_column_chord('G','maj3',format,0.5,track,-1)





# 为曲子midi添加一个钢琴按键动作.
# 为什么需要形参呢???要把形参干掉...
def add_column_chord_2(note_list,time_cnt,track,channel=0):
    '''
    传入:
        音符序列,(一维的) ,同时按下的一组钢琴按键都有哪些音符.
        时间长度,(一个数值),同时按下的一组钢琴按键持续了多长时间.
    作用:
        生成一组钢琴按键的动作
    '''    
    # 下面是添加音符的开始
    # 因为note_list是一维的序列,然后dis就是一维的序列中的每个元素.
    # 那么下面这个循环就是,把各个元素:dis,添加到一个曲子的某个时刻.
    # 如果note_list中是[1,3,5]这三个元素,那么就是同一时刻,有三个按键1,3,5被按下
    # 所以需要一个for,用于添加多个note_on
    for dis in note_list:
        track.append(Message('note_on', note=dis, velocity=56, time=0, channel=channel))
    # 下面是添加音符的结束,同理上面是多个note_on
    # 那么下面就要对应多个not_off
    # 注意!!!!如果是第一个,就是需要,time时间长度.其他的就都是0了.  
    for dis in note_list:
        if dis == note_list[0]: 
            track.append(Message('note_off', note=dis, velocity=56, time=time_cnt, channel=channel))
        else:
            track.append(Message('note_off', note=dis, velocity=56, time=0, channel=channel))



def create_song(note_array_2dim,time_array_1dim,newsong="DY_newSong.mid"):
    '''
    作用:
        note_array_2dim: 二维的音符数组 (里面的每一行都是一个一维的序列,代表着某一时刻按键的一组钢琴键)
        time_array_1dim: 一维的时间数组 (这里的数组是用序列构成的)
        newsong: 生成新的midi文件的名字
    '''
    #下面这里的是库,用于创建一个文件.
    mid = MidiFile()  
    #创建一个track,音轨的创建.     
    track = MidiTrack()
    #把音轨添加入文件中.
    mid.tracks.append(track)
    #这里Message是一个官方库的函数,
    #https://blog.csdn.net/weixin_38008864/article/details/104980875
    #'program_change'代表着起始,channel=0,time=0:只能是0 program= X代表乐器.
    track.append(Message('program_change', program=0, time=0))  
    '''
    上面是常规的操作,每个都会这么写
    下面是设置曲速
    '''
    # 设置曲速500000 代表 0.5s为一拍......
    # 目前曲速这里还是不知道怎么设置表较好......
    track.append(MetaMessage('set_tempo', tempo=2000000, time=0))   
    
    # 判断音符序列 和 时间序列 哪个短,哪个短用哪个
    if len(note_array_2dim)>len(time_array_1dim):
        long=len(time_array_1dim)
    else:
        long=len(note_array_2dim)
    
    #重点!!!!!!!!
    #下面是修改track中的内容,用于产生音符.
    # 二维数组有多长,就需要循环多少次.
    # 二维数组的行数,就代表有多少个钢琴按键组合. 
    for cnt in range(long):   
        # 为midi添加一个钢琴动作,
        # 一首曲子有几个动作,就循环几次.
        add_column_chord_2(note_array_2dim[cnt],time_array_1dim[cnt],track,channel=0)
    #把包含track的midi文件保存下来.
    mid.save(newsong)

        


if __name__ == '__main__':
    '''
    生成一首midi文件需要两个东西:
        一个是二维的音符序列;
        另一个是一维的时间序列;
    生成这两个东西,可以用三种方法:
    '''
    
    # 程序运行参数配置
    method=0
    midi_name="DY_doudizhu.mid"
    # 获取音乐参数,所有的参数存入全局变量中(存放在了DY_global.py文件中)
    # 目前下面函数里就有midi_read函数,midi_read返回的音符序列和时间序列并没有存入到全局变量中????
    Dge.global_calc_midi_parameter(midi_name)    
    
    
    
    
    
    
    # 程序开始运行
    if method==0:
        ''' 第0种方法,曲子导入 '''
        note,timer=rd.midi_read(midi_name)
        # Dg的意思是全局变量
        print(Dg.midi_dic_keys_list)
        
    if method==1:
        ''' 第1种方法,仿照生成 '''
        note,timer=rd.midi_read(midi_name)
        # 下面是根据传入的note二维序列,生成相仿的新的二维序列.
        note=Dge.primary_generation_2(1,note)
    
    
    if method==2:
        ''' 第2种方法,手动填写 '''
        note=[[45],[65,54],[60],[46],[65,75]]
        timer=[100,200,300,400,500]
    
    if method==3:
        ''' 第3种方法,根据相似度,一段一段组装的 '''
        note,timer=rd.midi_read(midi_name)
        note_list=Dco.cor_correct(Dg.midi_root_list,0)
        #print("note:::",note_list)
        # 对生成的序列,进行格式的处理
        note=[]
        for data in note_list:
            note_in=[]
            note_in.append(data)
            note.append(note_in)
        print(note)
    
#    # 生成的新song数据处理
#    cor1,cor_window=Dco.window_cor(note,0)
    
    # 开始作曲
    create_song(note,timer)
    print("最终曲子",note)
    
    
    
    
#    # 绘制图像
#    Dpl.plot_broken("cor",Dg.midi_window_cor_list)
#    Dpl.plot_broken("cor",cor_window)
    
    # 播放作曲
    pm.play_midi("DY_newSong.mid")









