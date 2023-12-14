import random
import sqlalchemy
import os
import sqlalchemy.orm
from dotenv import load_dotenv
from geoalchemy2 import Geometry
from faker import Faker

load_dotenv()

# Tworze plik o nazwie .env
db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    port=os.getenv("POSTGRES_PORT"),
)

engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'aaaaa'

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)  # serial
    name = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    location = sqlalchemy.Column('geom', Geometry(geometry_type='POINT', srid=4326, nullable=True))


Base.metadata.create_all(engine)

### Create

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

lista_userow: list = []
fake = Faker()



for item in range(10_000):
    lista_userow.append(
        User(
            name=fake.name(),
            location=f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
        ))



#session.add_all(lista_userow)
#session.commit()

## Read / Select
#print(users_from_db)


users_from_db = session.query(User).all()
for user in users_from_db:
    if user.name =='Mariah Carey':
        user.query.filter_by(name='Mariah Carey')

    print(user.name)

session.commit()

    #print(user.name)






 #   print(user.name)

#user_from_db = session.query(User).filter(User.name=='Janek')




session.flush()
connection.close()
engine.dispose()
