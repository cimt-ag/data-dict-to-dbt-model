from template_builder import TemplateBuilder


def create_stage_model(valueDict):
    templatePath = "../../Staging_Template.sql"
    modelPath = "../../DBT/models/staging/{filename}_stage.sql"

    values = {}
    values["materialization"] = "view"
    values["source_model"] = valueDict.get("source_model")
    values["src_source"] = valueDict.get("src_source")
    values["src_ldts"] = "TIMESTAMP()"
    values["src_nk"] = valueDict.get("src_nk")
    values["src_job_instance_id"] = -1
    values["src_encryptionkey_index"] = 0
    values["hashdiff_columns"] = valueDict.get("hashdiff_columns")

    templateObject = TemplateBuilder(templatePath, modelPath, values)
    template = templateObject.read_template()
    editedTemplate = templateObject.edit_template(template)
    templateObject.write_model(editedTemplate, values["src_nk"].lower())