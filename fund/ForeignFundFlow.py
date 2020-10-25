import requests
import json
import time

def get():
    url = "http://push2his.eastmoney.com/api/qt/kamt.kline/get?fields1=f1,f3,f5&fields2=f51,f52&klt=101&lmt=500&ut=b2884a393a59ad64002292a3e90d46a5"
    response = requests.get(url)
    source = response.text
    source_json = json.loads(source)
    # print(source)
    return source_json["data"]


def get_today_data(json):
    hk2sh = json["hk2sh"]
    hk2sz = json["hk2sz"]
    s2n = json["s2n"]
    sh_today = hk2sh[-1]
    sz_today = hk2sz[-1]
    n_today = s2n[-1]
    result = {
        "hk2sh": sh_today,
        "hk2sz": sz_today,
        "s2n": n_today
    }
    print(result)
    return result


def get__month_data(json):
    pass


def get_category_data(json):
    pass


if __name__ == '__main__':


    while(True):
        print("")
        print("")
        print("--------------------------------------")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        data = get()
        get_today_data(data)
        time.sleep(60)

