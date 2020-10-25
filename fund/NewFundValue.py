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
        item["rate"] = source_json["gszzl"] + "%"
        total = item["profit"] + total
        print(item)
    print(total)
    df = pd.DataFrame(data=funds, index=None)
    df.to_csv('pandas1.csv', mode='a', header=False, index=False)


if __name__ == '__main__':
    data_now = int(round(time.time() * 1000))
    fund_list = [
        {
            "code": "519674",
            "name": "银河创新成长混合",
            "base_price": 5.8451,
            "amount": 1057.47
        },
        {
            "code": "320007",
            "name": "诺安成长混合",
            "base_price": 1.8578,
            "amount": 1453.36
        },
        {
            "code": "001102",
            "name": "前海开源国家比较优势混合",
            "base_price": 3.0218,
            "amount": 1662.93
        },
        {
            "code": "003096",
            "name": "中欧医疗健康混合C",
            "base_price": 2.9883,
            "amount": 1505.87
        },
        {
            "code": "001559",
            "name": "天弘医疗健康混合C",
            "base_price": 1.9700,
            "amount": 558.38
        },
        {
            "code": "050026",
            "name": "博时医疗保健行业混合A",
            "base_price": 4.0545,
            "amount": 246.64
        },
        {
            "code": "001632",
            "name": "天弘中证食品饮料指数C",
            "base_price": 3.0328,
            "amount": 494.59
        },
        {
            "code": "161725",
            "name": "招商中证白酒指数分级",
            "base_price": 0.9873,
            "amount": 1924.35
        },
        {
            "code": "110011",
            "name": "易方达中小盘混合",
            "base_price": 7.3737,
            "amount": 46.11
        },
        {
            "code": "519026",
            "name": "海富通中小盘混合",
            "base_price": 1.7809,
            "amount": 1212.84
        },
        {
            "code": "003634",
            "name": "嘉实农业产业股票",
            "base_price": 2.2254,
            "amount": 1482.89
        },
        {
            "code": "007531",
            "name": "华宝券商ETF联接C",
            "base_price": 1.7217,
            "amount": 290.41
        },
        {
            "code": "007230",
            "name": "兴全沪深300指数(LOF)C",
            "base_price": 2.4716,
            "amount": 299.40
        },
        {
            "code": "004857",
            "name": "广发中证全指建筑材料指数C",
            "base_price": 1.5051,
            "amount": 132.88
        },
        {
            "code": "000977",
            "name": "长城环保主题混合",
            "base_price": 2.3661,
            "amount": 853.74
        },
        {
            "code": "007412",
            "name": "景顺长城绩优成长混合",
            "base_price": 1.7752,
            "amount": 281.66
        },

    ]

    while (True):
        print("")
        print("")
        print("--------------------------------------")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        calculate(data_now, fund_list)
        time.sleep(60)
