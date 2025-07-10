from templateobject import TemplateObject

class Satellite(TemplateObject):
    def __init__(
            self,
            src_nk,
            source_model,
            src_pk,
            src_column,
            payload_columns,
            src_eff,
            materialization="incremental",
            alias="HASHDIFF",
            src_ldts="META_LOAD_DTS",
            src_source="META_REC_SRC"
        ):
        self.src_nk = src_nk
        self.source_model = source_model
        self.src_pk = src_pk
        self.src_column = src_column
        self.payload_columns = payload_columns
        self.materialization = materialization
        self.src_eff = src_eff
        self.alias = alias
        self.src_ldts = src_ldts
        self.src_source = src_source
    
    @property
    def templatePath(self):
        return "../../Satellite_Template.sql"
    
    @property
    def modelPath(self):
        return "../../DBT/models/sats/sat_{filename}.sql"

    def edit_template(self):
        with open(self.templatePath, 'r', encoding = 'utf-8') as file:
            satTemplate = file.read()

        editedTemplate = satTemplate.format(
            materialization = self.materialization,
            source_model = self.source_model,
            src_pk = self.src_pk,
            src_column = self.src_column,
            alias = self.alias,
            payload_columns = self.format_arrays(),
            src_eff = self.src_eff,
            src_ldts = self.src_ldts,
            src_source = self.src_source
        )

        return editedTemplate
    
    def format_arrays(self):
        # Indentation needs to be done more dynamically
        return '\n'.join([f"\t- \"{column}\"" for column in self.payload_columns])

    def write_model(self, editedTemplate):
        with open (self.modelPath.format(filename = self.src_nk.lower()), 'w') as satModelFile:
            satModelFile.write(editedTemplate)