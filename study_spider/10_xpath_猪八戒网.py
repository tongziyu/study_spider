import requests

if __name__ == '__main__':

    url: str = "https://supei.zbj.com/api/ftServiceDomainService/search"

    param: dict = {
        "sortType": "7",
        "sign": "P20220704001",
        "extension[]": "2",
        "extensions[]": "22",
        "localCityId": "3374",
        "query": "%7B%22query%22:%22asas%22,%22size%22:30,%22start%22:0%7D"

    }
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    response = requests.post(url, params=param, headers=headers)

    print(response.text)




