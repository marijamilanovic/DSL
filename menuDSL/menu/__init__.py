import os
from textx import language, metamodel_from_file

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
