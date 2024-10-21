import requests
import re

if __name__ == '__main__':
    url: str = "https://www.maicuole.com/more/backyard/ikea-market-address.html"

    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    content = response.text
    patten = r'<span[^>]*>(.*?)</span>'
    result: list = re.findall(patten,content)

    print(content)

    pass


    