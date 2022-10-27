import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')

data.info()

data['votes']= data['votes'].str.replace(',','').astype(float)
data['votes'] = data['votes'].round(2)

data.loc[:,['votes']]

data.drop(['Unnamed: 0', 'url'], axis=1, inplace=True)
data.head()


#Grafico con año y genero

generoxanio = data[['year', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('year').sum()
generoxanio




#Grafico haciendo la relacion entre generos

genero = data[['Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy', 'Mystery', 'Sci-Fi', 'Thriller']]
genero


genres = pd.DataFrame()
for col in genero.columns:
    genres[col] = genero[genero[col]==True].sum()
    genres[col] /= genres[col].max()
    
fig = plt.figure(figsize=(16,6))
sns.heatmap(genres, cmap="RdPu", annot=True)
plt.show()
