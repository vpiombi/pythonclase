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


#Genero de juegos y raiting

generoxpuntaje = data[['rating', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('rating').sum()
generoxpuntaje

linea = px.line(generoxpuntaje, x=generoxpuntaje.index, y=generoxpuntaje.columns, title='Genero de juegos y rating',
             color_discrete_sequence=px.colors.qualitative.Plotly)
linea.show()
