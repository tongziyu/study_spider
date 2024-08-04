
class Student:
    """
    类的语法：
        class 类名:
            属性名
            def 方法():
    创建对象的语法:
        对象 = 类名()

    self 每个方法第一个参数必须要有self，相当于this，在访问对象的属性名和方法的时候需要使用 self
        self 在传递参数的时候，可以忽略他，只有在方法内部使用才会用到self

    类的内置方法：
        __init__ 构造方法
        __str__ 字符串方法   相当于是toString()方法
        __lt__ 小于等于比较
        __le__ 小于等于、大于等于符号比较
        __eq__ ==符号比较   相当于是equals()方法

    封装：
        私有成员变量语法：只需要在成员变量前加两个下划线 __name
            私有变量无法复制，也无法获取值

        私有方法语法：只需要在方法前添加两个下划线  __name
            私有方法无法直接被类对象使用

    继承：
        python中继承分为单继承和多继承
            单继承语法：
                class Cat(Animal):
                    pass

            多继承语法：
                class Cat(Animal, Runnable, Eatable):
                pass

        继承可以从父类那里继承成员变量+方法，但是私有的变量和方法无法继承

        多继承中，如果有相同的成员变量名，最先继承来的会保留，最后继承来的会丢失

        重写父类方法：
            - 如果对父类方法不满意，子类可以对其进行重写

        如果想在子类中调用父类的方法 需要使用 super

    类型注解：
        - 在弱类型语言中，有一个大大的缺点，当你想调用一个变量的某个方法的时候，你会发现没有提示!!!! 这就是因为pycharm他并不知道这是什么类型的变量
        - 在python3.5的时候引进了类型注解，也就是说，可以给变量指定一个数据类型，方便后期开发的时候调用方法有提示
        - 个人感觉，在python中，任何一个变量都像是 Java泛型，只有添加了类型注解 这样才指定了数据的类型。

        语法：
        基础数据类型 类型注解
            var_1: int = 10
            var_2: str = "Hello World"
            var_3: bool = True
            var_4: float = 3.14
        类对象数据类型 类型注解
        class Student:
            pass

            var_5: Student = Student()

        基础容器类型注解用法：
        my_list: list = [1, 2, 3]
        ...
        # 元组类型设置类型详细注解，需要将每一个元素都标记出来

        # 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value
        类型注解只是提示性的，不是决定性的，所以就算写错了，也行运行成功

        类型注解在方法形参和返回值上使用
        在方法形参上使用语法：
            def function1(x: int, y: int):
                pass
            这样在调用function1方法的时候，pycharm就能看到提示了

        指定方法的返回值类型语法：
            def function2(x: int, y: int) -> list[int]:
                pass
    多态：

    """
    # 如果使用了init 方法，那么这个变量的生命可以省略


    __test = None  # 定义私有变量
    def __init__(self, name, age, address):
        """
        构造方法，千万不要忘记self，在使用的时候也不要忘记self
        :param name:
        :param age:
        :param address:
        """
        self.name = name
        self.age = age
        self.address = address
        # print("init 方法执行，这个相当于是构造方法")

    def __str__(self):
        # 这个相当于是toString方法
        pass


    # 测试私有方法
    def __fun(self):
        print("私有方法执行")


    def say_hello(self):
        """
        对象的方法
        :return:
        """
        print(f"Hello！我是{self.name}")


class Animal:
    def __init__(self, category):
        self.category = category

    def print_name(self):
        print(f"我是：{self.category}")


class Cat(Animal):

    def __init__(self, category):
        self.category = category

    def print_name(self):
        print(f"重写父类方法:我是{self.category}")

def study_oop():
    # 创建两个对象
    s1 = Student("zhangsan", 18, "北京市")
    # 对name进行赋值
    s1.say_hello()


    s2 = Student("lisi", 18, "北京市")
    s2.say_hello()

    print(s1.name)
    print(s2.name)


def input_student_info():
    """
    循环录用学生信息
    :return:
    """
    student_info_list = list()
    while True:
        name = input("请输入学生名")
        age = input("请输入年龄")
        address = input("请输入地址")
        student = Student(name, age, address)
        student_info_list.append(student)
        print(f"学生：{student.name},年龄：{student.age},地址:{student.address}")


def lei_xing_zhu_jie(x: int, y: int):
    """
    学习类型注解


    """
    student: Student = Student("zhangsan", 18, "北京市")

    student.say_hello()


    # 对容器进行类型注解

    my_list: list = [1, 2, 3]

    my_tuple: tuple = (1, 2, 3)

    my_set: set = {"a", "b", "c"}

    my_dict: dict = {"a": 1, "b": 2, "c": 3}

    my_str: str = "Hello World"

    # 容器类型详细注解

    my_list2: list[int] = [1, 2, 3, 4]
    # 元组类型设置类型详细注解，需要将每一个元素都标记出来

    my_tuple2: tuple[int, int, int] = (1, 2, 3)

    my_set2: set[int] = {1, 2, 3}

    # 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value
    my_dict2: dict[str, int] = {"a": 1, "b": 2, "c": 3}

def lei_xing_zhu_jie2(x: int, y: int) -> list[int]:
    pass





if __name__ == '__main__':
    # input_student_info()

    cat = Cat("猫")
    cat.print_name()

    lei_xing_zhu_jie(1, 2)
    pass
