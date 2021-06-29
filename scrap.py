import urllib.request as urlrequest
from bs4 import BeautifulSoup
#导入需要的包和模块，这里需要的是 urllib.request 和 Beautifulsoup
#通过urllib来获取我们需要爬取的网页

weather_url='https://mp.weixin.qq.com/s/nelIph2oQibIsnnxecJRPw'
web_page=urlrequest.urlopen(weather_url).read()

#用 BeautifulSoup 来解析和获取我们想要的内容块
soup=BeautifulSoup(web_page, 'html.parser')
soup= soup.find(label='Powered by 135editor.com')
allImg = soup.find_all('img')
allsrc = []
for img in allImg:
    allsrc.append(img.attrs['data-src'])
print(allsrc)
print(len(allsrc))

#找到我们想要的那一部分内容

def download_img(img_url, name):
    print ('downloading: ' + img_url)
    request = urlrequest.Request(img_url)
    try:
        response = urlrequest.urlopen(request)
        img_name = name + ".jpeg"
        filename = "/Users/admin/Documents/pythonProject/gaokao/imgs/"+ img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"

# 下载要的图片
for index, img_url in enumerate(allsrc):
    # if index + 1 in [20, 39, 49, 60, 73, 76]:
    download_img(img_url, str(index + 1))