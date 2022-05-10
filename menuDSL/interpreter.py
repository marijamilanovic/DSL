from os import mkdir
from os.path import join, dirname, exists
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export_to_file, model_export
from io import StringIO
import psycopg2


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
    print(my_model.menuSections[0].items[0].type)
    model_export(my_model, 'example.dot')


if __name__ == "__main__":
    export_meta_model()
    export_example_model()