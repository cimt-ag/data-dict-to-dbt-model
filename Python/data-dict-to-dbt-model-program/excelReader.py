import pandas as pd

def read_excel():
    excel = pd.read_excel('../../Data_Dictionary.xlsx', sheet_name = 'Dict', skiprows=1)

    # Alternativ: df.iloc[:, [1]] um numerisch zu selektieren, nicht beim Namen
    source_column = tuple(excel['source\nsystem'])
    library_column = tuple(excel['library /\npath /\nscheme'])
    source_field_column = tuple(excel['field name in the source system'])
    description_column = tuple(excel['description'])

    dataFrame = pd.DataFrame({
        'Source': source_column,
        'Library': library_column,
        'Source Field': source_field_column,
        'Description': description_column
    })

    print(dataFrame)