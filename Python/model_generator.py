"""
Module: model_generator.py

Description:
    This script automates the generation of DBT stage models based on data from an Excel data dictionary.
    It reads an Excel sheet, extracts relevant values, and uses templates to create corresponding models.

Functions:
    - main(): The entry point of the script. Locates necessary files and directories, reads data from Excel,
              and generates stage models for each row in the sheet.

Workflow:
    1. Locates the Excel file and required folders (templates and models) using `find_path()`.
    2. Reads a specific worksheet from the Excel file using `read_excel()`.
    3. Extracts all relevant row values from the worksheet with `get_all_values()`.
    4. Iterates through each row dictionary and generates a stage model using `create_stage_model()`.

Dependencies:
    - excel_reader.py: Contains `read_excel()` and `get_all_values()` to handle Excel I/O.
    - stage.py: Contains `create_stage_model()` for generating model files.
    - utils.py: Contains `find_path()` for resolving file and directory paths.

Assumptions:
    - The Excel file must contain a sheet named "Dict - only positional files".
    - The project structure contains identifiable folders/files for templates and model output.

"""

from excel_reader import read_excel, get_all_values

from dvobjects.stage import create_stage_model

from utils import find_path


def main():
    sheetName:str  = "Dict - only positional files"
    excelFileName: str = "Data_Dictionary.xlsx"
    templatesFolderName: str = "Templates"
    modelsFolderName: str = "models"

    excelPath: str = find_path(excelFileName).as_posix()
    templatesPath: str = find_path(templatesFolderName).as_posix()
    modelsPath: str = find_path(modelsFolderName).as_posix()

    excelDataframe = read_excel(excelPath, sheetName)
    allValues: list = get_all_values(excelDataframe)

    for valueDict in allValues:
        create_stage_model(templatesPath, modelsPath, valueDict)

if __name__ == "__main__":
    main()