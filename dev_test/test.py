import requests
from bs4 import BeautifulSoup

payload = {'Host': 'q.10jqka.com.cn',
'Proxy-Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': 1,
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
'Referer': 'http://www.10jqka.com.cn/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6',
'Cookie': 'log=; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1558879049; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1558879049; v=AulZGmfEkfIsTK1GYP87JOAS_p5Att3oR6oBfIveZVAPUgdI0wbtuNf6EUAY'
}

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
'Accept': '*/*'
}

r = requests.get('http://q.10jqka.com.cn/gn/', headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
a = soup.select('.cate_items a')
for item in a:
    print(item.get_text())
    print(item['href'])