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

data.drop(['Unnamed: 0', 'url'], axis=1, inplace=True)
data.head()

data.info()


grafico3 = px.scatter(data,x='rating', y = 'votes', color= "votes",hover_name='name')
grafico3.show()