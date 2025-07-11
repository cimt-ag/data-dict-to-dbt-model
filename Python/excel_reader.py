"""
Module: excel_reader

Description:
    Provides functions to read and extract structured values from a formatted Excel file, specifically for data modeling workflows.
    Filters specific entries from the Excel sheet and maps them into dictionaries for use in model generation.

Functions:
    - read_excel(filePath, sheetName): Reads the Excel sheet and filters rows based on a predefined table name.
    - get_all_values(excelDataframe): Iterates through the dataframe and extracts required fields from each row.
    - get_source_model(row): Returns the field name in the source system.
    - get_src_source(row): Constructs the source string using source system and table name.
    - get_business_key(row): Determines the best available field to use as a business key.
    - get_hashdiff_columns(row): Returns a tuple of technical metadata about a field (type, format, nullability).
    - get_src_eff(row): Retrieves the position information for effective dating.

Dependencies:
    - pandas
"""

import pandas as pd

from pandas import DataFrame, Series


def read_excel(filePath: str, sheetName: str):
    """
    Reads an Excel sheet, skipping the first row, and filters rows where 'table /\nfile' equals a specific value.

    Args:
        filePath (str): Path to the Excel file.
        sheetName (str): Name of the worksheet to read.

    Returns:
        DataFrame: Filtered Excel data.
    """
    excel: DataFrame = pd.read_excel(filePath, sheetName, skiprows=1)
    filteredExcel: DataFrame = excel[excel['table /\nfile'] == 'ANABCR1P_BCR_DEFAULT']
    return filteredExcel

def get_all_values(excelDataframe: DataFrame) -> list:
    """
    Extracts and maps all relevant values from the given dataframe and returns them as a list containing a dictionary of values for every row.

    Args:
        excelDataframe (DataFrame): The filtered dataframe to extract values from.
    
    Returns:
        valuesForAllRows (list[dict]): A list of dictionaries containing row values.
    """
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

def get_source_model(row: Series) -> str:
    """
    Extracts the source_model value from the defined dataframe column for this row.

    Args:
        row (Series): The current row of the dataframe.
    
    Returns:
        source_model (str): A string containing the value from the specified column of this row.
    """
    source_model: str = row["field name in the source system"]
    return source_model

def get_src_source(row: Series) -> str:
    """
    Extracts the src_source value from the defined dataframe column for this row.

    Args:
        row (Series): The current row of the dataframe.
    
    Return:
        src_source (str): A string containing the value from the specified column of this row.
    """
    src_source: str = row["source\nsystem"] + "." + row["table /\nfile"]
    return src_source

def get_business_key(row: Series) -> str:
    """
    Extracts the business_key value from the specified dataframe columns, depending on prioritized availability.

    Args:
        row (Series): The current row of the dataframe.
    
    Returns:
        business_key (str): A string containing the value from the selected column of this row.
    """
    if pd.notna(row["target field name"]):
       return row["target field name"]
    if pd.notna(row["alternative name / \nidentifier in interface"]):
        return row["alternative name / \nidentifier in interface"]
    return row["field name in the source system"]

def get_hashdiff_columns(row: Series) -> tuple:
    """
    Extracts the hashdiff_columns values from the defined dataframe columns for this row.

    Args:
        row (Series): The current row of the dataframe.
    
    Return:
        hashdiff_columns (tuple): A tuple containing the values from the specified columns of this row.
    """
    hashdiff_columns: tuple = (row["data type\n(CHAR, INT, DEC, DATE, DOUBLE, Timestamp etc.)"], row["format / \nlength\n(0 / 0,00 / yyyy-mm-dd etc.)"], row["nullable?\n( Y / N)"])
    return hashdiff_columns

def get_src_eff(row: Series) -> str:
    """
    Extracts the src_eff value from the defined dataframe column for this row.

    Args:
        row (Series): The current row of the dataframe.
    
    Returns:
        src_eff (str): A string containing the value from the specified column of this row.
    """
    src_eff: str = row["position\nfrom"]
    return src_eff