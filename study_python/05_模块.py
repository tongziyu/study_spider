# 导入时间模块
import time as tt

# 导入时间模块中的sleep()方法
from time import sleep as sl

# 导入时间模块的所有方法
from time import *

# 导入自定义模块
import custom


if __name__ == '__main__':
    """
    学习Python模块
    
    Python模块就是一个.py结尾的文件，模块可以定义变量，类和函数
    
    模块在使用前需要先导入，导入的语法：
    [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
    
    常用形式如下：
        import 模块名
        from 模块名 import 类、变量、方法等
        from 模块名 import *
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名
    """

    # time.sleep(1)

    # print("睡眠了1秒")

    sleep(2)
    print("睡眠了两秒")

    custom.custom()
