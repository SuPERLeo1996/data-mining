import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent


def max_page(url):
    response = requests.get(url, headers={"User-Agent": UserAgent().random})
    if response.status_code == 200:
        source = response.text
        soup = BeautifulSoup(source, "html.parser")
        page_data = soup.find("div", class_="page-box house-lst-page-box")["page-data"]
        # pageData = '{"totalPage":100,"curPage":1}'，通过eval()函数把字符串转换为字典
        max = eval(page_data)["totalPage"]
        return max
    else:
        print("Fail status: {}".format(response.status_code))
        return None


def house_list():
    max = max_page("https://sh.lianjia.com/ershoufang")
    print("max" + str(max))
    with open('list.csv', 'w', encoding='utf-8') as output_file:
        for page in range(1, max + 1):
            url = "https://sh.lianjia.com/ershoufang/pg{}/".format(page)
            response = requests.get(url, headers={"User-Agent": UserAgent().random})
            source = response.text
            print(page)
            print(url)
            soup = BeautifulSoup(source, "html.parser")
            links = soup.find_all("a", class_="noresultRecommend img LOGCLICKDATA")
            for i in links:
                link = i["href"]
                output_file.write('{}\n'.format(link))


if __name__ == '__main__':
    house_list()
