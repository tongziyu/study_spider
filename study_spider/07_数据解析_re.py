import re

if __name__ == '__main__':
    # 正则表达式 解析数据
    """
    正则表达式：
    常用元字符
        \w 匹配字母、数字、下划线
        \s 匹配任意的空白符
        \d 匹配0-9数字
        \n 匹配一个换行符
        \t 匹配一个制表符
        
        ^ 匹配字符串的开始
        $ 匹配字符串的结尾
        
        \W 匹配非字母数字下划线
        \D 匹配非数字
        \S 匹配非空白符
        A|B 匹配字符A或者字符B
        [0-9a-zA-Z] 对每一个字符进行匹配，可能出现的状况是否是 数字 大小写字母，如果是 则匹配成功
        [^...] 匹配除了...的所有字符 
        
    量词：控制前面的元字符出现的次数
        * 重复零次或更多次
        + 重复一次或更多次
        ? 重复0次或一次【出现或者不出现】
        {n} 重复n次
        {n,} 重复n次或更多次
        [n,m] 重复n-m次
        
    贪婪匹配和惰性匹配
        .*  贪婪匹配
        .*?  惰性匹配  【爬虫中用的最多】
    """

    """
    import re 导入re模块
    re模块：记住下面几个功能
        findall 查找所有，返回list
        
        search 进行匹配，如果匹配到了第一个结果就返回，如果匹配不到 就返回None
        
        match 只能从字符串的开头进行匹配
        
        finditer 和findall差不多，只不过这时返回的是迭代器（重点）
    
    """

    """
    findall：匹配字符串中所有符合正则的内容
        patten: 正则表达式
        string: 要匹配的字符串
        返回一个list
    """
    result: list = re.findall(r"\d+", "我的电话是17311513981,我女朋友的电话是15533233121")

    for item in result:
        print(item)

    print(len(result))

    """
    finditer参数说明：匹配字符串中所有的内容【返回的是迭代器】
    """
    result1 = re.finditer(r"\d+", "我的电话是17311513981,我女朋友的电话是15533233121")

    print(type(result1))

    # 从迭代器中取数据,需要使用 .group() 方法
    for item in result1:
        print(item.group())

    """
    search返回的结果是match对象，那数据需要.group()
    search只返回匹配到的第一个
    """

    result2 = re.search(r"\d+", "我的电话是17311513981,我女朋友的电话是15533233121")

    print(result2.group())

    """
    match 从头开始匹配，默认在正则前面加了一个 ^，用的不多
    """
    result3 = re.match(r"\d+", "我的电话是17311513981,我女朋友的电话是15533233121")

    print(result3.group())

    """
    预加载正则表达式，提高效率,执行下面代码后，内存中就会有一个正则了，效率高
    直接使用obj调用findall 即可
    """
    obj = re.compile(r"\d+")
    res = obj.findall("我的电话是17311513981,我女朋友的电话是15533233121")


    """
    重点：从匹配到的 中提取到 重点
    """
    pass
