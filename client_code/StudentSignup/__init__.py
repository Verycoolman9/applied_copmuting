from ._anvil_designer import StudentSignupTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.users import login_with_email, signup_with_email


ALLOWED_DOMAIN = "@schools.vic.edu.au"


class StudentSignup(StudentSignupTemplate):
  def __init__(self, **properties):

    anvil.users.login_with_form()
    print(f"This user has logged in: {anvil.users.get_user()['email']}")
    open_form('StudentHomePage')

@anvil.server
def restricted_signup(email, password):
  if not email.lower().endswith(ALLOWED_DOMAIN):
    raise Exception(f"Only emails ending in {ALLOWED_DOMAIN} are allowed.")
  return signup_with_email(email, password)

@anvil.server
def restricted_login(email, password):
  if not email.lower().endswith(ALLOWED_DOMAIN):
   raise Exception(f"Only emails ending in {ALLOWED_DOMAIN} are allowed.")
  return login_with_email(email, password)