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
              f'4: Modyfiikuj uzytkonika'
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



def update_users(users_list: list[dict, dict]) -> None:
    nick_of_users = input('podaj nick uzytkownika do modyfikacj')
    print(nick_of_users)
    for users in users_list:
        if users['nick'] == nick_of_users:
            print('Znaleziono!!!')
            users['name'] = input('podaj nowe imie')
            users['nick'] = input('podaj nowa ksywe!!')
            users['posts'] = int(input('podaj liczbe postow: '))
