import requests

if __name__ == '__main__':

    url: str = "https://movie.douban.com/j/chart/top_list"

    # 封装get请求的参数，这个参数会在请求发送的时候 拼接到连接后面
    param: dict = {
        "type": "11",
        "interval_id": "100:90",
        "action": "",
        "start": "0",
        "limit": "20",
    }



    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(url,headers=headers,params=param)


    #  通过json() 将数据转成字典
    result: dict = response.json()

    # 输出一下请求的url
    print(response.request.url)

    print(type(result))

    print(response.json())


    print(len(result),"\n")

    # 爬取完成后 要记得关闭
    response.close()
