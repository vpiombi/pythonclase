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


genero = data[['Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy', 'Mystery', 'Sci-Fi', 'Thriller']]
genero


grafico = alt.Chart(data).mark_area().encode(
    x="year",
    y="certificate",
    color= genero,
     tooltip=[
        alt.Tooltip(genero,title="Type of Energy"),
        alt.Tooltip('year', title='Year'),
        alt.Tooltip('certificate', title='Production')
    ]
).properties(width = 900, height = 500)
grafico.title = "Europe's Energy Production per Year"

grafico