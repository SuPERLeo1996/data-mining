import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

cookies = "bid=Pne6vnvncmI;"
headers = {
    'User-Agent': user_agent,
    'cookies': cookies
}
html = requests.get("https://www.douban.com/group/shanghaizufang/discussion?start=350", headers=headers)
soup = BeautifulSoup(html.text, "html.parser")
print(soup)

table = soup.find("table", class_="olt")
tr_list = table.find_all("tr", class_="")

for item in tr_list:
    a = item.find("td", class_="title").find("a")
    url = a["href"]
    print(url)

    title = a["title"]
    print(title)
    text = a.text
    print(a.text)
    last_update_time_str = item.find("td", class_="time").text
    print(last_update_time_str)
    data = {}
    data["title"] = title
    data["url"] = url
    data["text"] = text
    last_update_time = "2021-" + last_update_time_str + ":00"
    data["last_update_time"] = last_update_time
    print(data)


