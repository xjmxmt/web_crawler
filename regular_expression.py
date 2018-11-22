import requests
import re

def a2(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    }

    r = requests.get(url, headers)
    txt = r.text.encode(r.encoding).decode('utf-8')
    # print(txt)
    pattern = re.compile(r'<a.*?"text-column-item box box-790">.*?"title".*?>(.*?)</a>', re.S)
    res = re.findall(pattern, txt)
    print(res)

a2('https://www.neihan8.com/article/')
