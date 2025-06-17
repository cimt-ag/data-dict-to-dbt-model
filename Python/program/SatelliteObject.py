class LinkObject():
    linkTemplatePath = "../../Link_Template.sql"
    linkModelPath = "../../DBT/models/links_automateDV/link_{filename}.sql"

    def __init__(self, source_model, src_pk, src_fk, src_ldts, src_source):
        self.source_model = source_model
        self.src_pk = src_pk
        self.src_fk = src_fk
        self.src_ldts = src_ldts
        self.src_source = src_source

    def edit_link_template(self):
        with open(self.linkTemplatePath, 'r', encoding = 'utf-8') as file:
            linkTemplate = file.read()

        editedTemplate = linkTemplate.format(
            source_model = self.source_model,
            src_pk = self.src_pk,
            src_nk = self.src_fk,
            src_ldts = self.src_ldts,
            src_source = self.src_source
        )

        return editedTemplate

    def write_link_model(self, linkModel):
        with open (self.linkModelPath.format(filename = self.src_fk.lower()), 'w') as linkModelFile:
            linkModelFile.write(linkModel)