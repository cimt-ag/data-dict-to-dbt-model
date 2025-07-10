from template_builder import TemplateBuilder

def create_hub_model(valueDict):
        templatePath = "../../Hub_Template.sql"
        modelPath = "../../DBT/models/hubs/hub_{filename}.sql"

        values = {}
        values["materialization"] = "incremental"
        values["source_model"] = valueDict.get("src_nk").lower() + "_stage"
        values["src_source"] = "META_REC_SRC"
        values["src_ldts"] = "META_LOAD_DTS"
        values["src_nk"] = valueDict.get("src_nk")
        values["src_pk"] = valueDict.get("src_nk") + "_HK"

        templateObject = TemplateBuilder(templatePath, modelPath, values)
        template = templateObject.read_template()
        editedTemplate = templateObject.edit_template(template)
        templateObject.write_model(editedTemplate, values["src_nk"].lower())