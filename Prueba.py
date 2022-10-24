import pandas
import matplotlib
url = "https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv"
data = pandas.read_csv(url)
print(data)


data.drop(['Unnamed: 0', 'url'], axis=1, inplace=True)
data.head()

data.columns



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


filepath = "https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv"
df = pd.read_csv(filepath)

df.columns