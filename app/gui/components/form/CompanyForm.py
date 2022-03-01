from app.gui.components.form.Form import Form
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.models import Company


class CompanyForm(Form):
    def __init__(self, model: Company) -> None:
        super(CompanyForm, self).__init__("CompanyInfo", model, "Company Information")

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Name")
        titleInput.setBinding(self._model, "name")
        titleInput.setPlaceholderText("Company name")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(self._model, "website")
        websiteInput.setPlaceholderText("www.job-application.com")

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(self._model, "comments")
        commentsInput.setPlaceholderText("Details about this job...")

        self.addRow(titleInput)
        self.addRow(websiteInput)
        self.addRow(commentsInput)
        # -------------------------- #
