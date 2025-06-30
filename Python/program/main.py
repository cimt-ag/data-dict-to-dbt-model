from excel_reader import read_excel, get_all_values
from stage import create_stage_model
from utils import find_path


def main():
    excelFileName: str = "Data_Dictionary.xlsx"
    templatesFolderName: str = "Templates"
    modelsFolderName: str = "models"

    excelPath = find_path(excelFileName)
    templatesPath: str = find_path(templatesFolderName).as_posix()
    modelsPath: str = find_path(modelsFolderName).as_posix()
    
    sheetName = "Dict - only positional files"

    excelDataframe = read_excel(excelPath, sheetName)
    allValues = get_all_values(excelDataframe)

    for valueDict in allValues:
        create_stage_model(templatesPath, modelsPath, valueDict)

if __name__ == "__main__":
    main()