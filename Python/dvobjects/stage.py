"""
This module handles the creation of stage model files from a template.

It executes functions which read a predefined SQL template, edit the template by mapping values from a data dictionary into placeholder entries
and write the resulting DBT model file into a specified location.

Classes:
    Templatebuilder: Imported for the utility functions to read, edit and write the sql template.

Functions:
    create_stage_model(templateFolder: str, modelFolder: str, valueDict: dict):
        Populates values in the dict and triggers TemplateBuilder functions to read, edit and write the sql model template.
"""

from .template_builder import TemplateBuilder

from utils import format_collection


def create_stage_model(templateFolder: str, modelFolder: str, excelValuesDict: dict):
    """
    Creates a DBT model file by executing TemplateBuilder functions.

    This sets up the paths for the template and model files.
    Populates a new dict with values extracted from an excel file and set predefined values for certain keys (editing collection format if needed).
    Creates a TemplateBuilder object and executes it's function to write an sql template into the DBT model.

    Args:
        templateFolder (str): The parent directory containing the staging template.
        modelFolder (str): The parent directory containing the staging dbt models.
        excelValuesDict (dict): A dictionary containing values to be mapped into the sql template.
    """
    templatePath: str = templateFolder + "/Staging_Template.sql"
    modelPath: str = modelFolder + "/staging/{filename}_stage.sql"

    templateValues: dict = {}
    templateValues["materialization"] = "view"
    templateValues["source_model"] = excelValuesDict.get("source_model")
    templateValues["src_source"] = excelValuesDict.get("src_source")
    templateValues["src_ldts"] = "TIMESTAMP()"
    templateValues["src_nk"] = excelValuesDict.get("src_nk")
    templateValues["src_job_instance_id"] = -1
    templateValues["src_encryptionkey_index"] = 0
    templateValues["hashdiff_columns"] = format_collection(excelValuesDict.get("hashdiff_columns"))

    stageTemplateObject = TemplateBuilder(templatePath, modelPath, templateValues)
    stageTemplateObject.write_model(templateValues["src_nk"].lower())