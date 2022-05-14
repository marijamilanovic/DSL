from os import mkdir
from os.path import join, dirname, exists
from textx import metamodel_from_file, metamodel_for_language, register_language
from textx.export import metamodel_export, model_export_to_file, model_export
from io import StringIO
import psycopg2
from config import config
from food import Food
from ingredient import Ingredient
from drink import Drink
import jinja2

print(join(dirname(__file__), 'templates'))
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(join(dirname(__file__), 'templates')), trim_blocks=True, lstrip_blocks=True)

all_data = {}
all_data_colnames = {}


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
    return my_model

class Menu:
    def __init__(self, menu_sections=None):
        self.menu_sections = menu_sections

    def interpret(self, model):
        #print(model.menu_sections[0].items[0].type)
        for m in model.menu_sections:
            #print(m.__class__.__name__)
            #print(m.section_type)
            for item in m.items:
                print(item.type)

def get_food_data_from_database():
    my_model = get_model('example.rbt')
    all_food = []
    for menu_section in my_model.menu_sections:
        for item in menu_section.items:
            if menu_section.section_type == 'Food':
                food = find_food_data_from_database(item.type)  #lista filtrirane hrane
                for f in food:
                    all_food.append(f)
    return all_food

def get_drink_data_from_database():
    my_model = get_model('example.rbt')
    all_drinks = []
    for menu_section in my_model.menu_sections:
        for item in menu_section.items:
            if menu_section.section_type == 'Drinks':
                drinks = find_drink_data_from_database(item.type)
                for drink in drinks:
                    all_drinks.append(drink)
    return all_drinks

def find_food_data_from_database(type):
    conn = None
    foods = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM food WHERE food_type=%(food_type)s", {'food_type': type})
        rows = cur.fetchall()
        for row in rows:
            food = Food(row[0], row[1], row[2], row[3])
            find_ingredients(food)
            foods.append(food)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return foods

def find_drink_data_from_database(type):
    conn = None
    drinks = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM drink WHERE drink_type=%(drink_type)s", {'drink_type': type})
        rows = cur.fetchall()

        for row in rows:
            drink = Drink(row[0], row[1], row[2], row[3])
            drinks.append(drink)
            
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return drinks

def find_ingredients(food):
    conn = None
    food_ingredients = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM food_ingredient WHERE food_id=%(food_id)s", {'food_id': food.id})
        rows = cur.fetchall()
       
        for row in rows:
            cur.execute("SELECT * FROM ingredient WHERE id=%(id)s", {'id': row[2]})
            ingredients = cur.fetchall()
            for i in ingredients:
                food.add_ingredient(i)
                food_ingredients.append(i)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return food_ingredients

def generate(model, outuput_dir):
    print('GENERISEM')
    output_folder = open(outuput_dir + "/output.html", 'w', encoding="utf-8")

    template = jinja_env.get_template('header_html.j2')
    output_folder.write(template.render())

    parse_table(output_folder)

    output_folder.close()

def parse_table(output_folder):
    col_names = ['Name', 'Price']
    main_dishes = []
    soups = []
    hot_drinks = []
    appetizers = []
    house_specials = []
    salads = []
    deserts = []
    alchocols = []
    carbonateds = []
    juices = []
    items = []
    title = ''
    for menu_section in my_model.menu_sections:
        title = my_model.title
        sections = my_model.menu_sections
        for item in menu_section.items:
            items.append(item)

    food_data = get_food_data_from_database() 
    drink_data = get_drink_data_from_database()  
    for food in food_data:
        if food.food_type == 'MainDishes':
            main_dishes.append(food)
        elif food.food_type == 'Soups':
            soups.append(food)
        elif food.food_type == 'Appetizers':
            appetizers.append(food)
        elif food.food_type == 'HouseSpecials':
            house_specials.append(food)
        elif food.food_type == 'Salads':
            salads.append(food)
        else:
            deserts.append(food)
    
    for drink in drink_data:
        if drink.drink_type == 'HotDrinks':
            hot_drinks.append(drink)
        elif drink.drink_type == 'Alchocol':
            alchocols.append(drink)
        elif drink.drink_type == 'Carbonated':
            carbonateds.append(drink)
        else:
            juices.append(drink)
    
    template = jinja_env.get_template('table.j2')
    output_folder.write(template.render(sections = sections, col_names=col_names, items = items, main_dishes = main_dishes , 
    soups = soups, salads = salads, appetizers = appetizers, deserts = deserts, house_specials = house_specials,
    hot_drinks = hot_drinks, juices = juices, alchocols = alchocols, carbonateds = carbonateds, title = title))


if __name__ == "__main__":
    export_meta_model()
    #get_food_data_from_database()
    my_model = export_example_model()
    menu = Menu()
    menu.interpret(my_model)
    generate(my_model,"generated/" )

