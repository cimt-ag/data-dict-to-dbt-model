class StageObject:
    stageTemplatePath = "../../Staging_Template.sql"
    stageModelPath = "../../DBT/models/staging_automateDV/{filename}_stage.sql"

    def __init__(self, source_model, src_nk, src_source, src_job_instance_id=-1, src_encryptionkey_index=0):
        self.source_model = source_model
        self.src_nk = src_nk
        self.src_source = src_source
        self.src_job_instance_id = src_job_instance_id
        self.src_encryptionkey_index = src_encryptionkey_index

    def edit_stage_template(self):
        with open(self.stageTemplatePath, 'r', encoding = 'utf-8') as file:
            stageTemplate = file.read()

        editedTemplate = stageTemplate.format(
            source_model = self.source_model,
            src_nk = self.src_nk,
            src_source = self.src_source,
            src_job_instance_id = self.src_job_instance_id,
            src_encryptionkey_index = self.src_encryptionkey_index
        )

        return editedTemplate

    def write_stage_model(self, stageModel):
        with open (self.stageModelPath.format(filename = self.src_nk.lower()), 'w') as stageModelFile:
            stageModelFile.write(stageModel)