import requests
import pandas as pd
from bs4 import BeautifulSoup


def getData():
    """
    get data from a rentberry for 3 cities : BERLIN, KOLN and MUNCHEN
    

    return : dataframe with the number total of flats per city and the 
    number total of flats per city with air conditioning
    """
    URL_MAIN = 'https://rentberry.com/de/apartments/s/'
    URL_LASTPART = ['/air-conditioning','']
    IND_AIRCON = ['with A/C', 'without A/C']

    CITIES = ['Munchen', 'Berlin', 'Koln']

    data = {"City" : [],
            "Air-conditioning" : [],
            "Number": []}

    for city in sorted(CITIES):
        for url_lastpart in zip(URL_LASTPART,IND_AIRCON):
            url = f"{URL_MAIN}{city}-germany{url_lastpart[0]}"
            # print("voyons ; ", url)

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
            r = requests.get(url)
            print(r.status_code)

            soup = BeautifulSoup (r.content, 'html.parser')

            c = soup.find(class_='font-s-b ng-star-inserted')
            
            print('For the city ', city,'With', url_lastpart[0], ' : ',c.text.replace(",",""))

            data.setdefault("City").append(city)
            data.setdefault("Air-conditioning").append(url_lastpart[1])
            data.setdefault("Number").append(int(c.text.replace(",","").replace(u'\xa0', u'')))

            print(data)
            df = pd.DataFrame(data)

    return df

getData()