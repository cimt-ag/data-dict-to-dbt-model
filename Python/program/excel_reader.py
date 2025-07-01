import pandas as pd


def read_excel(filePath, sheetName):
    excel = pd.read_excel(filePath, sheetName, skiprows=1)
    filteredExcel = excel[excel['table /\nfile'] == 'ANABCR1P_BCR_DEFAULT']
    return filteredExcel

def get_all_values(excelDataframe):
    valuesForAllRows: list = []
    for _, currentRow in excelDataframe.iterrows():
        rowValues: dict = {}

        rowValues["source_model"] = get_source_model(currentRow)
        rowValues["src_source"] = get_src_source(currentRow)
        rowValues["src_nk"] = get_business_key(currentRow)
        rowValues["hashdiff_columns"] = get_hashdiff_columns(currentRow)
        rowValues["src_eff"] = get_src_eff(currentRow)

        valuesForAllRows.append(rowValues)
    return valuesForAllRows

def get_source_model(row):
    return row["field name in the source system"]

def get_src_source(row):
    return row["source\nsystem"] + "." + row["table /\nfile"]

def get_business_key(row):
    if pd.isna(row["target field name"]):
        if pd.isna(row["alternative name / \nidentifier in interface"]):
            return row["field name in the source system"]
        else:
            return row["alternative name / \nidentifier in interface"]
    else:
        return row["target field name"]

def get_hashdiff_columns(row):
    return (row["data type\n(CHAR, INT, DEC, DATE, DOUBLE, Timestamp etc.)"], row["format / \nlength\n(0 / 0,00 / yyyy-mm-dd etc.)"], row["nullable?\n( Y / N)"])

def get_src_eff(row):
    return row["position\nfrom"]