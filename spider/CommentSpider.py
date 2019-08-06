import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import time

# list = []
# with open('cup.csv', 'r', encoding='utf-8') as input_file:
#     i = 0
#     for line in input_file.readlines():
#         if i != 0:
#             item = line.split('#')
#             print(item)
#             obj = {
#                 'title': item[0],
#                 'detail_url': item[1],
#                 'comment_url': item[3],
#                 'comment_count': item[4].replace('\\n', '')
#             }
#             # print(obj)
#             list.append(obj)
#         i += 1
ktsts = time.time()
_ksTS = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-3:])

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/76.0.3809.87 Safari/537.36'

headers = {
    'User-Agent': user_agent
}
callback = "jsonp%s" % (int(str(ktsts)[-3:]) + 1)
url = "https://rate.taobao.com/feedRateList.htm" \
      "?auctionNumId=591994262028&userNumId=781082871&currentPageNum=2" \
      "&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=" \
      "&hasSku=false&folded=0" \
      "&ua=098%23E1hvcpvnvRwvUpCkvvvvvjiPRF5vgj3EPLsWgjnEPmPpgjrR" \
      "PssOtjinRsqyAjtjR9wCvva47rMNz2Yo3QhvChCCvvm5vpvhphvhH2yCvvBvpvvvvphvCyCCvvvvvUyCvvXmp99he1Kiv" \
      "pvUphvh%2BLRwoqTtvpvIphvU%2F9vvphtvpvkRvvCvY6CvjvUvvhBGphv" \
      "wv9vvBHBvpvFRvvCCf9yCvh1HZa6vIqHkLkx%2FQj7J%2B3%2BdjL4UAfpgnCX%2Bm7zwdig" \
      "yoAn7rXZzR3r%2FVAilaBoAVA%2BanRsX%2B2D9Pz6eaJASdcvrNB3rA8g7j6B1bPox2QhvCvv" \
      "vvvvtvpvhphvvvUhCvv14caDvUa147DitDrGtvpvhphvvvv%3D%3D" \
      "&_ksTS=" + _ksTS + \
      "&callback=" + callback
url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=587770073813&order=3&sellerId=1914459560&currentPage=1'
r = requests.get(url, headers).text
print(r)
