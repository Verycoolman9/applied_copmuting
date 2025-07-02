from ._anvil_designer import SignUpPageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class SignUpPage(SignUpPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()
    print(f"This user has logged in: {anvil.users.get_user()['email']}")