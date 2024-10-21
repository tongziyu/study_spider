import requests
from lxml import etree

if __name__ == '__main__':
    """
    XPath 通过html中节点的关系 进行查找元素的
    安装 lxml
        pip install lxml
        
    通过lxml中的etree来进行解析
    """
    xml: str = """
    <book>
        <h4><strong><span style="font-family: 微软雅黑; font-size: 22px;"> 辽宁省</span></strong></h4>
        <p><span style="font-family: 微软雅黑; font-size: 18px;"><strong>宜家大连商场</strong></span></p>
        <p><span style="font-family: 微软雅黑;">商场地址：大连市西岗区海达南街51号（香炉礁轻轨站东侧，疏港路北侧）</span></p>
        <p><span style="font-family: 微软雅黑;">商场营业时间：10:00 - 21:00</span></p>
        <p><span style="font-family: 微软雅黑;">餐厅营业时间：09:00 - 20:30</span></p>
        <p><span style="font-family: 微软雅黑; font-size: 18px;"><strong>宜家沈阳商场</strong></span></p>
        <p><span style="font-family: 微软雅黑;">商场地址：沈阳市铁西区兴华北街20号（兴华街与北二路交叉口西北角）</span></p>
        <p><span style="font-family: 微软雅黑;">商场营业时间：10:00 - 21:00</span></p>
        <p><span style="font-family: 微软雅黑;">餐厅营业时间：09:00 - 20:30</span></p>
        <h4><strong><span style="font-family: 微软雅黑; font-size: 22px;"> 黑龙江省</span></strong></h4>
        <p><span style="font-family: 微软雅黑; font-size: 18px;"><strong>宜家哈尔滨商场</strong></span></p>
        <p><span style="font-family: 微软雅黑;">商场地址：黑龙江省哈尔滨市南岗区复旦街48号（哈西大街与复旦街交叉口）</span></p>
        <p><span style="font-family: 微软雅黑;">商场营业时间：</span></p>
        <p><span style="font-family: 微软雅黑;">夏季（5月至10月）：10:00 - 21:00</span></p>
        <p><span style="font-family: 微软雅黑;">冬季（11月至次年4月）：10:00 - 20:00</span></p>
        <p><span style="font-family: 微软雅黑;">餐厅营业时间：</span></p>
        <p><span style="font-family: 微软雅黑;">夏季（5月至10月）：09:00 - 20:30</span></p>
        <p><span style="font-family: 微软雅黑;">冬季（11月至次年4月）：09:00 - 19:00</span></p>
        <h4><strong><span style="font-family: 微软雅黑; font-size: 22px;"> 山东省</span></strong></h4>
        <p><span style="font-family: 微软雅黑; font-size: 18px;"><strong>宜家济南商场</strong></span></p>
        <p><span style="font-family: 微软雅黑;">商场地址：山东省济南市槐荫区烟台路121号（二环西路与烟台路、张庄路交叉口）</span></p>
        <p><span style="font-family: 微软雅黑;">商场营业时间：10:00 - 22:00</span></p>
    </book>
    """

    etree_xml = etree.XML(xml)

    # 拿到对应的标签内的值 使用 text() 就可以拿到
    # 拿到/span下的值，使用 /.../span/text()  就可以拿到
    result = etree_xml.xpath("/book/h4/strong/span/text()")
    result2 = etree_xml.xpath("/book/p/span/text()")

    print(result, end="\n")
    print(result2, end="\n")

    # -----------------------------------------------------------------------------------------------------

    url: str = "https://www.maicuole.com/more/backyard/ikea-market-address.html"

    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    tree = etree.HTML(response.text)

    result3 = tree.xpath("//div[@class='post-content']//text()")

    with open("b.txt", mode="w") as file:
        for item in result3:

            file.write(item)

    print(result3)

    pass

