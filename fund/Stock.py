import requests
import matplotlib.pyplot as plt
import numpy as np
import time

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号


def get_today_single_stock_data(code):
    url = "http://qt.gtimg.cn/q=" + code
    response = requests.get(url)
    source = response.text
    # print(source)
    replace_str = 'v_ff_' + code + '="'
    source_array = source.replace(replace_str, "").replace('";', "").split("~")
    item = {"股票名字": source_array[1], "股票代码": source_array[2], "当前价格": source_array[3], "昨收": source_array[4],
            "今开": source_array[5], "成交量（手）": source_array[36], "外盘": source_array[7], "内盘": source_array[8],
            "买一": source_array[9], "买一量（手）": source_array[10], "买二": source_array[11], "买二量（手）": source_array[12],
            "买三": source_array[13], "买三量（手）": source_array[14], "买四": source_array[15], "买四量（手）": source_array[16],
            "买五": source_array[17], "买五量（手）": source_array[18], "卖一": source_array[19], "卖一量": source_array[20],
            "卖二": source_array[21], "卖二量": source_array[22],
            "卖三": source_array[23], "卖三量": source_array[24],
            "卖四": source_array[25], "卖四量": source_array[26],
            "卖五": source_array[27], "卖五量": source_array[28],
            "最近逐笔成交": source_array[29], "时间": source_array[30], "涨跌": source_array[31],
            "涨跌 %": source_array[32], "最高": source_array[41], "最低": source_array[42],
            "价格 / 成交量（手） / 成交额": source_array[35], "成交额（万）": source_array[37], "换手率": source_array[38],
            "市盈率": source_array[39], "振幅": source_array[43], "流通市值": source_array[44], "总市值": source_array[45],
            "市净率": source_array[46], "涨停价": source_array[47], "跌停价": source_array[48]}

    return item


def get_real_time_flow_money(code):
    url = "http://qt.gtimg.cn/q=ff_" + code
    response = requests.get(url)
    source = response.text
    replace_str = 'v_ff_' + code + '="'
    source_array = source.replace(replace_str, "").replace('";', "").split("~")
    item = {"股票代码": source_array[0], "主力流入": float(source_array[1]), "主力流出": float(source_array[2]),
            "主力净流入": float(source_array[3]),
            "主力净流入/资金流入流出总和": float(source_array[4]), "散户流入": float(source_array[5]), "散户流出": float(source_array[6]),
            "散户净流入": float(source_array[7]), "散户净流入/资金流入流出总和": float(source_array[8]),
            "资金流入流出总和": float(source_array[9]),
            "名字": source_array[12], "日期": source_array[13]}
    return item


def get_access_data(code):
    url = "http://qt.gtimg.cn/q=s_pk" + code
    response = requests.get(url)
    source = response.text
    replace_str = 'v_s_pk' + code + '="'
    source_array = source.replace(replace_str, "").replace('";', "").split("~")
    item = {"买盘大单": source_array[0], "买盘小单": source_array[1], "卖盘大单": source_array[2], "卖盘小单": source_array[3].strip()}
    return item


if __name__ == '__main__':
    single_item = get_today_single_stock_data("sh600559")
    flow_money = get_real_time_flow_money("sh600559")
    access_data = get_access_data("sh600559")
    print(single_item)
    print(flow_money)
    print(access_data)

    # while True:
    #     print("")
    #     print("")
    #     print("--------------------------------------")
    #     print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #     single_item = get_today_single_stock_data("sz000789")
    #     flow_money = get_real_time_flow_money("sz000789")
    #     access_data = get_access_data("sz000789")
    #     print(single_item)
    #     print(flow_money)
    #     print(access_data)
    #     print(single_item["当前价格"])
    #     profit = (float(single_item["当前价格"]) - 24.5) * 100
    #     print(profit)
    #     time.sleep(60)

    labels = ['买盘大单', '买盘小单', '卖盘大单', '卖盘小单']
    values = [access_data['买盘大单'], access_data['买盘小单'], access_data['卖盘大单'], access_data['卖盘小单']]
    colors = ['yellow', 'green', 'red', 'blue']
    explode = 0.1, 0.05, 0.15, 0.2
    plt.pie(values, colors=colors, explode=explode, shadow=True, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

    # 输入统计数据
    waters = ('主力', '散户')
    input_number = np.array([flow_money['主力流入'], flow_money['散户流入']])
    output_number = np.array([-flow_money['主力流出'], -flow_money['散户流出']])
    total_number = np.array([flow_money['主力净流入'], flow_money['散户净流入']])

    bar_width = 0.2  # 条形宽度
    input = np.arange(len(waters))  # 主力条形图的横坐标
    output = input + 0.2  # 散户条形图的横坐标
    total = output + 0.2  # 散户条形图的横坐标

    # 使用两次 bar 函数画出两组条形图
    plt.bar(input, height=input_number, width=bar_width, color='blue', label='流入')
    plt.bar(output, height=output_number, width=bar_width, color='green', label='流出')
    plt.bar(total, height=total_number, width=bar_width, color='red', label='净流入')

    # 显示图例
    plt.legend()
    # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
    plt.xticks(np.arange(2) + 0.3, waters)
    # 纵坐标轴标题
    plt.ylabel('流入流出数据')
    # 图形标题
    plt.title('资金流入流出')

    plt.show()
