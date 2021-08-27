from selenium.webdriver import ActionChains
from seleniumwire import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)


def interceptor(request):
    request.headers['spider'] = 'fangfanglinjie'


browser.request_interceptor = interceptor

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

wait = WebDriverWait(browser, 20)

browser.get('https://spider.test.baixing.cn/detail/ff9ed1a83d1a43a79cb9a4459aa90a35')
input = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#view-owner'))
)

phone_btn = browser.find_element_by_css_selector('#view-phone-left')
ActionChains(browser).click(phone_btn).perform()