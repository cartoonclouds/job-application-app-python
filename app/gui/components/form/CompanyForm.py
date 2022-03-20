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
        self.setObjectName("Form:Company")

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Name")
        titleInput.setBinding(self._model, "name")
        titleInput.setPlaceholderText("Company name")

        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QCompleter.html
        titleInput.setCompleter(QCompleter(list(Company.all().pluck("name"))))

        phoneInput = TextInput("Phone")
        phoneInput.setBinding(self._model, "phone")
        phoneInput.setPlaceholderText("Company phone number")
        # on completer.activated.connect(update other fields)
        # https://www.stylemanual.gov.au/grammar-punctuation-and-conventions/numbers-and-measurements/telephone-numbers
        # https://developers.google.com/style/phone-numbers
        # https://uxplanet.org/phone-number-field-design-best-practices-23957cbd86d5
        # https://stackoverflow.com/questions/26868803/australian-phone-number-validation
        # https://uxmovement.com/forms/bad-practices-on-phone-number-form-fields/
        phoneInput.setInputMask("(99) 9999 9999")

        mobileInput = TextInput("Mobile")
        mobileInput.setBinding(self._model, "mobile")
        mobileInput.setPlaceholderText("Company mobile number")
        mobileInput.setPrefix("+61 ")
        mobileInput.setInputMask("999 999 999")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(self._model, "website")
        websiteInput.setPlaceholderText("www.job-application.com")
        websiteInput.setPrefix("www")

        # address
        addressLine1Input = TextInput("Address 1")
        addressLine1Input.setBinding(self._model.address, "address_line_1")

        addressLine2Input = TextInput("Address 2")
        addressLine2Input.setBinding(self._model.address, "address_line_2")

        suburbInput = TextInput("Suburb")
        suburbInput.setBinding(self._model.address, "suburb")
        
        cityInput = TextInput("City")
        cityInput.setBinding(self._model.address, "city")
        
        stateInput = TextInput("State")
        stateInput.setBinding(self._model.address, "state")
        
        postcodeInput = TextInput("Postcode")
        postcodeInput.setBinding(self._model.address, "postcode")
        postcodeInput.setInputMask("9999")

        # Country - pyside provides country list

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(self._model, "comments")
        commentsInput.setPlaceholderText("Details about this job...")
        commentsInput.setHeight(2)

        self.addRow(titleInput)
        self.addRow(phoneInput, mobileInput)
        self.addRow(websiteInput)
        self.addRow(commentsInput)
        # -------------------------- #
