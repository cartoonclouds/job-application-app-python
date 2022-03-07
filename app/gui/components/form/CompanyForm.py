from app.gui.components.form.Form import Form
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.models.Company import Company
from PySide6.QtWidgets import QCompleter


class CompanyForm(Form):
    def __init__(self, model: Company) -> None:
        super(CompanyForm, self).__init__("CompanyInfo", model, "Company Information")

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Name")
        titleInput.setBinding(self._model, "name")
        titleInput.setPlaceholderText("Company name")

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QCompleter.html
        titleInput.setCompleter(QCompleter(list(Company.all().pluck("name"))))
        # on completer.activated.connect(update other fields)
        titleInput.setInputMask("9999-999-999")

        phoneInput = TextInput("Phone")
        phoneInput.setBinding(self._model, "phone")
        phoneInput.setPlaceholderText("Company phone number")

        mobileInput = TextInput("Mobile")
        mobileInput.setBinding(self._model, "mobile")
        mobileInput.setPlaceholderText("Company mobile number")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(self._model, "website")
        websiteInput.setPlaceholderText("www.job-application.com")

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(self._model, "comments")
        commentsInput.setPlaceholderText("Details about this job...")

        self.addRow(titleInput)
        self.addRow(phoneInput, mobileInput)
        self.addRow(websiteInput)
        self.addRow(commentsInput)
        # -------------------------- #
