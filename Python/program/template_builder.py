class TemplateBuilder:
    def __init__(self, templatePath: str, modelPath: str, values: dict):
        self.templatePath = templatePath
        self.modelPath = modelPath
        self.values = values

    def read_template(self):
        with open(self.templatePath, 'r', encoding = 'utf-8') as templateFile:
            return templateFile.read()

    def edit_template(self, template):
        return template.format_map(self.values)

    def write_model(self, editedTemplate, filename):
        with open (self.modelPath.format(filename = filename), 'w') as modelFile:
            modelFile.write(editedTemplate)