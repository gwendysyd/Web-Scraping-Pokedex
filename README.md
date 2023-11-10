# PRA1: Web Scraping

<p align="center">
  <img src="https://cdn.pixabay.com/photo/2016/07/23/13/18/pokemon-1536847_1280.png" width="200" height="200">
</p>

## Descripción

La aplicación consiste en técnicas de web scraping para extraer un dataset sobre diferentes Pokémon y sus características. Los datos se han extraído a partir de la web https://www.serebii.net/pokedex-swsh. Esta aplicación se corresponde con la Práctica 1 de la asignatura Tipología y Ciclo de Vida de los Datos del Máster en Ciencia de Datos de la UOC.

## Miembros del equipo

Mireia Gomez Mengíbar y Gwendolin Herrera Carballido.

## Ficheros

* **requirements.txt**: Contiene las librerías que son necesarias para el correcto funcionamiento del programa.
* **main.py**: Ejecutable para iniciarl el proceso de Scraping.
* **src/scraper.py**: Contiene la clase PokemonScraper con la implementación del proceso para obtener datos de la web [serebii pokedex](https://www.serebii.net/pokedex)

## Instrucciones de uso

### Environment
Asegúrate de que tu environment cuenta con las librerías indicadas en el archivo `requirements.txt`

### Clonar el repositorio
Desde la terminal, navega hasta la carpeta en la que se desea clonar el repositorio

`cd la_carpeta_elegida`

después clona el repositorio

 `git clone https://github.com/gwendysyd/Web-Scraping-Pokedex.git`

### Ejecutar la aplicación
Navega hasta el directorio principal

`cd  Web-Scraping-Pokedex-main`

y ejecuta el archivo main.py
 
`python main.py`

El csv final con el resultado se guardará en la carpeta `output`.

## DOI del dataset generado
https://doi.org/10.5281/zenodo.10106105 

## Recursos

* Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
