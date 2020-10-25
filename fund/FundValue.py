import requests
import json
import time
import pandas as pd


def calculate(timestamp, funds):
    total = 0
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    for item in funds:
        code = item["code"]
        url = "http://fundgz.1234567.com.cn/js/{}.js?rt={}".format(code, timestamp)
        # print(url)
        response = requests.get(url)
        source = response.text
        # print(source)
        source = source.replace("jsonpgz(", "").replace(");", "")
        # print(source)
        source_json = json.loads(source)
        item["new_price"] = source_json["gsz"]
        item["name"] = source_json["name"]
        item["profit"] = (float(source_json["gsz"]) - item["base_price"]) * item["amount"]
        item["date"] = now
        total = item["profit"] + total
        print(item)
    print(total)
    df = pd.DataFrame(data=funds, index=None)
    df.to_csv('pandas.csv', mode='a', header=False, index=False)


if __name__ == '__main__':
    data_now = int(round(time.time() * 1000))
    fund_list = [
        {
            "code": "001102",
            "base_price": 2.7041,
            "amount": 369.81
        },
        {
            "code": "003096",
            "base_price": 2.8260,
            "amount": 353.86
        },
        {
            "code": "519674",
            "base_price": 6.6507,
            "amount": 71.18
        },
        {
            "code": "519026",
            "base_price": 1.7516,
            "amount": 285.45
        },
        {
            "code": "320007",
            "base_price": 2.1182,
            "amount": 94.42
        }
    ]

    while (True):
        print("")
        print("")
        print("--------------------------------------")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        calculate(data_now, fund_list)
        time.sleep(60)
