from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid


def use_chrome(url):
    profile = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="d:\\chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(100)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "booking-select")))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    use_soup(soup)


def use_soup(soup):
    flight_list = soup.find("div", class_="booking-select").find("div", id="sylvanas_3") \
        .find_all("article", class_="flight")

    data = flight_list[0]
    print(data)

    # result = {}
    #
    # result["flight_no"] = data.find("section", class_="summary")
    # print(result)

    # result_set = []
    # for data in list:
    #
    #     left = data.find("div", class_="fligthL")
    #     flight_info = left.find("div", class_="zls-flgno").find("div", class_="zls-flgno-info zh").text
    #
    #     result["plane"] = flight_info[6:]
    #     start_time_info = left.find("div", class_="zls-flgtime zls-flgtime-r zls-flgtime-dep").text
    #     result["start_time"] = start_time_info[0:5]
    #     result["start_airport"] = start_time_info[5:]
    #     end_time_info = left.find("div", class_="zls-flgtime zls-flgtime-arr").text
    #     result["end_time"] = end_time_info[0:5]
    #     result["end_airport"] = end_time_info[5:]
    #     duration = left.find("div", class_="zls-flg-during zls-trans-info").find("div", class_="zls-flg-time").text
    #     result["duration"] = duration
    #     right = data.find("div", class_="fligthR")
    #     ticket = right.find("ul").find_all("li", class_="zls-cabin-cell")[3].text
    #     result["duration"] = ticket.replace("¥", "")
    #     result_set.append(result)
    #
    # for item in result_set:
    #     print(item)


if __name__ == '__main__':
    day = "201128"

    series_id = str(uuid.uuid4()).replace("-", "")
    # 东航 南京->广州
    url = "http://www.ceair.com/booking/sha-can-" + day + "_CNY.html?seriesid=" + series_id
    # print(url)
    use_chrome(url)
