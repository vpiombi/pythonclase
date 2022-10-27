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


#Create a Word Cloud 

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


#Read plot from year 1962
stopwords=STOPWORDS


filt= (data['year']== 1962) 


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#save the file
wc.to_file('wordcloud_year_output1962.png')

#Read plot from year 2022
stopwords=STOPWORDS


filt= (data['year']== 2022) 


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#save the file
wc.to_file('wordcloud_year_output2022.png')

