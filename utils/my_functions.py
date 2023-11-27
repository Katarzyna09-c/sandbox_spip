def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imie ?')
    posts = input('podaj liczbe postow ?')
    users_list.append({'name': name, 'posts': posts})


def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """

    tap_list = []
    name = input('podaj imie uzytkownika do usuniecia')
    for user in users_list:
        if user['name'] == name:
            tap_list.append(user)
    print('Znaleziono uzytkownikow :')
    print('0: Usun wszystkich zmienionych uzytkownikow')
    for numerek, user_to_be_removed in enumerate(tap_list):
        print(f'{numerek + 1}: {user_to_be_removed}')
    numer = int(input(f'Wybierz uzytkownika do usuniecia'))
    if numer == 0:
        for user in tap_list:
            users_list.remove(user)
    else:
        users_list.remove(tap_list[numer - 1])


def show_users_from(users_list: list) -> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]}')


def gui(users_list) -> None:
    while True:
        print(f'Menu: \n'
              f'0: Zakoncz program \n'
              f'1: Wyswietl uzytkownikow \n'
              f'2: Podaj uzytkownika \n'
              f'3: Usun uzytkownika \n'
              f'4: Modyfiikuj uzytkonika\n'
              f'5: Wygeneruj mapę z użytkownikiem\n'
              f'6: Wygeneruj mapę z użytkownikami'
              )

        menu_option = input('Podaj funkcje do wywołania')
        print(f'Wybrano funkcje {menu_option}')

        match menu_option:
            case '0':
                print('Koncze prace')
                break
            case '1':
                print('Wysliwetlam nazwe uzytkownika')
                show_users_from(users_list)
            case '2':
                print('Dodaje uzytkownika')
                add_user_to(users_list)
            case '3':
                print('Usuniecie uzytkownika')
                remove_user_from(users_list)
            case '4':
                print('Modyfikuje uzytkownika')
                update_users(users_list)
            case '5':
                print('Rysuj mapę z użytkownikiem')
                user = input('podaj nazwe użytkownika do modyfikacji')
                for user in users_list:
                    if item['name'] ==
            case '6':
                print('Rysuje mape z wszystkimi użytkownikami')
                pass
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
def get_map_of(users: list[dict: list]) -> None:
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

def update_users(users_list: list[dict, dict]) -> None:
    nick_of_users = input('podaj nick uzytkownika do modyfikacj')
    print(nick_of_users)
    for users in users_list:
        if users['nick'] == nick_of_users:
            print('Znaleziono!!!')
            users['name'] = input('podaj nowe imie')
            users['nick'] = input('podaj nowa ksywe!!')
            users['posts'] = int(input('podaj liczbe postow: '))
