from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def use_chrome(url):
    profile = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="C:\\Users\\baixing\\Downloads\\chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(100)
    element = WebDriverWait(driver, 10)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    page = driver.find_elements_by_xpath("//div[@class='fold-page-content']")
    driver.execute_script('arguments[0].scrollIntoView();', page[-1])  # 拖动到可见的元素去
    next_page = driver.find_element_by_xpath("//span[@class='read-all']")
    driver.execute_script("arguments[0].click();", next_page)
    # size_list = soup.find("div", class_="doc-summary-wrap").find_all("em")

    size = 5

    i = 1
    s = ""
    while True:
        page = driver.find_elements_by_xpath("//div[@id='pageNo-" + str(i) + "']")
        driver.execute_script('arguments[0].scrollIntoView();', page[-1])
        time.sleep(3)
        content_list = BeautifulSoup(driver.page_source, 'lxml').find_all("p", class_="reader-word-layer")
        for item in content_list:
            s += item.text
        print(s)

        i = i + 1
        if i > size:
            break

    with open('data.txt', 'a+', encoding='utf-8') as f:
        f.write(s)


if __name__ == '__main__':
    url = "https://wk.baidu.com/view/d0a5a5e514791711cd7917af"
    use_chrome(url)
