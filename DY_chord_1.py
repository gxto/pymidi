#关于和弦的文档:https://blog.csdn.net/TruedickDing/article/details/101997574
#能够弹出声音的.

#需要做: 这里要改造一下,改造成用数字的表示方法,最终是要用数组代表音乐的,或者用链表.
#       #用链表代表音乐,这里就需要进行数字化,方便进行计算,不要用音符才好.    
#       #如果不这样做,就需要你,在中间加一个转换的代码,把数字计算好,然后转换一下,然后再调用这个和弦.    

#需要做: 要怎样写, 就是怎样把数组,写进midi中. 
         #目前想,弄一个数轴出来,然后,把每个音符的坐标写出来,就把曲子点出来...
         #每个音符,就相当于一个画面中的一点,然后,整个曲子是一个点,一个点点出来的.
         #所以这样,就需要构造一个函数,  函数传入参数是,音符的起始时间,时间长度,音符种类,,,,等
         #可能需要建立一个二维的数组,来代表音乐.



from mido import Message, MidiFile, MidiTrack
import random

#自己的库
import play_midi as pm





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


#分解和弦
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



#柱式和弦
#下面这里是添加和弦.
#调用下面依次,就会生成一个和弦.
#比如实参:'C','maj3',format,2,track
#第一个实参: root,代表根音.
#第二个实参: name,代表 和弦类型 
#第三个实参: format,就是一个序列,[1,2,3]
#......
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
        








#这里是添加和声的一种方法.
#添加一系列柱式和弦.
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






if __name__ == '__main__':
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
    
    
    #重点!!!!!!!!
    #下面是修改track中的内容.
    chord1(track)
    #把包含track的midi文件保存下来.
    mid.save('newSong.mid')
    pm.play_midi("newSong.mid")





