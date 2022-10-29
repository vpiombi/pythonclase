# Proyecto Final de Python _ Grupo 2

# Descripción: 
En nuestro proyecto final utilizamos Python para analizar los datos de un archivo csv, que contiene información acerca de los videojuegos que fueron lanzados entre el año 1962 y 2022. Primero hace una limpieza del dataset y luego transforma los datos necesarios por medio de representaciones gráficas para sacar conclusiones. 
A continuación, listamos los gráficos que van a poder visualizar al ejecutar el código:

- Grafico de Barras (categoria x Año): 

     - En este gráfico de barras podemos ver la cantidad de juegos que fueron publicados en cada año por categoría. 

  <img width="1087" alt="Capturar" src="https://user-images.githubusercontent.com/114704675/198758177-06f9e458-0450-4f8a-b37e-4f6ecc06f138.PNG">

     Podemos observar que la categoría de juegos que está creciendo más en los últimos años son los de Acción y de Aventura


- Grafico de Barras (Categoria x certificados): 

    -En este gráfico de barras podemos ver que certificado tiene cada juego con su respectiva categoría:
    
 <img width="1084" alt="Capturar" src="https://user-images.githubusercontent.com/114704675/198758767-f3a0d668-562b-47bc-b09a-058dc1f7151c.PNG">

- Gráfico de torta (certificados x juegos)

    - En este gráfico de torta podemos ver que certificados tienen los juegos. 

 ![WhatsApp Image 2022-10-28 at 9 15 56 PM](https://user-images.githubusercontent.com/114704675/198759668-f4161b5b-b453-4231-bd23-1d0ab05abc9a.jpeg)

- Gráfico (Categoria del juego y Rating):

     - En este gráfico podemos ver las distintas categorías de juego teniendo en cuenta la cantidad de juegos que tienen cierto rating(Por ejemplo podemos ver que casi 350 juegos de acción tienen un rating entre 7 y 8 puntos)
     - ![WhatsApp Image 2022-10-28 at 9 16 27 PM](https://user-images.githubusercontent.com/114704675/198770728-977cb35e-4a3c-4eee-a073-1ec0100faaaf.jpeg)


- Diagrama de dispersión (Rating y votos de los juegos):

    - En este diagrama de dispersión podemos ver el rating y la cantidad de votos que tuvo cada juego. 
    - Si llevamos el puntero arriba de cada uno de los puntos podemos ver cual es el juego. 
    - También tienen la opción de hacer zoom, para esto una vez que tienen el grafico, seleccione el recuadro y automáticamente van a poder hacer zoom. 


![WhatsApp Image 2022-10-28 at 10 12 21 PM](https://user-images.githubusercontent.com/114704675/198771375-ef382e37-dffe-49ff-8d21-c9b4eeeb8ae4.jpeg)

En este diagrama de dispersión podemos ver la relación entre los juegos mejor puntuados y la cantidad de votos. Por ejemplo el GTA V es el juego con más votos y está posicionado bastante alto en el rating

- Gráfico Word Cloud (Palabras mas usadas en los reviews):

     - En este gráfico Word Cloud pueden ver las palabras que más se usaron en los reviews que dejaron los usuarios de los juegos que fueron lanzados en los respectivos años. 

 1) 1960-1980: En el primer gráfico podemos ver las palabras que más usaron en los comentarios de los juegos que fueron lanzados entre los años 1960 y 1980

![wordcloud_year_output1960_1980](https://user-images.githubusercontent.com/114704675/198777519-a2987660-154a-4a36-a3fd-eb893995b216.png)

Si lo comparamos con el gráfico de barras de cantidad de juegos publicados (el gráfico 1) podemos ver que los juegos más vendidos en los entre los años 1960 y 1980 fueron de accion, Sci-Fi y Family. 

<img width="1087" alt="Capturar" src="https://user-images.githubusercontent.com/114704675/198758177-06f9e458-0450-4f8a-b37e-4f6ecc06f138.PNG">

Esto lo podemos ver reflejado en el word cloud porque algunas de las palabras más usadas en los reviews de los juegos lanzados en ese año fueron:
- Maze
- Control
- Space
- Arcade

 2) 1980-2000: En el segundo gráfico podemos ver las palabras que más usaron en los comentarios de los juegos que fueron lanzados entre los años 1980 y 2000.

![wordcloud_year_output1980_2000](https://user-images.githubusercontent.com/114704675/198778249-b9c75dd6-8ed0-4f93-9c8e-1f9fa1813c0c.png)

Si lo comparamos con el gráfico de barras de cantidad de juegos publicados (el gráfico 1) podemos ver que los juegos más vendidos en los entre los años 1980 y 2000 fueron de aventura y acción. Esto lo podemos ver reflejado en el word cloud porque algunas de las palabras más usadas en los reviews de los juegos lanzados en ese año fueron:
- World
- Evil
- Adventure
- Alien
- Fight

 3) 2000-2022: En el tercer gráfico podemos ver las palabras que más usaron en los comentarios de los juegos que fueron lanzados entre los años 2000 y 2022.
 
 ![wordcloud_year_output2000_2022](https://user-images.githubusercontent.com/114704675/198778658-1de515e4-a139-4551-b4ee-3455aca85760.png)

  Si lo comparamos con el gráfico de barras de cantidad de juegos publicados (el gráfico 1) podemos ver que los juegos más vendidos en los entre los años 2002 y 2022 fueron de aventura y acción. Esto lo podemos ver reflejado en el word cloud porque algunas de las palabras más usadas en los reviews de los juegos lanzados en ese año fueron:
- World
- Fight
- Battle
- Story
- Adventure

 


# Puntos importantes a tener en cuenta antes de ejecutar el código: 

     1) Al ejecutar los códigos en Visual Studio Code notamos que por momentos el código corría pero no se abría correctamente el gráfico, 
     por este motivo si esto llega a pasar por favor ejecutar el código en Google Colab, ya que aseguramos que de esta manera el código va 
     a funcionar correctamente. 

     2) En todos los gráficos excepto el “Word_cloud” tienen la opción de filtrar las variables que quieren ver, haciendo clic en los cuadrados de cada variable, por ejemplo:
     <img width="430" alt="Capturar" src="https://user-images.githubusercontent.com/114704675/198773045-a0923aa9-ef18-4591-82e1-f034270c25ba.PNG">

     3) En todos los gráficos menos en el pie chart y el Word Cloud pueden hacer zoom en los gráficos para ver las variables con mayor detalle, para esto tienen que:
          a) Ejecutar el código 
          b)Una vez que tienen el gráfico, seleccione el recuadro y automáticamente van a poder hacer zoom, por ejemplo: 
          
 ![WhatsApp Image 2022-10-28 at 9 24 34 PM](https://user-images.githubusercontent.com/114704675/198773896-154ec927-69dd-408d-960b-386f10dee9db.jpeg)

 ![WhatsApp Image 2022-10-28 at 9 25 00 PM](https://user-images.githubusercontent.com/114704675/198773980-e6f323ea-bec4-4278-a501-4e8bd3d2e0d0.jpeg)


