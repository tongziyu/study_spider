from urllib.request import urlopen

if __name__ == '__main__':
    """
    第一个爬虫程序
    爬虫就是通过编写程序来获取到互联网上的资源
    本质上就是使用python去发送请求，模拟浏览器，发送url请求，获取数据
    
    需求：用程序模拟浏览器，输入一个网址，从该网站中获取到资源或者内容
    
    python搞定以上需求，只需要3件事
        1. 导入request包
        2. 准备好网址
        3. 发送请求
    """
    url = "http://www.baidu.com"

    # 使用一个变量接收响应结果
    resp = urlopen(url)

    """
    如果只想要页面的数据的话，则使用read() 方法
    decode() 方法 解码并指定解码的字符集，这里使用utf-8 是因为页面中就写了utf-8
    read()方法会移动指针
    """
    #print(resp.read().decode('utf-8'))

    # 将爬取的数据保存到一个文件中

    """
    with 用法：一般都是配合着打开文件使用，可以保证当程序出错后，文件流也会关闭，避免了资源泄露
    后面这个file就是 open() 返回的对象，直接操作这个file即可完成对文件的操作
    """
    with open("baidu.html", mode="w") as file:
        # 将读取到的网页源代码 写入到文件中
        file.write(resp.read().decode('utf-8'))

    print("over!")