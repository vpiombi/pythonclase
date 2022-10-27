#pandas
import pandas as pd
import numpy as np


#limpieza de datos

data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')



data['votes']= data['votes'].str.replace(',','').astype(np.float)
data['votes'] = data['votes'].round(2)

data.loc[:,['votes']]


#Create a Word Cloud 

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#read text
stopwords=STOPWORDS
filt= (data['year']== 2021)


wc= WordCloud(
    background_color='white',
    stopwords=stopwords,
    height= 600,
    width=400
)


wc.generate(''.join(data.loc[filt,'plot']))

#save the file
wc.to_file('wordcloud_year_output.png')