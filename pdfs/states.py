from random import randint

from jinja2 import Environment, FileSystemLoader
import pdfkit
# from weasyprint import HTML
import os
# from pyhtml2pdf import converter
from html2image import Html2Image


def create_pdf(data: dict, id: int) -> str:
    env = Environment(loader=FileSystemLoader('pdfs/'))
    template = env.get_template("template.html")

    data["number"] = str(id)

    pdf_template = template.render(data)
    hti = Html2Image(size=(500, 705))

    hti.screenshot(html_str=pdf_template, save_as=f'{id}.png')
    # pdfkit.from_string(pdf_template, name_file)
    # HTML(string=pdf_template).write_pdf(name_file)

# print(create_pdf())
