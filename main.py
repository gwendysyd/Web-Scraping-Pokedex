from src.scraper import PokemonScraper

scraper = PokemonScraper();
scraper.scrape_pokemon_data()
scraper.export_to_csv("output/pokemon_dataset.csv")
