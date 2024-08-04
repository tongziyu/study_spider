
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

    # 使用while循环遍历列表
    index = 0
    while index < len(student_name):
        print(student_name[index])
        index += 1


def study_tuple():
    """
    学习元组:元组一旦完成定义，则不能被修改
    元组定义：使用小括号，中间使用 , 分割，数据类型可以是任意的，建议统一，元组也支持嵌套
    元组因为不能被修改，所以元组的方法特别少
    :return:
    """

    tuple1 = ("zhangsan", "lisi", "wangwu", "zhaoliu")

    print(tuple1)

    # 1.查找某个元素，如果找到了则返回下标，如果找不到抛出异常
    # print(tuple1.index("zhangsan1"))

    # 2.得到元组中某个元素出现的次数
    print(tuple1.count("zhangsan"))

    # 3.得到元组中元素的个数
    print(len(tuple1))

    # 4.根据下标得到某个元素的值
    print(tuple1[0])

    # 遍历元组
    for t in tuple1:
        print(t)


def study_str():
    """
    学习字符串，掌握字符串的常用方法
    :return:
    """
    message = "Hello World!"

    # 1.字符串也可以通过下标来获取值
    # 获取第一个值， 获取最后一个值
    print(message[0] + message[-1])

    # 2.字符串和元组一样，不支持修改，执行下面代码会报错
    # message[0] = 'h'

    # 3.查找特定字符串的索引下标值
    print(message.index("o"))  # 4

    # 4.字符串的替换，把Hello替换成 Hi
    # 注意：这种操作会得到一个新的字符串
    new_message = message.replace("Hello","Hi")
    print(new_message)

    # 5.字符串去除左右空格,会返回一个新的字符串
    username = " zhangsan "
    new_username = username.strip()

    print(new_username)

    # 6.字符串去除左右指定字符串，前后的12 都会被去掉
    test = "12 HelloWorld 12"
    new_test = test.strip("12 ")
    print(new_test)

    # 7.统计子字符串出现的次数
    test2 = "HelloWorld"
    print(test.count("o"))

def study_xulie():
    """
    序列是指：内容连续、有序、可使用下标索引的数据容器，其中 列表、元组、字符串都可以认为是序列
    序列支持切片，从一个序列中，取出一个子序列
    语法：序列[起始下标:结束下标:步长]
    :return:
    """
    message = "HelloWorld"

    # 这样写可以快速给字符串取反
    new_message = message[::-1]
    print(new_message)

    test = "万过薪月，员序程马黑来，nohtyP学"
    new_test = test[::-1]
    print(new_test)

    result_test = new_test[9:14:1]
    print(result_test)


def study_set():
    """
    set集合，数据不能重复，可以用来去重，内容无序
    set是无序的，所以不支持使用下标进行访问
    set语法：
    var = {}
    var = set()
    :return:
    """

    set_country = {"河北", "河南", "山东", "山西", "河北"}
    # 1.向集合中添加一个元素
    set_country.add("北京")

    # 2.删除指定元素
    set_country.remove("河北")
    print(len(set_country))

    # 3.随机弹出一个元素
    item = set_country.pop()
    print(item)

    # 4.清空集合
    set_country.clear()

    print(set_country)


def study_dick():
    """
    字段
    定义格式：
    dict = {key: value, key2: value2, key3: value3}
    :return:
    """
    student = {
        "name": "zhangsan",
        "age": 30,
        "address": "北京市"
    }

    print(student["name"])

    for key in student.keys():
        print(f"key : {key}, value : {student[key]}")

    student_score = {
        "zhangsan": {
            "yuwen": 80,
            "shuxue": 100,
            "yingyu": 99
        },
        "lisi": {
            "yuwen": 100,
            "shuxue": 78,
            "yingyu": 67
        }
    }
    print(student_score["lisi"]["yuwen"])


if __name__ == '__main__':
    """
    学习python数据容器
    python支持的数据容器：列表，元组，字符串，集合，字典

    """
    # study_list()

    # study_tuple()

    # study_str()

    # study_xulie()

    # study_set()

    study_dick()
    pass