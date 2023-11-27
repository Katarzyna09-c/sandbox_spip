from bs4 import BeautifulSoup

import requests
import re
# pobranie strony internetowej
nazwa_miejscowosci = 'Gdańsk'
def get_coordinates_of(city:str)->list[float,float]:

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text,'html.parser')

    # pobranie wspolrzednych z tresci strony intrnetowej

    response_html_latitude = response_html.select('.latitude')[1].text # . poniewaz class
    response_html_latitude= float(response_html_latitude.replace(',','.'))
    response_html_longitude = response_html.select('.longitude')[1].text # . poniewaz class
    response_html_longitude= float(response_html_longitude.replace(',','.'))


    return[response_html_latitude, response_html_longitude]
    # print(response_html_latitude[23:-7])

    #latitude = re.sub( "(\<).*?(\>)", repl='', string=response_html_latitude, count=0,flags=0)
for item in nazwa_miejscowosci
print(get_coordinates_of(nazwa_miejscowosci)

