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
    # df = pd.DataFrame(data=funds, index=None)
    # df.to_csv('pandas1.csv', mode='a', header=False, index=False)


if __name__ == '__main__':
    data_now = int(round(time.time() * 1000))
    fund_list = [
        {
            "code": "519674",
            "name": "银河创新成长混合",
            "base_price": 5.8138,
            "amount": 1235.17
        },
        {
            "code": "320007",
            "name": "诺安成长混合",
            "base_price": 1.8213,
            "amount": 2031.54
        },
        {
            "code": "001102",
            "name": "前海开源国家比较优势混合",
            "base_price": 3.2064,
            "amount": 1942.45
        },
        # {
        #     "code": "003096",
        #     "name": "中欧医疗健康混合C",
        #     "base_price": 2.9805,
        #     "amount": 420.00
        # },
        # {
        #     "code": "001559",
        #     "name": "天弘医疗健康混合C",
        #     "base_price": 1.9171,
        #     "amount": 417.29
        # },
        # {
        #     "code": "050026",
        #     "name": "博时医疗保健行业混合A",
        #     "base_price": 3.9995,
        #     "amount": 81.29
        # },
        {
            "code": "001632",
            "name": "天弘中证食品饮料指数C",
            "base_price": 3.0328,
            "amount": 247.29
        },
        {
            "code": "161725",
            "name": "招商中证白酒指数",
            "base_price": 1.1842,
            "amount": 4325.83
        },
        {
            "code": "110011",
            "name": "易方达中小盘混合",
            "base_price": 8.5333,
            "amount": 112.50
        },
        {
            "code": "519026",
            "name": "海富通中小盘混合",
            "base_price": 1.7704,
            "amount": 1192.92
        },
        {
            "code": "003634",
            "name": "嘉实农业产业股票",
            "base_price": 2.2254,
            "amount": 1186.31
        },
        # {
        #     "code": "007531",
        #     "name": "华宝券商ETF联接C",
        #     "base_price": 1.6574,
        #     "amount": 482.69
        # },
        {
            "code": "007230",
            "name": "兴全沪深300指数(LOF)C",
            "base_price": 2.5192,
            "amount": 508.09
        },
        # {
        #     "code": "004857",
        #     "name": "广发中证全指建筑材料指数C",
        #     "base_price": 1.4114,
        #     "amount": 354.25
        # },
        {
            "code": "000977",
            "name": "长城环保主题混合",
            "base_price": 2.3606,
            "amount": 999.74
        },
        {
            "code": "007412",
            "name": "景顺长城绩优成长混合",
            "base_price": 1.7752,
            "amount": 281.66
        },
        {
            "code": "005827",
            "name": "易方达蓝筹精选混合",
            "base_price": 2.8131,
            "amount": 355.48
        },

    ]

    while (True):
        print("")
        print("")
        print("--------------------------------------")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        try:
            calculate(data_now, fund_list)
        except Exception as e:
            print(e)
        time.sleep(60)
