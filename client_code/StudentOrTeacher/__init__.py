from ._anvil_designer import StudentOrTeacherTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

ALLOWED_STUDENT_EMAIL = "@schools.vic.edu.au"
ALLOWED_TEACHER_EMAIL = "@education.vic.gov.au"

class StudentOrTeacher(StudentOrTeacherTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def student_button_click(self, **event_args):
    open_form('StudentSignUp')
    email = self.email_box.text.strip()
    password = self.password_box.text
    try:
      anvil.server.call("student_signup_or_login", email, password)
      alert("Logged in successfully!")
    except Exception as e:
      alert(str(e))

  def teacher_button_click(self, **event_args):
    open_form('TeacherSignUp')
    email = self.email_box.text.strip()
    password = self.password_box.text
    try:
      anvil.server.call("teacher_signup_or_login", email, password)
      alert("Logged in successfully!")
    except Exception as e:
      alert(str(e))
