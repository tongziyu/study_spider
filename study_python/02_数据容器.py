


def study_list():
    """
    学习list数据结构
    :return: None
    """
    # 定义一个列表，里面存学生的姓名
    # 列表中元素没有限制，但是还是统一比较好
    student_name = ["zhangsan", "lisi", "wangwu", "zhaoliu"]

    # 定义空列表的两种方式
    student_address = []
    student_phone = list()

    # 类型为list
    print(type(student_name))

    # 取出元素,下标从0开始
    print(student_name[1])

    # 反向索引, -1 就是最后一个元素， -2 就是倒数第二个元素
    print(student_name[-1])

    # 修改元素
    student_name[0] = "仝子瑜"

    print(student_name[0])

    # 查看列表长度
    print(len(student_name))

    # 遍历列表
    for name in student_name:
        print(name)

    # 列表的常用操作
    # 1.查找某元素的下标
    print(student_name.index("仝子瑜"))

    # 2.插入元素,使用列表的insert(下标,元素)方法
    student_name.insert(1,"张起灵")


    # 3.追加元素，在列表的后面追加元素
    student_name.append("张启山")

    print("-----------------")
    # 4.追加元素的第二种方式,使用extend()方法
    extend_name = ["雪梨", "王胖子", "胡八一"]
    student_name.extend(extend_name)

    for name in student_name:
        print(name)

    print("---------------")
    # 删除元素的两种方式
    # 第一种方式： del 列表[下标]
    # 第二种方式： 使用 列表.pop()方法

    del student_name[0]

    for name in student_name:
        print(name)

    print("-----------------")

    student_name.pop(0)

    print(student_name)

    # 删除某一个元素在列表中出现的第一个匹配项，如果列表中有两个，只会删除第一次出现的那个
    student_name.append("lisi")
    student_name.append("lisi")
    student_name.remove("lisi")
    print(student_name)

    # 清空列表
    #student_name.clear()
    #print(student_name)

    # 统计列表中lisi的出现次数
    print(student_name.count("lisi"))

    # 查看列表中有多少元素，元素的数量
    print(len(student_name))

if __name__ == '__main__':
    """
    学习python数据容器
    python支持的数据容器：列表，元组，字符串，集合，字典

    """
    study_list()


    pass