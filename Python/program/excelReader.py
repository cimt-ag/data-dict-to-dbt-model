import pandas as pd

def read_excel():
    excel = pd.read_excel('../../Data_Dictionary.xlsx', sheet_name = 'Dict - only positional files', skiprows=1)
    filteredExcel = excel[excel['table /\nfile'] == 'ANABCR1P_BCR_DEFAULT']
    #print(filteredExcel.columns.tolist())
    return filteredExcel