# <h1 align=center> ** Proyecto Individual Nro.1 - DATA05 **

# <h1 align=center>**`Data Engineering`*</h1> **

<h1 align=center>María Belén Sendot</h1>
  
<p align="center">
<img src=https://user-images.githubusercontent.com/111015749/206626200-1577e4a8-be9c-4b91-8cce-d8ad19534399.png height=300>
</p>
  
¡Bienvenidos a mi primer proyecto individual de la etapa de labs! 

<hr>  

## **Introducción**

En este primer trabajo tuve que cumplir el rol de una ***Data Engineer***, realizando actividades como la extracción de datos, su modelado, las transformaciones necesarias para su normalizacion o ETL, el montaje en una Api y la realización de una Imagen de Docker.

<p align="center">
<img src = 'https://user-images.githubusercontent.com/111015749/206627044-8b1d9613-0800-4597-869e-1baad4b32172.png' height=250><p>
  

## **ETL**

El proyecto comienza con la ingesta de datos desde diversas fuentes, ya sean archivos csv o json. Para la normalizacion y limpieza de los datos elimine duplicados, corregi los valores nulos con 'sin dato' o reemplazandolos por la mediana en el caso de que fueran de tipo numerico, e inserte los datos en un dataset unificado agregando una columna con la plataforma correspondiente a cada fila.

  ![image](https://user-images.githubusercontent.com/111015749/206627755-5801bf50-9267-45b9-b1db-f5bd7658c1ef.png)
  
  ![image](https://user-images.githubusercontent.com/111015749/206628298-7e500bea-d084-455c-84ce-0bb92a7d879a.png)

  ![image](https://user-images.githubusercontent.com/111015749/206628559-5bdc360c-70a4-4c34-b47e-eaebd3d2acec.png)


Tambien tuve que indexar el nuevo dataset con números únicos para cada fila y renombrar y ordenar las columnas para que fuera mas cómodo trabajar.

  ![image](https://user-images.githubusercontent.com/111015749/206628012-8afe8881-32c0-4aec-b764-2099b75a954d.png)

  ![image](https://user-images.githubusercontent.com/111015749/206628084-6b3ddf1e-6dcf-4a19-9487-885c9c8ff59c.png)


Aplicando la función Split separe el dato numérico de la unidad para disponibilizar los datos para resolver las querys finales. Así mismo tambien me encargue de normalizar los tipos de datos, las mayúsculas y minúsculas. 

 ![image](https://user-images.githubusercontent.com/111015749/206628727-4a6149cf-d294-4a4a-b445-71ae00d1d6d3.png)

Finalmente en esta parte del proceso ETL realicé 3 archivos Csv, de genero, de actores y uno gral para después podes llamarlos para la realización de las funciones.

 ![image](https://user-images.githubusercontent.com/111015749/206628816-dcf4e168-2ff9-4923-a6b8-28c2ed2f2818.png)

  ![image](https://user-images.githubusercontent.com/111015749/206628871-9861ee0d-e005-40fb-af4e-7bdadb82cc63.png)

  ![image](https://user-images.githubusercontent.com/111015749/206628912-64127be2-6404-4935-9fba-bd7db77b874a.png)

  
Posteriormente tuve que disponibilizar los datos limpios para su consulta a través de una API. Esta API fue construida en un entorno virtual dockerizado.

Las consultas que tuvimos que realizar a los datasets son las siguientes:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

Construi el archivo main.py con las querys necesarias para obtener dichos resultados e inicialice la API con el comando:  *python -m uvicorn main:app --reload*
  
  ![image](https://user-images.githubusercontent.com/111015749/206629327-9b8fb46d-94cf-4fd8-8b0c-4062a0c84ee4.png)

  ![image](https://user-images.githubusercontent.com/111015749/206629620-8a1dd6bc-2bdc-4b77-857f-d4d66ad1e189.png)

 **API** en funcionamiento:
 
  ![image](https://user-images.githubusercontent.com/111015749/206629973-6b03af7f-ac74-4ab6-aaa0-5c08723db221.png)

Finalmente levante una imagen de ***DOCKER*** de la API con los siguientes comandos en otra terminal del Visual Code:
  
  *docker build -t first_app:latest .*
  
  *docker run -p 8080:80  first_app:latest*
  
  ![image](https://user-images.githubusercontent.com/111015749/206630321-90b677a4-2d65-4df3-ad00-23c234e39d89.png)

  ![image](https://user-images.githubusercontent.com/111015749/206630371-c562bd71-a341-4eb4-95b6-877e6e337512.png)

  ![image](https://user-images.githubusercontent.com/111015749/206630412-e2dba949-c36b-4e69-bbca-af6921c12529.png)
  
  ![image](https://user-images.githubusercontent.com/111015749/206630458-3e3c886f-6c47-4668-ac90-2f59276f1a19.png)

  ![image](https://user-images.githubusercontent.com/111015749/206630556-9b479310-20bb-495e-990c-5c99eba5f94b.png)

  ![image](https://user-images.githubusercontent.com/111015749/206630620-35fdfa2c-8133-49dd-9b4a-cf38c1231f0d.png)

  ![image](https://user-images.githubusercontent.com/111015749/206630669-f2871f4f-99a0-46d8-b9da-b5b9c3657c28.png)



## **Video demostrativo**

Finalmente realice un video demostrativo ejecutando las tareas solicitadas de no mas de 5 min. incluyendo la presentacion del proyecto, el paso a paso y el funcionamiento del codigo.
