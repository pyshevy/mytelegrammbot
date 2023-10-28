from random import randint

from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML
import os
# from pyhtml2pdf import converter
from html2image import Html2Image

import imgkit



def create_pdf(data: dict, id: int) -> str:
    env = Environment(loader=FileSystemLoader('pdfs/'))
    template = env.get_template("template.html")
    data["number"] = str(id)

    pdf_template = template.render(data)

    try:
        options = { 'width': '500', 'height': '705' }

        imgkit.from_string(pdf_template, f'{id}.jpg', options=options)

    except:
        hti = Html2Image(size=(500, 705))
        hti.screenshot(html_str=pdf_template, save_as=f'{id}.png')


    # pdfkit.from_string(pdf_template, name_file)
    # HTML(string=pdf_template).write_pdf(name_file)

# print(create_pdf())
#create_pdf(data={'type': 'writing', 'otdelenie': 'Взрослая поликлиника', 'doctor': ['Врач дерматовенеролог', 'Иванцов Федор Алексеевич', '08:00-14:00', '221'], 'name': 'f g', 'date': '17.05.2008', 'year': '15 лет', 'date_a': 'Вторник 26.10 в 13:20', 'number': '986717'}, id=1212121)
