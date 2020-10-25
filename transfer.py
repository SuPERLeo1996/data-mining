import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql

# import MySQLdb

if __name__ == '__main__':
    infos = []
    with open('sensi_words.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            infos.append(line.strip())

    db = pymysql.connect("rm-bp1egq19zcvebvav1no.mysql.rds.aliyuncs.com", "root", "SHboka20171115", "lavipeditum")
    details = []
    word_str = ""
    string = "insert into t_sensitive(word) values "
    i = 0
    for info in infos:
        if i != 0:
            string += ","
        else:
            i+=1
        string += "('" + str(info) + "')"

    print(string)
    cursor = db.cursor()
    cursor.execute("%s" % string)
    db.commit()
