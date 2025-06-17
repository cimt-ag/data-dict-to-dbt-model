class Hub():
    hubTemplatePath = "../../Hub_Template.sql"
    hubModelPath = "../../DBT/models/hubs/hub_{filename}.sql"

    def __init__(
            self,
            source_model,
            src_pk,
            src_nk,
            materialization="incremental",
            src_ldts="META_LOAD_DTS",
            src_source="META_REC_SRC"
        ):
        self.source_model = source_model
        self.src_pk = src_pk
        self.src_nk = src_nk
        self.materialization = materialization
        self.src_ldts = src_ldts
        self.src_source = src_source

    def edit_hub_template(self):
        with open(self.hubTemplatePath, 'r', encoding = 'utf-8') as file:
            hubTemplate = file.read()

        editedTemplate = hubTemplate.format(
            materialization = self.materialization,
            source_model = self.source_model,
            src_pk = self.src_pk,
            src_nk = self.src_nk,
            src_ldts = self.src_ldts,
            src_source = self.src_source
        )

        return editedTemplate

    def write_hub_model(self, editedTemplate):
        with open (self.hubModelPath.format(filename = self.src_nk.lower()), 'w') as hubModelFile:
            hubModelFile.write(editedTemplate)