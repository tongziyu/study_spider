"""
函数的定义：

def 函数名:
    函数体
    return 返回值

"""


def print_message():
    print("HelloWorld")
    print("人工智能开发")


def sum(a, b):
    """
    两数相加 （python函数的注释要写在函数里，在调用时，鼠标悬停 就能看到）
    :param a: 参数1
    :param b: 参数2
    :return: 求和
    """

    # 可以在函数内部声明全局变量，要使用global关键字
    # 先声明 后使用
    global result
    result = a + b
    return a + b


if __name__ == '__main__':
    test = print_message()

    # 如果一个函数没有返回值的话，那么则会默认返回一个none
    # None表示空的、无实际意义的
    # 同时None也可以手动return回来

    # 如果一个函数返回None，则表示False
    # None 也可以给变量赋值
    print(type(test))

    print(sum(1, 2))
    pass