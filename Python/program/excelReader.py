import pandas as pd
from templateObjects import Stage

def read_excel():
    excel = pd.read_excel('../../Data_Dictionary.xlsx', sheet_name = 'Dict - only positional files', skiprows=1)
    filteredExcel = excel[excel['table /\nfile'] == 'ANABCR1P_BCR_DEFAULT']

    meta_rec_src = filteredExcel['source\nsystem'] + "." + filteredExcel['table /\nfile']
    src_nk = filteredExcel['target field name']