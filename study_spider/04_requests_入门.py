import requests

if __name__ == '__main__':
    """
    之前的代码使用的是urllib中的urlopen()，虽然很简单了，但是requests这个模块会更加简单
    requests对处理请求头这种方式，会更加的简单快捷
    
    request模块不是官方自带的模块，是第三方的，需要使用pip (在终端)安装一下
        pip install requests
    """

    """
    为什么要进行ua伪装
        - 在
    """
    # 进行UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    query: str = "仝子瑜"
    
    resp = requests.get(f'https://www.baidu.com/s?wd={query}', headers=headers)


    headers: dict = resp.headers



    # 拿到页面源代码
    content: str = resp.text

    print(content)

    pass
