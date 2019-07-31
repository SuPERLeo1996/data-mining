import numpy as np
import pandas as pd

df = pd.read_csv('top250_movie.csv', sep='#', encoding='utf8')

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 500)
# df.head()
# print(df.head())
#
# print(df.duplicated().value_counts())
#
# print(len(df.movie_name.unique()))


# 查看国家或地区参与电影制作的排名情况
country = df['movie_country'].str.split(' ').apply(pd.Series)
print(country)

all_country = country.apply(pd.value_counts).fillna('0')
all_country.columns = ['area1', 'area2', 'area3', 'area4', 'area5', 'all_counts']
all_country['area1'] = all_country['area1'].astype(int)
all_country['area2'] = all_country['area2'].astype(int)
all_country['area3'] = all_country['area3'].astype(int)
all_country['area4'] = all_country['area4'].astype(int)
all_country['area5'] = all_country['area5'].astype(int)

all_country['all_counts'] = all_country['area1'] + all_country['area2'] + all_country['area3'] + all_country['area4'] + \
                            all_country['area5']
# 降序
all_country = all_country.sort_values(['all_counts'], ascending=False)

print(all_country)

# 关于电影类型的字段分析
all_type = df['movie_type'].str.split(' ').apply(pd.Series)
print(all_type)
all_type = all_type.apply(pd.value_counts).fillna('0')
print(all_type)

# all_type.columns = ['type1', 'type2', 'type3', 'type4', 'type5', 'all_counts']
# all_type['type1'] = all_type['type1'].astype(int)
# all_type['type2'] = all_type['type2'].astype(int)
# all_type['type3'] = all_type['type3'].astype(int)
# all_type['type4'] = all_type['type4'].astype(int)
# all_type['type5'] = all_type['type5'].astype(int)
# all_type['type6'] = all_type['type6'].astype(int)
#
#
# all_type['all_counts'] = all_type['type1'] + all_type['type2'] + all_type['type3'] + all_type['type4'] + all_type[
#     'type5'] + all_type['type6']
#
# print(all_type)
# all_type = all_type.sort_values(['all_counts'], ascending=False)
# print(all_type)
