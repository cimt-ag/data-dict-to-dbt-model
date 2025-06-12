from excelReader import read_excel
from stageObjectCreator import create_stage_objects
from hubObjectCreator import create_hub_objects
from templateEditor import create_stage_templates, create_hub_templates
from sqlFileGenerator import write_stage_files, write_hub_files

def main():
    excelDataframe = read_excel()
    stageObjects = create_stage_objects(excelDataframe)
    stageTemplates = create_stage_templates(stageObjects)
    write_stage_files(stageTemplates)
    hubObjects = create_hub_objects(excelDataframe)
    hubTemplates = create_hub_templates(hubObjects)
    write_hub_files(hubTemplates)

if __name__ == "__main__":
    main()