

def study_exception():
    """
    如果test2.txt文件不存在，则肯定会报错【使用r读】
    :return:
    """

    # with open("test2.txt", mode="r") as file:
    #     print(file.readlines())


    # 使用异常捕捉
    try:
        with open("test2.txt", mode="r") as file:
            print(file.read())
    except Exception as e:
        print(f"出现了异常,异常信息：{e}")


if __name__ == '__main__':
    """
    学习异常
    捕捉异常的基本写法：
    try:
        可能发生异常的代码
    except [Exception]:
        捕捉到异常后执行的操作，如果指定了Exception则会捕捉指定的异常名
    else:
        else表示，执行完之后如果没有异常，则会执行else
    finally:
        不管出不出现异常，都会执行到finally代码块，可以在这里做资源释放
    """

    study_exception()