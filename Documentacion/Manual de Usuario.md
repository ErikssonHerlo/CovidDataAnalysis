# Coronavirus Data Analysis With Machine Learning 
## Manual de Usuario
##### Universidad de San Carlos de Guatemala
##### Facultad de Ingeniería 
##### Laboratorio de Organización de Lenguajes y Compiladores 2 Sección "A"
##### MSC. Luis Fernando Espino Barrios
##### Aux. Haroldo Pablo Arias Molina
##### Eriksson José Hernández López - 2927 19159 1415 - 201830459
##### Julio Fernando Ixcoy - 201530158 - 3133 88970 0901
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
---
## Introducción
El proyecto presentado, permite realizar distintos analisis de información basados de un origen de datos y en base a la parametrización de distintas variables configurables según el analísis, generar reportes estadisticos.

## Objetivos
#### Objetivo General
-  Aplicar los conocimientos sobre Ciencia de Datos y Machine Learning para la realización de una Aplicación de Predicciones Estadisticas completa y Funcional.

#### Objetivos Específicos
- Reforzar los conocimientos matemáticos sobre Regresiones Lineales y Predicciones Estadisticas
- Aplicar los conceptos de Ciencia de Datos, para el Analisis de Interpretación de Datos Estadísticos.

## Resumen
Durante la emergencia sanitaria provocada por el COVID-19, se ha observado un notable incremento en la aplicación de nuevas tecnologías al campo de la salud y la investigación. Desde la creación de todo tipo de dispositivos inteligentes destinados a detectar el más mínimo síntoma indicativo de contagio, hasta el diseño de nuevos patrones de investigación en la cura del nuevo coronavirus.

Sin duda, la IA (Inteligencia Artificial) ha estado presente en todas y cada una de las etapas de esta pandemia, e incluso en momentos previos a ella. En este sentido, se trató de una startup canadiense –BlueDot- que, gracias a un algoritmo basado en inteligencia artificial, logró predecirlo.

Mediante el procesamiento y análisis de noticias de todos los países del mundo, junto con información relacionada con rutas de vuelos comerciales y brotes de enfermedades, pudieron predecir, no solo la existencia de una enfermedad potencialmente pandémica, sino también el epicentro de la enfermedad. Así mismo, como su trayectoria más inmediata.

Así, la aplicación de la IA en esta pandemia global ha supuesto un antes y un después en el campo epidemiológico, ya que no solo ha permitido establecer un mayor control sobre la propagación del virus, sino que ha participado activamente en el diagnóstico, tratamiento. e investigación para poner fin a este brote lo antes posible.

En la actual pandemia que vive el mundo, el COVID-19 ha tenido grandes variaciones y tiende a ser engañoso debido a las nuevas olas derivadas del relajamiento social, las nuevas variantes y mutaciones que tenido el virus, asi tambien hoy en día existen varios factores que dificultan las comparaciones entre países, existen diferencias de una nación a otra, así como casos no detectados o reportados de la enfermedad, además existen diferentes tipos de pruebas, estrategias de detección, pero esto está limitado por las diferentes definiciones y formas de clasificación, como casos leves o asintomáticos que no son habitualmente contabilizados, porque no se reportan, por lo que la calidad de la atención también puede ser determinante, aun así es importante contar con modelos con los que sea posible predecir el comportamiento de la enfermedad de tal manera que se puedan tomar medidas preventivas en el a nivel poblacional para evitar el contagio, así como un mayor cuidado con las personas de alto riesgo, en dichos procesos de características y factores determinantes, diferentes características de los pacientes en los diferentes análisis realizados a lo largo del siguiente informe, edad, sexo, nacionalidad, entre otros.

A continuación se tratará de cómo ha evolucionado la pandemia del covid-19 desde el primer día que llegó a Guatemala y a algunos países de América, como Honduras, Costa Rica, Estados Unidos, e incluso una comparativa con países del otro lado del mundo como China. abordando preguntas sobre la tasa de mortalidad, número de personas infectadas por día, porcentaje de muertes según casos activos, porcentajes de vacunación, entre otros.

Todos los datos recopilados y mostrados han sido extraídos de las bases de datos públicas de cada país que rastrean esta información. Con esta información y utilizando el lenguaje de programación Python y su biblioteca Sckit-learn, es posible analizar y predecir los datos que se mostrarán a continuación.

## Descripción de la Aplicación
#### Funcionalidades
Esta aplicación tendrá como objetivo principal que un usuario pueda generar distintos análisis de información basados de un origen de datos (archivos con extensión CSV, JSON, XLSX, XLS).

#### Parametrización
Las variables a utilizar en cada reporte, seran utilizadas por medio de un proceso de parametrización, en el que por medio de un solo archivo de entrada, se pueden generar distintos reportes, gracias a un proceso de filtrado de parametros, el cual se describe en cada uno de los reportes.
#### Reportes a Generar
En cada uno de los Reportes que la Aplicación puede generar, se describen los datos que espera recibir cada uno de los Reportes.
##### 1. Tendencia de la infección por Covid-19 en un País.
   - Columna con Paises
   - Columna con infectados por dia *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del pais a filtrar

##### 2. Prediccion de la infección por Covid-19 en un País.
   - Columna con Paises
   - Columna con infectados por dia *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del pais a filtrar
   - Dia a Predecir *(numero entero)*

##### 3. Indice de Progresión de la pandemia.
   - Cantidad de Población Total
   - Cantidad de Población Infectada
   - Columna con las fechas *(formato dd/mm/yyyy)*

##### 4. Prediccion de Contagios por Covid en un Departamento
   - Columna con Departamentos
   - Columna con infectados por dia *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del departamento a filtrar
   - Dia a Predecir *(numero entero)*

##### 5. Prediccion de la infección por Covid-19 en un País.
   - Columna con Paises
   - Columna con Muertes por dia *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del pais a filtrar
   - Dia a Predecir *(numero entero)*

##### 6. Análisis del número de muertes por coronavirus en un País.
   - Columna con Paises
   - Columna con Muertes por dia *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del pais a filtrar

##### 7. Tendencia del número de infectados por día de un País.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Infectados por dia *(cantidad entera)*
   - Nombre del pais a filtrar
   - Dia a Predecir *(numero entero)*

##### 8. Prediccion de la infección por Covid-19 en un País.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Infectados por dia *(cantidad entera)*
   - Nombre del pais a filtrar
   - Año a predecir *(numero entero)*

##### 9. Tendencia de la vacunación de en un País.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Vacunados por dia *(cantidad entera)*
   - Nombre del pais a filtrar

##### 10. Ánalisis Comparativo de Vacunaciópn entre 2 paises.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Vacunados por dia *(cantidad entera)*
   - Nombre del pais a filtrar
   - Nombre del Segundo Pais a comparar

##### 11. Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo
   - Columna con Paises
   - Nombre del pais a filtrar
   - Columna con Registro de Infectados Hombres *(cantidad entera)*
   - Columna con Registro de Infectados Mujeres *(cantidad entera)*
   - Estructura recomendada para obtener la informacion:
        | Pais | Hombres Infectados | Mujeres Infectadas |
        | ------ | ------ | ------ |
        | Guatemala | 160000 | 120000|    

##### 12. Ánalisis Comparativo entres 2 o más paises o continentes.
   - Columna con Paises / Continentes
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Infectados por dia *(cantidad entera)*
   - Nombre del pais a filtrar
   - Nombre del Segundo Pais a comparar

##### 13. Muertes promedio por casos confirmados y edad de covid 19 en un País.
   - Columna con Paises
   - Columna con Muertes por dia *(cantidad entera)*
   - Columna con Edades *(cantidad entera)*
   - Nombre del pais a filtrar

##### 14. Muertes por Covid 19 según regiones de un país.
   - Columna con Paises 
   - Columna con Regiones
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Muertes por dia *(cantidad entera)*
   - Nombre del pais a filtrar
   - Nombre de la region a filtrar
   - Estructura recomendada para obtener la informacion:
        | Pais | Region | Fecha | Muertes |
        | ------ | ------ | ------ | ------ |
        | Guatemala | Occidente | 03/01/2022 | 600|  

##### 15. Tendencia de casos confirmados de Coronavirus en un departamento de un País.
   - Columna con Paises 
   - Columna con Departamentos
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Infectados por dia *(cantidad entera)*
   - Nombre del pais a filtrar
   - Nombre del departamento a filtrar
   - Estructura recomendada para obtener la informacion:
        | Pais | Departamento | Fecha | Infectados |
        | ------ | ------ | ------ | ------ |
        | Guatemala | Quetzaltenango | 03/01/2022 | 721|  

##### 16. Porcentaje de muertes frente al total de casos en un país, región o continente.
   - Columna con Paises / Regiones / Continentes
   - Columna con el Total de Infectados *(cantidad entera)*
   - Nombre del pais / región / continente a filtrar
   - Columna con el Total de Muertes *(cantidad entera)*
   - Estructura recomendada para obtener la informacion:
        | Pais | Casos | Fallecimientos | 
        | ------ | ------ | ------ | 
        | Guatemala | 150000 | 70000 |   

##### 17. Tasa de comportamiento de casos activos en relación al número de muertes en un continente.
   - Columna con Continentes
   - Columna con el Total de Infectados *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del continente a filtrar
   - Columna con el Total de Muertes *(cantidad entera)*
   - Estructura recomendada para obtener la informacion:
        | Continente | Casos Activos | Fallecimientos | 
        | ------ | ------ | ------ | 
        | América | 150000 | 70000 |   

##### 18. Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País.
   - Columna con Paises
   - Columna con Departamentos
   - Columna con Municipios
   - Columna con Infectados por dia *(cantidad entera)*
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del Pais a filtrar
   - Nombre del Departamento a filtrar
   - Nombre del Continente a filtrar
   - Estructura recomendada para obtener la informacion:
        | Pais | Departamento | Municipio | Fecha | Infectados | 
        | ------ | ------ | ------ | ------ | ------ | 
        | Guatemala | Quetzaltenango | Quetzaltenango | 14/09/2021 | 700 |   

##### 19. Predicción de muertes en el último día del primer año de infecciones en un país.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del Pais a filtrar
   - Columna con Muertes por dia *(cantidad entera)*

##### 20. Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del Pais a filtrar
   - Columna con Infectados por dia *(cantidad entera)*
   - Columna con Muertes por dia *(cantidad entera)*

##### 21. Predicciones de casos y muertes en todo el mundo - Neural Network MLPRegressor
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Infectados por dia *(cantidad entera)*
   - Columna con Muertes por dia *(cantidad entera)*

##### 22. Tasa de mortalidad por coronavirus (COVID-19) en un país.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del Pais a filtrar
   - Columna con Infectados por dia *(cantidad entera)*
   - Columna con Muertes por dia *(cantidad entera)*

##### 23. Factores de muerte por COVID-19 en un país.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del Pais a filtrar
   - Columna con Factores de Muerte por dia *(cantidad entera)*

##### 24. Comparación entre el número de casos detectados y el número de pruebas de un país.
   - Columna con Paises
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Nombre del Pais a filtrar
   - Columna con Infectados por dia *(cantidad entera)*
   - Columna con Pruebas Realizadas por dia *(cantidad entera)*

##### 25. Predicción de casos confirmados por día
   - Columna con las fechas *(formato dd/mm/yyyy)*
   - Columna con Infectados por dia *(cantidad entera)*
   - Columna con Pruebas Realizadas por dia *(cantidad entera)*


## Flujo de la Aplicación
#### Carga de Archivos
Para utilizar la aplicación es necesario cargar un archivo, con un formato (csv, json, xlsx, xls).

![Carga del Archivo](https://github.com/ErikssonHerlo/CovidDataAnalysis/blob/main/Documentacion/resources/2_UploadFile.png)

#### Elección del Reporte
El usuario debe elegir el tipo de reporte que desea generar, entre las distintas opciones
![Eleccion del Reporte](https://github.com/ErikssonHerlo/CovidDataAnalysis/blob/main/Documentacion/resources/3_ChooseReport.png)

#### Visualización de las Columnas
El usuario podrá visualizar las Columnas que contiene el Archivo, desplegadas en una lista
![Visualizacion de las Columnas](https://github.com/ErikssonHerlo/CovidDataAnalysis/blob/main/Documentacion/resources/4_PreviewColumns.png)

#### Parametrización
El usuario debe elegir las columnas a utilizar, en base al tipo de reporte elegido. Dicha descripción de los parametros , por reporte la puede encontrar [aquí.](https://github.com/ErikssonHerlo/CovidDataAnalysis/blob/main/Documentacion/Manual%20de%20Usuario.md#reportes-a-generar)
![Parametrizacion](https://github.com/ErikssonHerlo/CovidDataAnalysis/blob/main/Documentacion/resources/5_Parameterization.png)

#### Reporte Generado
El usuario visualizará el Reporte Generado
![ReporteGenerado](https://github.com/ErikssonHerlo/CovidDataAnalysis/blob/main/Documentacion/resources/6_GeneratedReport.png)

#### Exportar el Reporte
El usuario tendrá la opción de Exportar el Reporte Generado en un formato PDF

#### Acceso al Proyecto
- Para acceder a la Aplicación de Predicciones debe ingresar al siguiente enlace:   [ML con Sklearn](https://ml-con-sklearn-e7gju.ondigitalocean.app/) 

