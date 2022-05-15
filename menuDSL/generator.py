import os
from os.path import join, dirname
from models.food import Food
from models.ingredient import Ingredient
from models.drink import Drink
import pdfkit

def create_folder():
    if not os.path.exists('generated'):
            os.makedirs('generated')

def generate_pdf_from_html(output_dir):
    print('Generating pdf...')
    pdfkit.from_file(
        output_dir + "/output.html", 
        output_dir + "/output.pdf",
        configuration=pdfkit.configuration(
            wkhtmltopdf = join(dirname(__file__), 'wkhtmltopdf.exe')
            )
    )
    print('PDF has been generated')
    