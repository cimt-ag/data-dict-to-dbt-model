from excel_reader import read_excel, get_fields
from utils import find_path


def main():
    excelDataframe = read_excel()
    valueDicts = get_fields(excelDataframe)

    templatesFolder: str = "Templates"
    modelsFolder: str = "models"
    
    templatesPath = find_path(templatesFolder)
    modelsPath = find_path(modelsFolder)

if __name__ == "__main__":
    main()