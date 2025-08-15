from ._anvil_designer import StudentOrTeacherTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StudentOrTeacher(StudentOrTeacherTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def student_button_click(self, **event_args):
    open_form('StudentSignup')
    
  def teacher_button_click(self, **event_args):
    open_form('TeacherSignup')
  