#pandas
import pandas as pd
import numpy as np


#limpieza de datos

data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')


data['votes']= data['votes'].str.replace(',','').astype(np.float)
data['votes'] = data['votes'].round(2)

data.loc[:,['votes']]

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



#Create a Word Cloud 

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


#Read plot from year 1960 a 1980
stopwords=STOPWORDS


filt= (data['year']<= 1980) & (data['year']>= 1960)


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#save the file
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

#save the file
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

#save the file
wc.to_file('wordcloud_year_output2000_2022.png')

