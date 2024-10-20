
def study_read():
    file = open("../result/baidu.html", mode='r', encoding="utf-8")

    # 如果传入一个数值，则表示要读的数据长度，如果没有传入参数，则表示全部读取
    print(file.read(3))

    # readlines() 可以按照行的方式进行一次性读取，并且返回一个列表，其中每一行就是一个元素
    content = file.readline()
    print(len(content))

    # readline() 每调用一次读取一行，可以使用for来循环读取
    for line in open("../result/周杰伦.html", mode="r"):
        print(line)

    # 关闭文件
    file.close()

    # 使用with open as方式，在操作完之后会自动关闭文件流，如果执行中抛出了一场也会关闭
    with open(file="../result/baidu.html", mode="r") as file:
        print(file.readlines())


def study_write():
    """
    mode="w" 如果文件不存在，会创建文件，如果文件存在则会清空里面的内容。
    文件的写入，文件写入后需要调用一下 flush() 方法来刷新一下
    只有调用flush()方法的时候，才会写入到磁盘中，不然是不会写入到磁盘中的，这样做的好处是为了避免频繁的写入
    :return:
    """
    with open("test.txt", mode="w") as file:
        file.write("HelloWorld!!")
        file.flush()


def study_append():
    """
    学习文件操作-追加
    :return:
    """
    with open("test.txt", mode="a") as file:
        file.write("\n")
        file.write("\n")
        file.write("测试追加！！")
        file.flush()

if __name__ == '__main__':
    """
    python操作文件
    mode参数有三个：
        1. w 写入
        2. r 读取
        3. a 追加
    """
    study_append()