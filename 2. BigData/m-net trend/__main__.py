from config import CONFIG
import collect

if __name__ == '__main__':

    # collect.fetch_data(CONFIG['chart'], CONFIG['common_fetches'])
    collect.fetch_data(**CONFIG['COMMON'], **CONFIG['CHART'])