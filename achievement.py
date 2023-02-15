# -*- coding: utf-8 -*-

"""
自制成就弹窗提示，也可用于信息提示。

Copyright © 2022 轩哥啊哈OvO/卡猫kat. All rights reserved.
"""

import sys
import time
import threading
import tkinter as tk
from PIL import Image, ImageTk

class get_achievement():
    def __init__(self, description: str, name: str, colour: str="Black", icon: str=None, player: str="", xp: int=100, duration: int=3):
        r"""
        自制成就弹窗提示，也可用于信息提示。

        >>> import achievement
        >>> achievement.get_achievement(
            description=str,    #获得成就提示语
                    显示在第一行，可自定义显示
                    可选内置选项：
                        "PROGRESS"，显示“进度已达成！”，绿色
                        "AIM",
                        "ACHIEVEMENT",
                        "ADVENTURE",
                        "CHALLENGE"
            name=str,    #成就名称
                    显示在第二行，自定义
            *colour=str,    #成就提示语显示颜色（可选）
                    默认为黑色
                    当description使用内置选项时，默认为对应颜色
                    可自定义颜色：
                        格式为“Red”“Green”等英语单词，或“#XXXXXX”颜色代码
            *icon=str,    #显示图标或图片（可选）
                    默认不显示
                    建议大小：70px×70px
                    建议图片格式：.jpg/.png
                    ***文件名前必须加r，如：icon=r"C:\Users\XXX\Documents\icon.png"
            *player=str,    #获得成就玩家（可选）
                    默认为自己（不显示）
            *xp=int,    #获得经验（可选）
                    默认100点经验
            *duration=int    #成就显示时间（可选）
                    默认3秒
        )"""

        root=tk.Tk() #因Toplevel会无法避免地生成两个窗口，需要隐藏一个
        root.withdraw()

        root=tk.Toplevel() #因PIL有bug，必须使用Toplevel才可刷新图片
        root.geometry('340x100-340+1100')
        root.overrideredirect(True) #无边框窗口

        show_description = description
        show_colour = colour

        if description == "PROGRESS": show_description = "进度已达成！"; show_colour = "Green" #内置description选项
        if description == "AIM": show_description = "目标已达成！"; show_colour = "Red"
        if description == "ACHIEVEMENT": show_description = "成就已达成！"; show_colour = "Orange"
        if description == "ADVENTURE": show_description = "冒险已完成！"; show_colour = "Blue"
        if description == "CHALLENGE": show_description = "挑战已完成！"; show_colour = "Purple"

        def blank(row:int,column:int,txt:str): #空格占位
            blank = tk.Label(root,text=txt,font=("",6))
            blank.grid(row=row,column=column)

        blank(0,0,"  ")

        if icon != None: #图片显示
            icon = ImageTk.PhotoImage(Image.open(icon))
            icon_label = tk.Label(root,image=icon,height=70,width=70)
            icon_label.grid(row=1,column=1,rowspan=2)

            blank(0,2,"   ")
            
        else:
            pass
            
        description_label = tk.Label(root,text=show_description,font=("微软雅黑",17),fg=show_colour,anchor="w") #描述显示
        description_label.grid(row=1,column=3)

        name_label = tk.Label(root,text=name,font=("微软雅黑",17),anchor="w") #名称显示
        name_label.grid(row=2,column=3)

        def show(): #显示主线程
            print("[",time.strftime("%H:%M:%S",time.localtime()),"]",player,"获得成就","[",name,"]")
            for i in range(-340,16,4):#因为移动距离小，所以间隔要大
                root.geometry('340x100-'+str(i)+'+923')
                time.sleep(0.01)
            time.sleep(duration)
            for e in range(16,-340,-4):#因为移动距离小，所以间隔要大
                root.geometry('340x100-'+str(e)+'+923')
                time.sleep(0.01)

            root.quit()
            try:
                root.destroy()                
            except RuntimeError: #连续的成就显示导致关闭窗口事件时不可避免的RuntimeError报错
                pass

        show_thread=threading.Thread(target=show)#将开始函数放入多线程容器
        show_thread.start()#与mainloop同步执行

        root.mainloop()

    def __str__():
        return None

if __name__ == "__main__": 
    get_achievement(description="CHALLENGE", name="当鸡儿被套圈", colour="Red", icon=r"C:\Users\xiang\Documents\Visual Studio 2022\1.19.3-pre1.png", player="轩哥啊哈OvO", xp=1000, duration=3)
    get_achievement(description="PROGRESS", name="当鸡儿又被套圈", xp=1000, duration=3)
    get_achievement(description="测试啦啦啦~", name="当鸡儿再被套圈啦啦啦", colour="Blue", icon=r"C:\Users\xiang\Documents\Visual Studio 2022\1.19.3-pre1.png", player="卡猫kat", xp=1000, duration=3)
    print("测试完成，继续执行")
