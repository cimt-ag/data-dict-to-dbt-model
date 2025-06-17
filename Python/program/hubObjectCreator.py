from HubObject import HubObject

import pandas as pd

def create_hub_objects(excelDataframe):
    valueCollections = get_all_objects_values(excelDataframe)
    hubObjects = []
    for valueDict in valueCollections:
        business_key = valueDict.get("business_key")
        newHubObject = HubObject(business_key)
        hubObjects.append(newHubObject)
    return hubObjects

def get_all_objects_values(excelDataframe):
    hubObjectValues = []
    for _, currentRow in excelDataframe.iterrows():
        hubObjectValues.append(get_object_values(currentRow))
    return hubObjectValues

def get_object_values(currentRow):
    business_key = get_business_key(currentRow)
    hubObjectValues = {"business_key": business_key}
    return hubObjectValues

def get_business_key(currentRow):
    if pd.isna(currentRow["target field name"]):
        if pd.isna(currentRow["alternative name / \nidentifier in interface"]):
            return currentRow["field name in the source system"]
        else:
            return currentRow["alternative name / \nidentifier in interface"]
    else:
        return currentRow["target field name"]