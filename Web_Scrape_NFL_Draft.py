import pandas as pd

url_template = "http://www.pro-football-reference.com/years/{year}/draft.htm"
# for each year from 1950 to 2017
dataset = []
for year in range(1950, 2017):
    df_list = pd.read_html(url_template.replace("{year}",str(year)), skiprows = 0, header=1,  index_col=1)[0]
    df_list['Draft Year']= year
    dataset.append(df_list)
dataset = pd.concat(dataset)

# removing all the multiple headers
dataset = dataset[dataset.Player != 'Player']

# export to excel
dataset.to_excel('NFL_Draft_1950_to_2017.xlsx')
