# Standard Library
import logging

# Application imports
from app.gui.components.form.Form import Form
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.form.PayOptions import PayOptions
from app.gui.components.models.ProfessionListModel import ProfessionListModel
from app.models.Job import Job
from app.utils.EnumUtility import EmploymentType
from app.utils.mixins.Logger import LoggerMixin

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


class JobForm(Form, LoggerMixin):
    def __init__(self, model: Job) -> None:
        super(JobForm, self).__init__("JobInfo", model, "Job Information")
        self.setObjectName("Form:Job")

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Position Title")
        titleInput.setBinding(model, "title")
        titleInput.setPlaceholderText("Job title")

        employmentTypeInput = SelectBox("Employment Type")
        employmentTypeInput.addItems(EmploymentType.AS_LIST())
        employmentTypeInput.setEditable(True)
        employmentTypeInput.setBinding(model, "employment_type")
        employmentTypeInput.setPlaceholderText("Employment Type")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(model, "website")
        websiteInput.setPlaceholderText("www.job-application.com")
        websiteInput.setPrefix("http://")
        # websiteInput.setSuffix(".com")

        professionInput = SelectBox("Profession")
        professionInput.setModel(ProfessionListModel(professionInput))
        professionInput.setEditable(True)
        professionInput.setBinding(model.profession, "profession", "id")
        professionInput.setUpdateBinding(model, "profession_id")
        professionInput.setPlaceholderText("Profession")

        payOptionsInput = PayOptions("Pay Options", model)

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(model, "comments")
        commentsInput.setPlaceholderText("Details about this job...")
        commentsInput.setHeight(2)

        closingDateInput = DateTimeInput("Closing Date")
        closingDateInput.setBinding(model, "closing_date")

        # address_id

        self.addRow(titleInput, closingDateInput)
        self.addRow(employmentTypeInput, columnSpan=2)
        self.addRow(professionInput, columnSpan=2)
        self.addRow(payOptionsInput)
        self.addRow(websiteInput, columnSpan=2)
        self.addRow(commentsInput, columnSpan=2)

        self.modified.connect(self._formModified)
        # -------------------------- #

    def _formModified(self):
        debug("Modified? " + str(self.isModified()))
