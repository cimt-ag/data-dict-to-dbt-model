from templateObjects import Stage

import pandas as pd

def create_stage_objects(excelDataframe):
    valueCollections = get_all_objects_values(excelDataframe)
    stageObjects = []
    for valueDict in valueCollections:
        business_key = valueDict.get("business_key")
        meta_rec_src = valueDict.get("meta_rec_src")
        newStageObject = Stage(business_key, meta_rec_src)
        stageObjects.append(newStageObject)
    return stageObjects

def get_all_objects_values(excelDataframe):
    stageObjectValues = []
    for _, currentRow in excelDataframe.iterrows():
        stageObjectValues.append(get_object_values(currentRow))
    return stageObjectValues

def get_object_values(currentRow):
    business_key = get_business_key(currentRow)
    meta_rec_src = get_meta_rec_src(currentRow)
    stageObjectValues = {"business_key": business_key, "meta_rec_src": meta_rec_src}
    return stageObjectValues

def get_business_key(currentRow):
    if pd.isna(currentRow["target field name"]):
        if pd.isna(currentRow["alternative name / \nidentifier in interface"]):
            return currentRow["field name in the source system"]
        else:
            return currentRow["alternative name / \nidentifier in interface"]
    else:
        return currentRow["target field name"]

def get_meta_rec_src(currentRow):
    return currentRow["source\nsystem"] + "." + currentRow["table /\nfile"]