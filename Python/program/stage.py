from template_builder import TemplateBuilder


def create_stage_model(templateFolder: str, modelFolder: str, valueDict: dict):
    templatePath = templateFolder + "/Staging_Template.sql"
    modelPath = modelFolder + "/staging/{filename}_stage.sql"

    values = {}
    values["materialization"] = "view"
    values["source_model"] = valueDict.get("source_model")
    values["src_source"] = valueDict.get("src_source")
    values["src_ldts"] = "TIMESTAMP()"
    values["src_nk"] = valueDict.get("src_nk")
    values["src_job_instance_id"] = -1
    values["src_encryptionkey_index"] = 0
    values["hashdiff_columns"] = valueDict.get("hashdiff_columns")

    stageTemplateObject = TemplateBuilder(templatePath, modelPath, values)
    stageTemplate = stageTemplateObject.read_template()
    editedTemplate = stageTemplateObject.edit_template(stageTemplate)
    stageTemplateObject.write_model(editedTemplate, values["src_nk"].lower())