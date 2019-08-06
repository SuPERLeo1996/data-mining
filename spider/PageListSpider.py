from bs4 import BeautifulSoup
import requests
import random
import json
import time


def get_url_list():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                 ' Chrome/76.0.3809.87 Safari/537.36'
    cookies = 'miid=799219851787240040; t=61aeb359db6bb102c84f3f09cf6911f5;' \
              ' cna=YS2PFSl22wkCAXJdDQw+/FeQ; hng=CN%7Czh-CN%7CCNY%7C156; ' \
              'thw=cn; mt=ci%3D-1_1; _m_h5_tk=fc14ce3733d6a3b0416dde1176bdac33_1565077347691;' \
              ' _m_h5_tk_enc=fb70a1259a5e7b27461c26ff026b814c; v=0; ' \
              'cookie2=1455005dfa3ee4dcf99adf5d5b49b258; _tb_token_=7173e1b63563e;' \
              ' alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; ' \
              'JSESSIONID=220D145F5AE88D711C5BD7507D1A8D3A; ' \
              'l=cBSMsgzlqYDbkUu2BOfwVuI8Ua_OqIObzsPzw49gOICPOv5Fl6DRWZF_-ULwCnGVK6mw-3P0SFC4BlYOayh2nNqMhwIEW11..;' \
              ' isg=BL-_QZqK3r8rUdqpizbkRHLxTpOJDBHIE8DAS1GNFG4cYNziW3Y3ll2ypnA7OOu-'
    headers = {
        'User-Agent': user_agent,
        'cookies': cookies
    }
    i = 1

    with open('cup.csv', 'w', encoding='utf-8') as output_file:
        output_file.write(
            "raw_title#detail_url#comment_url#comment_count\n")
        while i < 101:
            ktsts = time.time()
            _ksTS = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-3:])
            callback = "jsonp%s" % (int(str(ktsts)[-3:]) + 1)
            data_value = 60 * i
            url = "https://s.taobao.com/list?data-key=s&data-value=" + str(
                data_value) + "&ajax=true&_ksTS=" + _ksTS + "&callback=" + callback + "&spm=a219r.lm5734.15.1.34452f73QRGwHZ&q=%E6%96%87%E8%83%B8&cat=1625&style=grid&seller_type=taobao&sort=sale-desc&bcoffset=0&pb=false&s=60"
            print(url)
            response = requests.get(url, headers=headers).text
            response = response.replace(callback+'(', '').replace(');', '')
            result_json = json.loads(response)
            question = result_json["mods"]['itemlist']
            if question['status'] == 'show':
                list_page = question['data']['auctions']
                print(list_page)
                for item in list_page:
                    output_file.write(
                        '{}#{}#{}#{}\n'.format(item['raw_title'], item['detail_url'], item['comment_url'],
                                               item['comment_count']))
            i += 1
            time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    get_url_list()
