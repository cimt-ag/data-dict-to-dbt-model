class Satellite():
    satTemplatePath = "../../Satellite_Template.sql"
    satModelPath = "../../DBT/models/sats/sat_{filename}.sql"

    def __init__(self, source_model, src_pk, src_fk, src_ldts, src_source):
        self.source_model = source_model
        self.src_pk = src_pk
        self.src_fk = src_fk
        self.src_ldts = src_ldts
        self.src_source = src_source

    def edit_sat_template(self):
        with open(self.satTemplatePath, 'r', encoding = 'utf-8') as file:
            satTemplate = file.read()

        editedTemplate = satTemplate.format(
            source_model = self.source_model,
            src_pk = self.src_pk,
            src_nk = self.src_fk,
            src_ldts = self.src_ldts,
            src_source = self.src_source
        )

        return editedTemplate

    def write_sat_model(self, satModel):
        with open (self.satModelPath.format(filename = self.src_fk.lower()), 'w') as satModelFile:
            satModelFile.write(satModel)