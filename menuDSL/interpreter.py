from os import mkdir
from os.path import join, dirname, exists
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export_to_file, model_export
from io import StringIO
import psycopg2
from config import config

def get_meta_model():
    current_dir = dirname(__file__)
    my_metamodel = metamodel_from_file(join(current_dir + '\menu', 'menu.tx'), debug=False)
    return my_metamodel


def get_model(file_name):
    my_metamodel = get_meta_model()
    model = my_metamodel.model_from_file(file_name)
    return model


def export_meta_model():
    my_metamodel = get_meta_model()
    metamodel_export(my_metamodel, join(dirname(__file__), join("menu/", 'menu.dot')))

def export_example_model():
    my_model = get_model('example.rbt')
    model_export(my_model, 'example.dot')

def get_data_from_database():
    my_model = get_model('example.rbt')
    for menu_section in my_model.menuSections:
        for item in menu_section.items:
            if menu_section.section_type == 'Food':
                get_food_data_from_database(item.type)
            else:
                get_drink_data_from_database(item.type)

def get_food_data_from_database(type):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM food WHERE food_type=%(food_type)s", {'food_type': type})
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_drink_data_from_database(type):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM drink WHERE drink_type=%(drink_type)s", {'drink_type': type})
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    export_meta_model()
    export_example_model()
    get_data_from_database()