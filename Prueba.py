import pandas
#Instalar import matplotlib.pyplot
url = "https://raw.githubusercontent.com/vpiombi/pythonclase/main/imdb-videogames.csv"
data = pandas.read_csv(url)
print(data)

#Primero entendemos los formatos de los datos con los que contamos 
data.info()
print(data)

