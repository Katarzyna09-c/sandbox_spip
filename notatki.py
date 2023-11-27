from bs4 import BeautifulSoup
import requests
import folium
import re

# pobranie strony internetowej
nazwa_miejscowosci = ['Zamość']
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
#for item in nazwa_miejscowosci:
  #  print(get_coordinates_of(item))

# zwrócić mape z pinezką odnoszącą się do wskazanego na podstawie nazwy użytkownika podanej z klawiatury


user ={"city":'Zamość',"name":"Kasia" , "nick":"katarzyna","posts":1}
# zwróci mapę z wszystkimi użytkownikami z danej listy (znajomymi)
### Rysowanie mapy
def get_map_of(users: list) -> None:
    map = folium.Map(
        location=[52.3, 21.0],    #gdzie mapa ma byc wycentrowana
        tiles="OpenStreetMap",
        zoom_start=7
    )

    for user in users:
        folium.Marker(
            location=get_coordinates_of(city=user['city']),
            popup=f'Użytkownik: {user["name"]} \n'
                  f'liczba postów {user["posts"]}'
        ).add_to(map)
    map.save(f'mapka.html')


from dane import users_list
get_map_of(users_list)

city = get_coordinates_of(city='Zamość')