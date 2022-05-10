import psycopg2
from config import config

ingredients = (
    (1, 'tomato', True),
    (2, 'cheese', False),
    (3, 'chicken', False),
    (4, 'ham', False),
    (5, 'potato', True),
    (6, 'olives', True),
    (7, 'mashrooms', True),
    (8, 'burger sauce', False),
    (9, 'grilled vegetables', True),
    (10, 'pork', False),
    (11, 'ketchup', True),
    (12, 'bread', True),
    (14, 'pumkin', True),
    (15, 'chicken', False),
)

food = (
    (100, 'pizza', 'MainDishes'),
    (101, 'burger','MainDishes'),
    (102, 'chicken with vegetables', 'MainDishes'),
    (103, 'chicken soup', 'Soups'),
    (104, 'pumkin soup', 'Soups'),
)

food_ingredients= (
    (300, 100, 11),
    (301, 100, 7),
    (302, 100, 4),
    (303, 100, 6),
    (304, 100, 2),
    (305, 101, 8),
    (306, 100, 10),
    (307, 100, 11),
    (308, 100, 12),
)

drinks = (
    (200, 'hot chocolate', 'HotDrinks'),
    (201, 'coffe','HotDrinks'),
    (202, 'apple juice', 'Juices'),
    (203, 'tequila', 'Alchocol'),
    (204, 'orange juice', 'Juices'),
)

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        
        create_tables(cur, conn)
        insert_data(cur,conn)

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def create_tables(cur, conn):
    cur.execute("CREATE TYPE FoodType AS ENUM ('MainDishes', 'Appetizers', 'HouseSpecials','Soups', 'Salads', 'FastingDishes');")
    cur.execute("CREATE TYPE DrinkType AS ENUM ('Alchocol', 'Carbonated', 'Juices','HotDrinks');")
    cur.execute("CREATE TABLE IF NOT EXISTS food(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, food_type FoodType)")
    cur.execute("CREATE TABLE IF NOT EXISTS ingredient(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, fasting BOOLEAN)")
    cur.execute("CREATE TABLE IF NOT EXISTS food_ingredient(id SERIAL PRIMARY KEY,food_id integer REFERENCES food (id), ingredient_id integer REFERENCES ingredient (id) )")
    cur.execute("CREATE TABLE IF NOT EXISTS drink(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, drink_type DrinkType)")
    conn.commit()

def insert_data(cur, conn):
    query_food = "INSERT INTO food (id, name, food_type) VALUES (%s, %s, %s)"
    cur.executemany(query_food, food)
    conn.commit()
        
    query_ingredient= "INSERT INTO ingredient (id, name, fasting) VALUES (%s, %s, %s)"
    cur.executemany(query_ingredient, ingredients)
    conn.commit()

    query_drink = "INSERT INTO drink (id, name, drink_type) VALUES (%s, %s, %s)"
    cur.executemany(query_drink, drinks)
    conn.commit()

    query_food_ingredient = "INSERT INTO food_ingredient (id, food_id, ingredient_id) VALUES (%s, %s, %s)"
    cur.executemany(query_food_ingredient, food_ingredients)
    conn.commit()

if __name__ == '__main__':
    connect()