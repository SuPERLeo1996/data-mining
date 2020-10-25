from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def use_chrome(url):
    profile = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="d:\\chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(100)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "zls-flight")))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    use_soup(soup)


def use_soup(soup):
    list = soup.find_all("li", class_="zls-flight-cell")

    result_set = []
    for data in list:
        result = {}
        left = data.find("div", class_="fligthL")
        flight_info = left.find("div", class_="zls-flgno").find("div", class_="zls-flgno-info zh").text
        result["flight_no"] = flight_info[0:6]
        result["plane"] = flight_info[6:]
        start_time_info = left.find("div", class_="zls-flgtime zls-flgtime-r zls-flgtime-dep").text
        result["start_time"] = start_time_info[0:5]
        result["start_airport"] = start_time_info[5:]
        end_time_info = left.find("div", class_="zls-flgtime zls-flgtime-arr").text
        result["end_time"] = end_time_info[0:5]
        result["end_airport"] = end_time_info[5:]
        duration = left.find("div", class_="zls-flg-during zls-trans-info").find("div", class_="zls-flg-time").text
        result["duration"] = duration
        right = data.find("div", class_="fligthR")
        ticket = right.find("ul").find_all("li", class_="zls-cabin-cell")[3].text
        result["duration"] = ticket.replace("¥", "")
        result_set.append(result)

    for item in result_set:
        print(item)


if __name__ == '__main__':
    day = "2020-11-28"
    # 南航 广州->上海
    # url = "https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CAN&c2=SHA&d1=" + day \
    #       + "&at=1&ct=0&it=0&b1=CAN&b2=SHA-PVG"
    # 南航 上海->广州
    # url = "https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=SHA&c2=CAN&d1=" + day \
    #       + "&at=1&ct=0&it=0&b1=SHA-PVG&b2=CAN"

    # 南航 南京->广州
    url = "https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=NKG&c2=CAN&d1=" + day \
          + "&at=1&ct=0&it=0&b1=NKG&b2=CAN"
    use_chrome(url)
