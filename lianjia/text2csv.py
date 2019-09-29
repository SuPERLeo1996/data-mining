import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    infos = []
    with open('detail.csv','r',encoding='utf-8') as file:
        for line in file.readlines():
            infos.append(line.strip())

    details = []
    for info in infos:
        temp = info.split("#")
        detail = {}
        detail["price"] = str(temp[0])
        detail["unit"] = temp[1].replace("元/平米","")
        detail["village"] = temp[2]
        loc = temp[3].split("\xa0")
        detail["location1"] = loc[0]
        detail["location2"] = loc[1]
        detail["location3"] = loc[2]
        detail["underground"] = temp[4]
        detail["apartment"] = temp[5].replace("房屋户型","")
        detail["area"] = temp[6].replace("建筑面积","").replace("㎡","")
        detail["orientation"] = temp[7].replace("房屋朝向","")
        detail["decoration"] = temp[8].replace("装修情况","")
        detail["lift"] = temp[9].replace("配备电梯","")
        details.append(detail)

    df = pd.DataFrame(data=details,index=None)
    print(df)
    df.to_csv('pandas.csv',index=0)

