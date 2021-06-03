# -*- coding: utf-8 -*-
"""
作用: 主函数
"""

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
import DY_create_0 as Dcreate










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
    

    
    # 开始作曲
    Dcreate.create_song(note,timer)
    print("最终曲子",note)
    
    
    
    
#    # 绘制图像
#    Dpl.plot_broken("cor",Dg.midi_window_cor_list)
#    Dpl.plot_broken("cor",cor_window)
    
    # 播放作曲
    pm.play_midi("DY_newSong.mid")





