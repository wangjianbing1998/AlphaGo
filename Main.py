# coding=gbk

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['text.usetex'] = True
import seaborn as sns

import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 6)
pd.set_option('precision', 2)

df = pd.read_excel('PM2.5-meteos.xlsx', index_col=[0])
print(df)

data_2019 = df[['2019年']]
data_2019['year'] = '2019'
data_2019.rename(columns={'2019年': 'value'}, inplace=True)

data_2020 = df[['2020年']]
data_2020['year'] = '2020'
data_2020.rename(columns={'2020年': 'value'}, inplace=True)

data = pd.concat([data_2019, data_2020])
data = data.reset_index(drop=False)

e_i = 'TAD'


def plot_box():
    flatui = ['#4472c5', '#FF6600']
    my_map = sns.color_palette(flatui)

    sns.set(style="ticks")
    sns.boxplot(x='date', y='value', data=data, showfliers=False, hue='year', width=0.5, linewidth=1.3, palette=my_map)
    plt.xlabel('Date', fontsize='larger')
    plt.ylabel(r"$PM2.5\ \ [ug/{m^3}]$", fontsize='larger')
    # sns.despine(offset=5, trim=True)


plt.figure()
plot_box()
plt.title('Observation PM2.5', fontsize='x-large')
plt.savefig('Main.png')
plt.show()
