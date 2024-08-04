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


def function_return():
    """
    在返回时，可以使用返回两个
    :return:
    """
    return 1, 2


def user_info(name, age, address):
    print(f"你的名字:{name},年龄:{age},来自:{address}")


def student_info(name, age, address, country="中国"):
    print(f"你的名字:{name},年龄:{age},来自:{address},国籍:{country}")


def unsteady_para(*args):
    """
    *args 表示不定长参数，可以传递很多，传递过来的参数会形成一个元组 tuple
    :param args:
    :return:
    """
    print(type(args))


def unsteady_para2(**args):
    """
    这种方式接收来的形参是key：value形式
    :param args:
    :return:
    """
    print(args)


def study_lambda(pri):
    pri("zhangsan")

if __name__ == '__main__':
    test = print_message()

    # 如果一个函数没有返回值的话，那么则会默认返回一个none
    # None表示空的、无实际意义的
    # 同时None也可以手动return回来

    # 如果一个函数返回None，则表示False
    # None 也可以给变量赋值
    print(type(test))

    print(sum(1, 2))

    # 使用两个变量，接受函数返回的两个返回值
    x, y = function_return()
    print(x)
    print(y)

    # 在传值的时候可以使用key=value的形式
    # 这样就可以打乱顺序往里面传参数
    user_info(name="zhangsan", age=18, address="北京市")

    # 对缺省形参可以不对其进行指定
    # 如果传值，则会修改值，如果不传，则会使用默认值
    student_info(name="zhangsan", age=18, address="北京市", country="美国")

    # 调用不定长参数的时候，传递时 可以传递很多参数
    unsteady_para(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    # 当函数的形参是这样写的时候 **args 有两个*,则表示可以 根据 key="value"的方式进行传参
    # 传过去的参数会转化成字典的形式
    unsteady_para2(name="zhangsan", age=18)

    # 学习匿名函数 lambda
    study_lambda(lambda name: print(name))


    pass