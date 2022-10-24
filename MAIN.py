#pandas
import pandas as pd
import numpy as np


#limpieza de datos

data = pd.read_csv('https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv')



data['votes']= data['votes'].str.replace(',','').astype(np.float)
data['votes'] = data['votes'].round(2)

data.loc[:,['votes']]

data.info()
