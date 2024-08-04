
# 导入自定义包
from study import my_module1


import study

if __name__ == '__main__':
    """
    学习包
    从物理上看，包就是一个文件夹，这个文件夹里面有很多.py文件，其中有一个 __init__.py文件
    """

    # my_module1.module1()

    study.my_module1.module1()

    """
    安装第三方包
    """