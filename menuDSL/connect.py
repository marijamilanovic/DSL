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
    (16, 'pumpkin', True)
)

food = (
    (100, 'pizza', 'MainDishes', 680, 'pizza.jpg'),
    (101, 'burger','MainDishes', 700, 'burger.jpg'),
    (102, 'chicken with vegetables', 'MainDishes', 690, 'chicken with vegetables.jpg'),
    (103, 'chicken soup', 'Soups', 350, 'chicken soup.jpg'),
    (104, 'pumpkin soup', 'Soups', 370, 'pumpkin soup.jpg'),
)

food_ingredients= (
    (300, 100, 11),
    (301, 100, 7),
    (302, 100, 4),
    (303, 100, 6),
    (304, 100, 2),
    (305, 101, 8),
    (306, 101, 10),
    (307, 101, 11),
    (308, 101, 12),
    (309, 104, 16),
)

drinks = (
    (200, 'hot chocolate', 'HotDrinks', 210),
    (201, 'coffe','HotDrinks', 150),
    (202, 'apple juice', 'Juices', 190),
    (203, 'tequila', 'Alchocol', 230),
    (204, 'orange juice', 'Juices', 190),
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
    cur.execute("CREATE TABLE IF NOT EXISTS food(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, food_type FoodType, price INTEGER NOT NULL, image VARCHAR(255))")
    cur.execute("CREATE TABLE IF NOT EXISTS ingredient(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, fasting BOOLEAN)")
    cur.execute("CREATE TABLE IF NOT EXISTS food_ingredient(id SERIAL PRIMARY KEY,food_id integer REFERENCES food (id), ingredient_id integer REFERENCES ingredient (id) )")
    cur.execute("CREATE TABLE IF NOT EXISTS drink(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, drink_type DrinkType, price INTEGER NOT NULL)")
    conn.commit()

def insert_data(cur, conn):
    query_food = "INSERT INTO food (id, name, food_type, price, image) VALUES (%s, %s, %s, %s, %s)"
    cur.executemany(query_food, food)
    conn.commit()
        
    query_ingredient= "INSERT INTO ingredient (id, name, fasting) VALUES (%s, %s, %s)"
    cur.executemany(query_ingredient, ingredients)
    conn.commit()

    query_drink = "INSERT INTO drink (id, name, drink_type, price) VALUES (%s, %s, %s, %s)"
    cur.executemany(query_drink, drinks)
    conn.commit()

    query_food_ingredient = "INSERT INTO food_ingredient (id, food_id, ingredient_id) VALUES (%s, %s, %s)"
    cur.executemany(query_food_ingredient, food_ingredients)
    conn.commit()

if __name__ == '__main__':
    connect()