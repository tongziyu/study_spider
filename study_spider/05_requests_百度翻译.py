import requests


if __name__ == '__main__':

    url: str = "https://fanyi.baidu.com/sug"

    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    data: dict = {
        "kw": "你好"
    }

    # 发送的参数放到字典中，然后通过post方法的data形参进行传递
    response = requests.post(url=url, headers=headers,data=data)

    # response.json() 将服务器返回的内容直接处理成json => dict
    result: dict = response.json()

    print(result["data"][0]["v"])
    #print(response.json())

