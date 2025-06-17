import pandas as pd

def read_excel():
    # Path needs to be set via parameter or something else dynamically
    excel = pd.read_excel('../../Data_Dictionary.xlsx', sheet_name = 'Dict - only positional files', skiprows=1)
    filteredExcel = excel[excel['table /\nfile'] == 'ANABCR1P_BCR_DEFAULT']
    #print(filteredExcel.columns)
    return filteredExcel

def get_fields(excelDataframe):
    valueDicts = []
    for _, row in excelDataframe.iterrows():
        rowValues = {}

        # Getting the source model (table/file)
        rowValues["source_model"] = row["field name in the source system"]

        # Getting the source (META_REC_SOURCE)
        rowValues["src_source"] = row["source\nsystem"] + "." + row["table /\nfile"]

        # Getting the business key (nk)
        if pd.isna(row["target field name"]):
            if pd.isna(row["alternative name / \nidentifier in interface"]):
                rowValues["src_nk"] = row["field name in the source system"]
            else:
                rowValues["src_nk"] = row["alternative name / \nidentifier in interface"]
        else:
            rowValues["src_nk"] = row["target field name"]

        rowValues["hashdiff_columns"] = [row["data type\n(CHAR, INT, DEC, DATE, DOUBLE, Timestamp etc.)"], row["format / \nlength\n(0 / 0,00 / yyyy-mm-dd etc.)"], row["nullable?\n( Y / N)"]]

        rowValues["src_eff"] = row["position\nfrom"]

        valueDicts.append(rowValues)
    return valueDicts