from excel_reader import read_excel, get_all_values
from stage import create_stage_model
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