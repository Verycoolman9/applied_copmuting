from ._anvil_designer import StudentSignupTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class StudentSignup(StudentSignupTemplate):
  def __init__(self, **properties):

    anvil.users.login_with_form()
    print(f"This user has logged in: {anvil.users.get_user()['email']}")
    open_form('StudentHomePage')