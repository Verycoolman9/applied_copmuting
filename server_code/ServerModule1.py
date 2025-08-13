import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.users import signup_with_email, login_with_email

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
ALLOWED_STUDENT_EMAIL = "@schools.vic.edu.au"
ALLOWED_TEACHER_EMAIL = "@education.vic.gov.au"

@anvil.server.callable
def student_signup_or_login(email, password):
  if not email.lower().endswith(ALLOWED_STUDENT_EMAIL):
    raise Exception(f"Only student emails ending in {ALLOWED_STUDENT_EMAIL} are allowed.")
  try:
    return login_with_email(email, password)
  except:
    return signup_with_email(email, password)

@anvil.server.callable
def teacher_signup_or_login(email, password):
  if not email.lower().endswith(ALLOWED_TEACHER_EMAIL):
    raise Exception(f"Only teacher emails ending in {ALLOWED_TEACHER_EMAIL} are allowed.")
  try:
    return login_with_email(email, password)
  except:
    return signup_with_email(email, password)
