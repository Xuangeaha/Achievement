# Python 成就系统模块 achievement

**Copyright © 2022 轩哥啊哈OvO/卡猫kat. All rights reserved.**

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

    )

    默认3秒
