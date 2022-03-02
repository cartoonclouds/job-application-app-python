from app.gui.components.form.Form import Form
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.gui.components.models.ProfessionListModel import ProfessionListModel
from app.models import Job
from PySide6.QtWidgets import QComboBox

from app.models.Profession import Profession


class JobForm(Form):
    def __init__(self, model: Job) -> None:
        super(JobForm, self).__init__("JobInfo", model, "Job Information")

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Title")
        titleInput.setBinding(model, "title")
        titleInput.setPlaceholderText("Job title")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(model, "website")
        websiteInput.setPlaceholderText("www.job-application.com")

        professionInput = SelectBox("Profession")
        professionInput.setModel(ProfessionListModel(professionInput))
        professionInput.setEditable(True)
        professionInput.setBinding(model.profession, "profession", "id")
        professionInput.setPlaceholderText("Profession")

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(model, "comments")
        commentsInput.setPlaceholderText("Details about this job...")

        closingDateInput = DateTimeInput("Closing Date")
        closingDateInput.setBinding(model, "closing_date")

        # salary / rate/rate_unit
        # employment_type
        # address_id

        self.addRow(titleInput, closingDateInput)
        self.addRow(professionInput)
        self.addRow(websiteInput)
        self.addRow(professionInput)
        self.addRow(commentsInput, 1, 2)
        # -------------------------- #
