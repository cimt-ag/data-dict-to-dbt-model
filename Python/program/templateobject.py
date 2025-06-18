from abc import ABC, abstractmethod

class TemplateObject(ABC):

    @property
    @abstractmethod
    def templatePath(self):
        pass

    @property
    @abstractmethod
    def modelPath(self):
        pass

    @abstractmethod
    def edit_template(self):
        pass

    @abstractmethod
    def write_model(self):
        pass