from app.gui.components.form.Form import Form
from app.gui.components.form.inputs.DateTimeInput import DateTimeInput
from app.gui.components.form.inputs.SelectBox import SelectBox
from app.gui.components.form.inputs.TextAreaInput import TextAreaInput
from app.gui.components.form.inputs.TextInput import TextInput
from app.models import Job

from app.models.Profession import Profession


class JobForm(Form):
    def __init__(self, model: Job) -> None:
        super(JobForm, self).__init__("JobInfo", model, "Job Information")

        # -------------------------- #
        # -- insert form elements -- #

        titleInput = TextInput("Title")
        titleInput.setBinding(self._model, "title")
        titleInput.setPlaceholderText("Job title")

        websiteInput = TextInput("Website")
        websiteInput.setBinding(self._model, "website")
        websiteInput.setPlaceholderText("www.job-application.com")

        professionInput = SelectBox("Profession")
        professionInput.addItems(sorted([p.profession for p in Profession.get().all()]))
        professionInput.setEditable(True)
        professionInput.setBinding(self._model.profession, "profession")
        professionInput.setPlaceholderText("Profession")

        commentsInput = TextAreaInput("Comments")
        commentsInput.setBinding(self._model, "comments")
        commentsInput.setPlaceholderText("Details about this job...")

        closingDateInput = DateTimeInput("Closing Date")
        closingDateInput.setBinding(self._model, "closing_date")

        # salary / rate/rate_unit
        # employment_type
        # address_id

        self.addRow(titleInput, closingDateInput)
        self.addRow(professionInput)
        self.addRow(websiteInput)
        self.addRow(professionInput)
        self.addRow(commentsInput)
        # -------------------------- #
