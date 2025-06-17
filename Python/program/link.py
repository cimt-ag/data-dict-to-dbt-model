import json

class Link():
    linkTemplatePath = "../../Link_Template.sql"
    linkModelPath = "../../DBT/models/links/link_{filename}.sql"

    def __init__(
            self,
            source_model,
            src_pk,
            src_fk=["LINKSOURCE1_HK", "LINKSOURCE2_HK"],
            materialization="incremental",
            src_ldts="META_LOAD_DTS",
            src_source="META_REC_SRC"
        ):
        self.source_model = source_model
        self.src_pk = src_pk
        self.src_fk = src_fk
        self.materialization = materialization
        self.src_ldts = src_ldts
        self.src_source = src_source

    def edit_link_template(self):
        with open(self.linkTemplatePath, 'r', encoding = 'utf-8') as file:
            linkTemplate = file.read()

        editedTemplate = linkTemplate.format(
            materialization = self.materialization,
            source_model = self.source_model,
            src_pk = self.src_pk,
            src_fk = json.dumps(self.src_fk),
            src_ldts = self.src_ldts,
            src_source = self.src_source
        )

        return editedTemplate

    def write_link_model(self, editedTemplate):
        with open (self.linkModelPath.format(filename = self.src_pk.replace("_HK", "").lower()), 'w') as linkModelFile:
            linkModelFile.write(editedTemplate)