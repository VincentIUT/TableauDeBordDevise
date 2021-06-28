from datetime import date, timedelta
from pprint import pprint

import requests


# fonction qui permet de récupérer les devises (liste de devises) et les jours
def get_rates(currencies, days=30):
    # on récupère la date d'aujourd'hui
    end_date = date.today()
    # je fabrique la date de début en utilisant le delta = je recule de 30 jours
    start_date = end_date - timedelta(days=days)

    # je fais une requete get à l'api
    symbols = ','.join(currencies)
    requete = f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}"
    r = requests.get(requete)
    if not r and not r.json():
        return False, False

    # je récupère le dictionnaire qui contient les données
    api_rates = r.json().get("rates")

    # je crée mon dictionnaire pour récupérer les valeurs (devises et leurs valeurs)
    all_rates = {currency: [] for currency in currencies}

    # je récupère les clés de api_rates = les jours
    all_days = sorted(api_rates.keys())

    # je boucle sur les jours que j'ai récupérés et j'ajoute chaque clé-valeur à mon dico
    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    return all_days, all_rates


# je retourne 2 choses : liste des devises et listes des jours
if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])
