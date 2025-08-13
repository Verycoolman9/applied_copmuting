from ._anvil_designer import StudentOrTeacherTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

ALLOWED_STUDENT_EMAIL = "@schools.vic.edu.au"
ALLOWED_TEACHER_EMAIL = "@education.vic.gov.au"

class StudentOrTeacher(StudentOrTeacherTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def student_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    if ALLOWED_STUDENT_EMAIL is not ALLOWED_STUDENT_EMAIL.endswith("@schools.vic.edu.au"):
      alert("Please use student Email when signing up or logging in :)")

  def teacher_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    if ALLOWED_TEACHER_EMAIL is not ALLOWED_TEACHER_EMAIL.endswith("@education.vic.edu.au"):
      alert("Please use teacher email when signing up or logging in")
