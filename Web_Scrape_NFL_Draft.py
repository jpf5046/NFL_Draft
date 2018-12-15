# -*- coding: utf-8 -*-
import pandas as pd

url_template = "http://www.pro-football-reference.com/years/{year}/draft.htm"
# for each year from 1967 to (and including) 2016
dataset = []
for year in range(1950, 2017):
    df_list = pd.read_html(url_template.replace("{year}",str(year)), skiprows = 0)[0]
    dataset.append(df_list)
dataset = pd.concat(dataset)


# removing first row of multi-header
dataset.columns = dataset.columns.droplevel(0)


# removing all the multiple headers
dataset = dataset[dataset.Player <> 'Player']

# export to excel
dataset.to_excel('NFL_Draft_1950_to_2017.xlsx')
