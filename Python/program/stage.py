class Stage:
    stageTemplatePath = "../../Staging_Template.sql"
    stageModelPath = "../../DBT/models/staging/{filename}_stage.sql"

    def __init__(
            self,
            source_model,
            src_source,
            src_nk,
            hashdiff_columns,
            materialization="view",
            load_dts="TIMESTAMP()",
            src_job_instance_id=-1,
            src_encryptionkey_index=0
        ):
        self.source_model = source_model
        self.src_source = src_source
        self.src_nk = src_nk
        self.hashdiff_columns = hashdiff_columns
        self.materialization = materialization
        self.load_dts = load_dts
        self.src_job_instance_id = src_job_instance_id
        self.src_encryptionkey_index = src_encryptionkey_index

    def edit_stage_template(self):
        with open(self.stageTemplatePath, 'r', encoding = 'utf-8') as file:
            stageTemplate = file.read()

        editedTemplate = stageTemplate.format(
            materialization = self.materialization,
            source_model = self.source_model,
            src_source = self.src_source,
            src_nk = self.src_nk,
            hashdiff_columns = self.format_array(),
            load_dts = self.load_dts,
            src_job_instance_id = self.src_job_instance_id,
            src_encryptionkey_index = self.src_encryptionkey_index
        )

        return editedTemplate

    def format_array(self):
        # Indentation needs to be done more dynamically
        return '\n'.join(([f"\t\t\t- \"{column}\"" for column in self.hashdiff_columns]))

    def write_stage_model(self, editedTemplate):
        with open (self.stageModelPath.format(filename = self.src_nk.lower()), 'w') as stageModelFile:
            stageModelFile.write(editedTemplate)