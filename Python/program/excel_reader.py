import pandas as pd
from pandas import DataFrame, Series


def read_excel(filePath: str, sheetName: str):
    excel: DataFrame = pd.read_excel(filePath, sheetName, skiprows=1)
    filteredExcel: DataFrame = excel[excel['table /\nfile'] == 'ANABCR1P_BCR_DEFAULT']
    return filteredExcel

def get_all_values(excelDataframe: DataFrame):
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

def get_source_model(row: Series):
    source_model: Series = row["field name in the source system"]
    return source_model

def get_src_source(row:  Series):
    src_source: Series = row["source\nsystem"] + "." + row["table /\nfile"]
    return src_source

def get_business_key(row: Series):
    business_key: Series
    if pd.isna(row["target field name"]):
        if pd.isna(row["alternative name / \nidentifier in interface"]):
            business_key = row["field name in the source system"]
        else:
            business_key = row["alternative name / \nidentifier in interface"]
    else:
        business_key = row["target field name"]
    return business_key

def get_hashdiff_columns(row: Series):
    hashdiff_columns: Series = (row["data type\n(CHAR, INT, DEC, DATE, DOUBLE, Timestamp etc.)"], row["format / \nlength\n(0 / 0,00 / yyyy-mm-dd etc.)"], row["nullable?\n( Y / N)"])
    return hashdiff_columns

def get_src_eff(row: Series):
    src_eff: Series = row["position\nfrom"]
    return src_eff