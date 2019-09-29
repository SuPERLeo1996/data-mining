import multiprocessing
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def request(url):
    print(url)
    try:
        response = requests.get(url, headers={"User-Agent": UserAgent().random})
        if response.status_code == 200:
            source = response.text
            soup = BeautifulSoup(source, "html.parser")

            detail = {}

            detail["价格"] = soup.find("span", class_="total").text
            detail["单价"] = soup.find("span", class_="unitPriceValue").text
            detail["小区"] = soup.find("div", class_="communityName").find("a", class_="info").text
            detail["所在区域"] = soup.find("div", class_="areaName").find("span", class_="info").text
            detail["地铁"] = soup.find("div", class_="areaName").find("a", class_="supplement").text
            base = soup.find("div", class_="base").find_all("li")

            if len(base) > 0:
                detail["户型"] = base[0].text
            else:
                detail["户型"] = ""

            if len(base) > 2:
                detail["面积"] = base[2].text
            else:
                detail["面积"] = ""

            if len(base) > 6:
                detail["朝向"] = base[6].text
            else:
                detail["朝向"] = ""

            if len(base) > 8:
                detail["装修情况"] = base[8].text
            else:
                detail["装修情况"] = ""

            if len(base) > 10:
                detail["电梯"] = base[10].text
            else:
                detail["电梯"] = ""

            return detail
        else:
            return None
    except Exception as e:
        print("-------开始-------")
        print(e)
        print(url)
        print("-------结束-------")


def get(urls, num):
    result = []
    i = 1
    for url in urls:
        print("线程" + str(num) + "第" + str(i) + "个")
        result.append(request(url))
        i += 1
    file = 'detail' + str(num) + '.csv'
    print(file)
    with open(file, 'w', encoding='utf-8') as detail_file:
        for detail in result:
            print(detail)
            detail_file.write(
                '{}#{}#{}#{}#{}#{}#{}#{}#{}#{}\n'.format(detail["价格"], detail["单价"], detail["小区"], detail["所在区域"],
                                                         detail["地铁"], detail["户型"], detail["面积"], detail["朝向"],
                                                         detail["装修情况"], detail["电梯"]))


if __name__ == '__main__':
    infos = []
    with open('list.csv', 'r') as list_file:
        for line in list_file.readlines():
            infos.append(line.strip())
    p1 = multiprocessing.Process(target=get, args=(infos[:500], 1))
    p2 = multiprocessing.Process(target=get, args=(infos[500:1000], 2))
    p3 = multiprocessing.Process(target=get, args=(infos[1000:1500], 3))
    p4 = multiprocessing.Process(target=get, args=(infos[1500:2000], 4))
    p5 = multiprocessing.Process(target=get, args=(infos[2000:2500], 5))
    p6 = multiprocessing.Process(target=get, args=(infos[2500:], 6))
    p1.deamon = True
    p2.deamon = True
    p3.deamon = True
    p4.deamon = True
    p5.deamon = True
    p6.deamon = True
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
