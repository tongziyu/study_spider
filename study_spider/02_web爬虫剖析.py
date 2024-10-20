from urllib.request import urlopen
from urllib.parse import quote

if __name__ == '__main__':
    """
    当我们使用urlopen() 去打开一个url的时候，python会像浏览器一样发送一个http请求，
    当服务器收到请求后，会返回一个响应包 html页面
    
    如果向百度发送一个带有请求参数的url的话，比如带上 "周杰伦"，那么百度那边会先内部自己检索，检索完毕后返回带有周杰伦信息的html数据 响应包
    
    需求:向百度发送一个请求，携带请求参数 "周杰伦"
    """

    """
    发送请求的时候用不能直接在url中拼接中文，需要转成ASCII之后才行
    使用quote()方法转成ASCII后，然后使用 f 格式化字符串，在字符串前面写一个f，然后在字符串里 使用 {}{} 来替代
    
    """
    search_query = "周杰伦"
    encode_query = quote(search_query, safe='')

    url = f"https://www.baidu.com/s?wd={encode_query}"

    resp = urlopen(url)

    with open("../result/周杰伦.html", mode="w") as f:
        f.write(resp.read().decode("utf-8"))

    print("over!")

    """
    上述代码执行结果，会响应一个页面，而不是一个json串，这就说明了这种方式是服务器渲染，也就是servlet中的JSP
    
    服务器渲染：在服务器那边直接把数据和html整合在一起，统一返回给浏览器。在页面源代码中能看到数据
    
    客户端渲染：（这种就是前后端分离的方式）后端只返回json数据，客户端拿到json数据后，进行渲染。这种方式的特点就是在页面源代码中看不到数据
            看不到数据，直接找请求，模拟发送请求，就能得到响应包。
            
    客户端渲染方式比较友好，直接可以通过一个接口获取到json数据，然后保存到字典里。假如是服务器渲染方式的话，数据全部在页面里，还需要使用解析工具进行提炼。
            
        如果要爬取的内容是客户端渲染的话，则需要熟练的找到想要的请求，就需要熟练使用客户端抓包工具（F12）network
    """