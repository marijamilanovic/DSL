from os import mkdir
from os.path import join, dirname, exists
from textx import metamodel_from_file, metamodel_for_language, register_language
from textx.export import metamodel_export, model_export_to_file, model_export
from io import StringIO

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
    #print(my_model.menu_sections[0].items[0].type)
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


if __name__ == "__main__":
    export_meta_model()
    my_model = export_example_model()
    menu = Menu()
    menu.interpret(my_model)