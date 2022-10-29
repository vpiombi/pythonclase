import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')

#Limpieza de datos

data['votes']= data['votes'].str.replace(',','').astype(float)
data['votes'] = data['votes'].round(2)


data.loc[:,['votes']]

data.drop(['url'], axis=1, inplace=True)
data.head()

data["votes"].fillna(0, inplace = True)


#Grafico 1 Bar Chart

#Grafico con año y genero

generoxanio = data[['year', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('year').sum()
generoxanio


generoxanio = generoxanio[generoxanio.index <= 2022]

barra1 = px.bar(generoxanio, x=generoxanio.index, y=generoxanio.columns, title='Cantidad de juegos publicados',
             color_discrete_sequence=px.colors.qualitative.Plotly)
barra1.show()

#Grafico 2 Bar Chart


#Grafico con certificado y genero



generoxcertificado = data[['certificate', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('certificate').sum()
generoxcertificado


barra2 = px.bar(generoxcertificado, x=generoxcertificado.index, y=generoxcertificado.columns, title='Cantidad de juegos por certificado',
             color_discrete_sequence=px.colors.qualitative.Plotly)
barra2.show()

#Grafico 3 Pie Chart

fig = px.pie(data, values="Unnamed: 0", names='certificate')
fig.show()

#Grafico 4 Scatterplot

scatter = px.scatter(data,x='rating', y = 'votes', color= "votes",hover_name='name',size = "votes")
scatter.show()

#Grafico 5  Line Chart
#Genero de juegos y raiting


generoxraiting = data[['rating', 'Action', 'Adventure', 'Comedy', 'Crime', 'Family', 'Fantasy',
                    'Mystery', 'Sci-Fi', 'Thriller']].groupby('rating').sum()
generoxraiting

linea = px.line(generoxraiting, x=generoxraiting.index, y=generoxraiting.columns, title='Genero de juegos y rating',
             color_discrete_sequence=px.colors.qualitative.Plotly)
linea.show()

#Grafico 6 Word Cloud


#clear plot's column without text
data['plot']= data['plot'].str.replace('Add','').astype(np.object)
data['plot']= data['plot'].str.replace('Plot','').astype(np.object)
data['plot']= data['plot'].str.replace('Full','').astype(np.object)
data['plot']= data['plot'].str.replace('full','').astype(np.object)
data['plot']= data['plot'].str.replace('summary','').astype(np.object)
data['plot']= data['plot'].str.replace('set','').astype(np.object)
data['plot']= data['plot'].str.replace('See','').astype(np.object)
data['plot']= data['plot'].str.replace('one','').astype(np.object)
data['plot']= data['plot'].str.replace('back','').astype(np.object)
data['plot']= data['plot'].str.replace('take','').astype(np.object)
data['plot']= data['plot'].str.replace('make','').astype(np.object)
data['plot']= data['plot'].str.replace('will','').astype(np.object)
data['plot']= data['plot'].str.replace('now','').astype(np.object)
data['plot']= data['plot'].str.replace('way','').astype(np.object)
data['plot']= data['plot'].str.replace('find','').astype(np.object)
data['plot']= data['plot'].str.replace('Two','').astype(np.object)
data['plot']= data['plot'].str.replace('two','').astype(np.object)
data['plot']= data['plot'].str.replace('summary','').astype(np.object)

#Crear un Word Cloud 

from wordcloud import WordCloud, STOPWORDS


##Word Cloud de los plots del año 1960 a 1980
stopwords=STOPWORDS


filt= (data['year']<= 1980) & (data['year']>= 1960)


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#guardar el archivo
wc.to_file('wordcloud_year_output1960_1980.png')

#Word Cloud de los plots del año 1980 a 2000
stopwords=STOPWORDS


filt= (data['year']<= 2000) & (data['year']>= 1980)


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#guardar el archivo

wc.to_file('wordcloud_year_output1980_2000.png')

#Word Cloud de los plots del año 2000 a 2022
stopwords=STOPWORDS


filt= (data['year']<= 2022) & (data['year']>= 2000)


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#Guardar el archivo

wc.to_file('wordcloud_year_output2000_2022.png')
