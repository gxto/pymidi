# -*- coding: utf-8 -*-
"""
作用: 主函数

目前应用了遗传算法,
想象一下,一首midi音乐,就是一条完整的鱼.
不同类型的音乐就是不同种类的鱼,鲨鱼,小丑鱼,鲈鱼...
鱼也是由各个部分组成的,有鱼头,鱼身,鱼鳍,鱼尾...它们对应了音乐的开头,结尾,等......


fish是一个midi音乐.是一个二维的数组,二维数组里面的每个数组,都是一个时间点,按下的音符.
fish_root就是一个一维数组,其中的数字,就是一个时间点中,按下的一个音符.
"""

# 官方库
from mido import Message, MidiFile, MidiTrack,MetaMessage
import random
import numpy as np

# 自己的库
import play_midi as pm
import DY_read_midi_0 as rd
import DY_geneEncoding_2 as Dge
import DY_global as gl
import DY_cor_0 as Dco
import DY_plot_0 as Dpl
import DY_create_0 as Dcreate
import DY_selection as sel    # 筛选
import DY_crisscross as cri   # 交叉
import DY_mutation as mut     # 变异
import DY_decode as dec       # 赌轮




if __name__ == '__main__':
    '''
    生成一首midi文件需要两个东西:
        一个是二维的音符序列;
        另一个是一维的时间序列;
    生成这两个东西,可以用三种方法:
    '''
    
    # 程序运行参数配置
    method=3
    midi_name="DY_kanong.mid"
    gl.midi_cor_window_size=10
    # 获取音乐参数,所有的参数存入全局变量中(存放在了DY_global.py文件中)
    gl.global_parameter(midi_name)    
    
    
    # 遗传算法的参数配置
    midi_root=gl.midi_root_list
    
    window_size=gl.midi_cor_window_size
    
    
    
    # 程序开始运行
    if method==0:
        ''' 第0种方法,曲子导入  把导入的曲子进行原样播放'''
        note=gl.midi_note_list_2D
        timer=gl.midi_time_list_1D
        print("进入第0中方法,输出note",gl.midi_note_list_2D)  
        
    if method==1:
        ''' 第1种方法,仿照生成 '''
        note=gl.midi_note_list_2D
        timer=gl.midi_time_list_1D        
        # 下面是根据传入的note二维序列,生成相仿的新的二维序列.
        note=Dge.primary_generation_2(1,note)
    
    
    if method==2:
        ''' 第2种方法,手动填写 '''
        note=[[45],[65,54],[60],[46],[65,75]]
        timer=[100,200,300,400,500]
    
    
    # 下面是应用遗传算法进行仿照生成midi文件.
    if method==3:
        ''' 第3种方法,根据相似度,一段一段组装的 '''
        # 时间持续时长导入,这个是1维的序列,实际上应该改成多维的.
        timer=gl.midi_time_list_1D
        # 生成原始鱼
        gl.original_fish=Dge.produce_original_fish(gl.fish_parts_number,window_size,0,)
        print("gl.original_fish")
        print(gl.original_fish)        
        # 生成原始鱼池
        gl.fish_pond=Dge.produce_original_fishpond(gl.fishs_number,gl.original_fish)
        print("gl.fish_pond")
        print(np.array(gl.fish_pond))
        
        # 交叉,变异,排序,赌轮  遗传算法,每一项都是针对鱼池的.
        gl.fish_pond=cri.crossover_5(gl.fish_pond, gl.pc)
        gl.fish_pond=mut.mutation_5(gl.fish_pond,gl.pm)
        # 一条鱼有几段构成呢???[0:10]就是从中取出10个.这里是取出30个.
        num=gl.midi_root_window_cor_list[0:30]
        print("num",num)
        #pass
        # 这里是筛选,进化出新的鱼池,并选出最好的鱼.
        # 里面有优选和淘汰
        gl.fish_pond,gl.first_fish=dec.decode_5(gl.fish_pond,gl.first_window,num)
        note=gl.first_fish
        
    # 开始作曲,
    # 一个是音符序列,一个是时间序列,他们会自己适应短的那个.
    # 从而不用担心,这两个序列长度不同的问题.
    Dcreate.create_song(note,timer)
    print("最终曲子",note)
    
    
    
    
#    # 绘制图像
#    Dpl.plot_broken("cor",Dg.midi_window_cor_list)
#    Dpl.plot_broken("cor",cor_window)
    
    # 播放作曲
    pm.play_midi("DY_newSong.mid")





