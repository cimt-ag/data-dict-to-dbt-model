class TemplateBuilder:
    """
    A utility class to build model files based on templates.

    This class reads a template file from a parameterized path.
    It then maps placeholder text with values from a dictionary and writes the file into a specified folder.

    Attributes:
        templatePath (str): The file path to the template file.
        modelPath (str): The file path template to the output folder.
        values (dict): A dictionary of values used to populate the template.
    """

    def __init__(self, templatePath: str, modelPath: str, values: dict):
        """
        Initializes the templatebuilder and sets its path and values attributes.

        Args:
            templatePath (str): The path to the input template file.
            modelPath (str): The path to the output model folder.
            values (dict): A dictionary of values to be mapped into the template.
        """
        self.templatePath = templatePath
        self.modelPath = modelPath
        self.values = values

    def read_template(self) -> str:
        """
        Reads the template file from the given path and returns the content as a string.
        
        Returns:
            templateFile.read() (str): The content of the read template file.
        """
        with open(self.templatePath, 'r', encoding = 'utf-8') as templateFile:
            return templateFile.read()

    def edit_template(self, template) -> str:
        """
        Edits the template file content by maping the object values to placeholders.

        Args:
            template (str): The template file content as a string.
        
        Returns:
            template.format_map() (str): The template string editted with mapped values.
        """
        return template.format_map(self.values)

    def write_model(self, filename: str):
        """
        Writes the edited template to a dbt model file.

        Args:
            filename (str): The business key of this object, used to edit the model file name.
        """
        template = self.read_template()
        editedTemplate = self.edit_template(template)
        with open (self.modelPath.format(filename = filename), 'w') as modelFile:
            modelFile.write(editedTemplate)