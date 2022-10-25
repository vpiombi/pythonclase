import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')



data['votes']= data['votes'].str.replace(',','').astype(float)
data['votes'] = data['votes'].round(2)

data.loc[:,['votes']]

data.drop(['Unnamed: 0', 'url'], axis=1, inplace=True)
data.head()

generoxanio = data[['year', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('year').sum()
generoxanio

generoxanio = generoxanio[generoxanio.index <= 2022]

fig = px.line(generoxanio, x=generoxanio.index, y=generoxanio.columns, title='Number of games published',
             color_discrete_sequence=px.colors.qualitative.Bold)
fig.show()