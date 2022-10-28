from asyncio.windows_events import NULL
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



generoxcertificado = data[['certificate', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('certificate').sum()
generoxcertificado


generoxcertificado.drop





grafico = px.bar(generoxcertificado, x=generoxcertificado.index, y=generoxcertificado.columns, title='Cantidad de juegos por certificado',
             color_discrete_sequence=px.colors.qualitative.Plotly)
grafico.show()
