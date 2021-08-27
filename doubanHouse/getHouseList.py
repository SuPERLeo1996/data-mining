import requests
from bs4 import BeautifulSoup
import pymysql
from fake_useragent import UserAgent
import time


# 打开数据库连接
# db = pymysql.connect(host="172.17.0.1", port=3306, database="hogwarts", user="root", password="root")
db = pymysql.connect(host="106.14.25.134", port=3306, database="hogwarts", user="root", password="root")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


def get_data(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    cookies = "bid=Pne6vnvncmI;"
    cookies = """bid=Pne6vnvncmI; douban-fav-remind=1; __yadk_uid=GKaWPjdDi7QqoxzLXyAzbQXvA8iZ174Z; ll="108296"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23669; ct=y; __gads=ID=da2784121ca58106-2266ce911bca000c:T=1625132211:RT=1625132211:S=ALNI_MZGnV8L-8VTQZTBoKcL3i5868CnmQ; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1626160707%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.908857454.1620271463.1626160708.1626160886.20; __utmz=30149280.1626160886.20.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_id.100001.8cb4=ca1382265ee705db.1620271462.19.1626162454.1626155051.; ap_v=0,6.0; __utmb=30149280.13.7.1626161319104"""

    headers = {
        'User-Agent': UserAgent().random,
        'cookies': cookies
    }
    html = requests.get(url, headers=headers)
    time.sleep(1)
    return BeautifulSoup(html.text, "html.parser")


def parse_data(soup, cursor, catalog_id):
    table = soup.find("table", class_="olt")
    tr_list = table.find_all("tr", class_="")

    for item in tr_list:
        a = item.find("td", class_="title").find("a")
        url = a["href"]
        print(url)
        title = a["title"]
        text = a.text
        last_update_time_str = item.find("td", class_="time").text
        last_update_time = "2021-" + last_update_time_str + ":00"
        try:
            sql = "INSERT INTO t_house_detail(catalog_id,url,title,text,last_update_time,create_time) VALUES ('%s', '%s', '%s', '%s', '%s',now() )" \
                  % (catalog_id, url, title, text, last_update_time)
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # Rollback in case there is any error
            print(e)
            db.rollback()


def begin(item):
    suffix = "discussion?start="
    total = 8
    step = 25
    catalog_id = item["id"]
    start = 0
    base_url = item["url"] + suffix
    index = 0
    while index < total:
        catalog_url = base_url + str(start)
        print(catalog_url)
        try:
            soup = get_data(catalog_url)
            parse_data(soup, cursor, catalog_id)
        except Exception as e:
            print(e)

        start += step
        index += 1


# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT id,url FROM t_catalog")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

cursor.execute("SELECT * FROM t_index")
index = cursor.fetchone()
spider_index = int(index["index"])

mod = spider_index % 9
for datum in data:
    if datum["id"] == mod + 1:
        begin(datum)
        cursor.execute("UPDATE t_index SET `index` = `index` + 1")
        db.commit()

# 关闭数据库连接
db.close()
