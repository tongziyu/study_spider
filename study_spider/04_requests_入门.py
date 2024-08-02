import requests

if __name__ == '__main__':
    """
    之前的代码使用的是urllib中的urlopen()，虽然很简单了，但是requests这个模块会更加简单
    requests对处理请求头这种方式，会更加的简单快捷
    
    request模块不是官方自带的模块，是第三方的，需要使用pip (在终端)安装一下
        pip install requests
    """
    resp = requests.get('https://www.baidu.com/s?wd=pip怎么切换清华源')


    pass
