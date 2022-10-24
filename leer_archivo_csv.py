import csv
with open ('./pythonclase/imdb-videogames.csv') as File:
    misDatosReunion= csv.DictReader (File, delimiter=';')
    for asistente in misDatosReunion:
        print(asistente['Nombre']+' - ' + asistente['Correo'] + ' - ' + asistente['Rol'])