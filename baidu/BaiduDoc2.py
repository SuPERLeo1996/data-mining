from selenium import webdriver
from bs4 import BeautifulSoup

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(executable_path="C:\\Users\\baixing\\Downloads\\chromedriver.exe", chrome_options=options)
    driver.get('https://wenku.baidu.com/view/506f50f88662caaedd3383c4bb4cf7ec4bfeb637')

    html = driver.page_source
    bf1 = BeautifulSoup(html, 'lxml')
    result = bf1.find_all('p', class_='reader-word-layer')

    s = ""
    for item in result:
        s += item.text

    print(s)
    with open('data.txt', 'a+', encoding='utf-8') as f:
        f.write(s)

    driver.quit()
