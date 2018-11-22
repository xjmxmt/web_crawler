import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_string(s):
    return s.get_text().replace('\r','').replace('\n','').replace('\t','')

def loupan_web_spider(baseurl, start):
    tmp = baseurl.split('/')
    url = '/'.join(tmp[:-2]) + '/' + 'pg' + str(start) + '/' + tmp[-1]
    req = requests.get(url, headers=headers)

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all(class_ = 'resblock-desc-wrapper')

    info = []
    price = []
    for i in result:
        res = i.find_all('a')
        info.append(res)
        res2 = i.find_all(class_='main-price')
        price.append(res2)

    tmp_csv = []
    for i, j in zip(info, price):
        a = i[0]
        b = i[1]
        c = j[0]
        tmp_csv.append(get_string(a))
        tmp_csv.append(get_string(b))
        tmp_csv.append(get_string(c))
        with open("2.csv", "a", newline="", encoding='utf-8') as datacsv:
            csvwriter = csv.writer(datacsv)
            csvwriter.writerow(tmp_csv)
            tmp_csv.clear()

if __name__ == '__main__':
    baseurl = 'https://cd.fang.ke.com/loupan/jinjiang/pg1/#jinjiang'
    for i in range(10):
        loupan_web_spider(baseurl, i+1)

