from asyncio.windows_events import NULL
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')


data['votes']= data['votes'].str.replace(',','').astype(float)
data['votes'] = data['votes'].round(2)

data.loc[:,['votes']]

data.drop(['url'], axis=1, inplace=True)
data.head()

header_names=['Games', 'name', 'url', 'year', 'certificate', 'rating', 'votes', 'plot', 'Action', 'Adventure','Comedy', 'Crime', 'Family', 'Fantasy', 'Mystery', 'Sci-Fi', 'Thriller']
file=pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv', header=None, skiprows=1, names=header_names)


file.drop(file[(file['Games' ==NULL]) ].index)

fig = px.pie(file, values="Games", names='certificate')
fig.show()