import os
from textx import language, metamodel_from_file
from textx import generator as file_generator
from .interpreter import generate

__version__ = "0.1.0.dev"


@language('menu', '*.que')
def menu_language():
    "menu language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'menu.tx'))

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm


@gen('menu', 'html+pdf')
def menu_generate_files(metamodel, model, output_path, overwrite, debug): 
    """Generating pdf and html from document visualization text"""
    input_file = model._tx_filename
    output_dir = output_path if output_path else dirname(input_file)
    generate(model, output_dir)
    