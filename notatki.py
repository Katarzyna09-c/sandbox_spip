import psycopg2 as ps
from dane import users_list

db_params = ps.connect(
    database='postgres',
    user='postgres',
    password='psip2023',
    host='localhost',
    port=5432
)

cursor=db_params.cursor()



#engine = sqlalchemy.create_engine(db_params)
#connection = engine.connect()
#sql_query_1 = sqlalchemy.text ("INSERT INTO public.my_table( name) VALUES('kepa');")
#sql_query_1= sqlalchemy.text ("select * from public.my_table;")
#user = input('podaj nazwe zawodnika do usuniecia')
#sql_query_1= sqlalchemy.text (f"DELETE FROM public.my_table WHERE name='{user}';")
#kogo_zamienic = input('podaj kogo zmienic')
#na_kogo = input('podaj na kogo zamienic')
#sql_query_1= sqlalchemy.text (f"UPDATE public.my_table SET name={'na_kogo'} WHERE name={'kogo_zamienic'};")

def dodaj_uzytkownika(user:str):
    for nick in users_list:
        if user == nick['nick']:
            sql_query_1 = f"INSERT INTO public.lab(city, name, nick, posts) VALUES ('{nick['city']}', '{nick['name']}', '{nick['nick']}', '{nick['posts']}');"
            cursor.execute(sql_query_1)
            db_params.commit()

dodaj_uzytkownika(input('dodaj teraz'))

#def usun_uzytkownika(user:str):
 #   sql_query_1 = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name='{user}';")
  #  connection.execute(sql_query_1)
   # connection.commit()


#def aktualizuj_uzytkownika(user_1:str,user_2:str):
 #   sql_query_1 = sqlalchemy.text(f"UPDATE public.my_table SET name='{user_1}' WHERE name='{user_2}';")
  #  connection.execute(sql_query_1)
   # connection.commit()
#aktualizuj_uzytkownika(
 #   user_1=input('na kogo zamienic'),
  #  user_2= input('kogo zamienic'))


#connection.execute(sql_query_1)
#connection.commit()