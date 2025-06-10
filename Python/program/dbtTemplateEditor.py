from jinja2 import Template

from excelReader import read_excel

def read_dbt_template():
    with open ('../../Hubs_Template.sql', 'r') as file:
        dbt_template = Template(file.read())

    #print(read_excel())

    context = {
        
    }

    rendered_template = dbt_template.render()

    print(rendered_template)