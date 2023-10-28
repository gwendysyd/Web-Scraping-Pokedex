import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

class PokemonScraper():
    def __init__(self, url="https://www.serebii.net/pokedex-swsh"):
        self.url = url
        self.base_url = "https://www.serebii.net"
        self.pokemon_list = []

    def scrape_pokemon_data(self):
        print("Scraping has started...")
        page_data = requests.get(self.url)
        soup = BeautifulSoup(page_data.content, 'html.parser')
        table_of_pokedex_selects = soup.find_all("table")[1]
        select_elements = table_of_pokedex_selects.find_all('select', attrs={'name': 'SelectURL'})

        for select_element in select_elements:
            for option in select_element.find_all('option')[1:]:
                number = option.get_text().split()[-2]
                name = option.get_text().split()[-1]
                url = option['value']

                print(number, name)
                # Obtener numero, nombre y url de cada Pokemon
                pokemon_dict = {
                    'Number': number,
                    'Name': name,
                    'URL': self.base_url + url
                }

                # Extraer caracteristicas individuales de cada Pokemon
                poke_data = requests.get(self.base_url + url)
                poke_soup = BeautifulSoup(poke_data.content, 'html.parser')
                # Obtener Tipo de Pokemon
                td_cen = poke_soup.find('td', class_='cen')
                img_elements = td_cen.find_all('img')
                types = [img['src'].split('/')[-1].split('.')[0] for img in img_elements if 'src' in img.attrs]
                pokemon_dict['Type'] = types

                # Obtener Clasificacion, Altura en metros, Peso en kilos, y Ratio de captura
                height_m = poke_soup.find('td', class_='foo', text='Height')
                info_table = height_m.parent.parent #busco la tabla con toda la información
                for index, tr in enumerate(info_table):
                    if index == 7: #me quedo con la que contiene los datos a buscar
                        columns = tr.find_all('td', class_='fooinfo')
                        classification = columns[0].get_text()
                        height_m = columns[1].get_text().split('\n')[1].strip().replace("m", "")
                        weight_kg = columns[2].get_text().split('\n')[1].strip().replace("kg", "")
                        capture_rate = columns[3].get_text()

                pokemon_dict['Classification'] = classification
                pokemon_dict['Height_m'] = height_m
                pokemon_dict['Weight_kg'] = weight_kg
                pokemon_dict['Capture_rate'] = capture_rate

                # Obtener Stats: HP, Ataque, Defensa, Especial, Velocidad
                stats_table = poke_soup.find('td', class_='fooevo', text='HP')

                if stats_table:
                    iterator = stats_table.find_next('td', class_='fooinfo').find_next('td', class_='fooinfo')
                    hp_value = iterator.get_text()
                    iterator = iterator.find_next('td', class_='fooinfo')
                    attack_value = iterator.get_text()
                    iterator = iterator.find_next('td', class_='fooinfo')
                    defense_value = iterator.get_text()
                    iterator = iterator.find_next('td', class_='fooinfo')
                    special_attack_value = iterator.get_text()
                    iterator = iterator.find_next('td', class_='fooinfo')
                    special_defense_value = iterator.get_text()
                    iterator = iterator.find_next('td', class_='fooinfo')
                    speed_value = iterator.get_text()

                pokemon_dict['HP'] = hp_value
                pokemon_dict['Attack'] = attack_value
                pokemon_dict['Defense'] = defense_value
                pokemon_dict['Sp. attack'] = special_attack_value
                pokemon_dict['Sp. defense'] = special_defense_value
                pokemon_dict['Speed'] = speed_value

                self.pokemon_list.append(pokemon_dict)
            
    def export_to_csv(self, filename="output/pokemon_data.csv"):
        if not self.pokemon_list:
            print("No data to export.")
            return

        # Crear df a partir de pokemon_list
        df = pd.DataFrame(self.pokemon_list)

        # Crear directorio si no existe
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Exportar a formato csv
        df.to_csv(filename, index=False)
        print(f"Data exported to {filename}")
