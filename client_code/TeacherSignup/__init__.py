from ._anvil_designer import TeacherSignupTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TeacherSignup(TeacherSignupTemplate):
  def __init__(self, **properties):

    anvil.users.login_with_form()
    print(f"This user has logged in: {anvil.users.get_user()['email']}")
    open_form('TeacherHomePage')