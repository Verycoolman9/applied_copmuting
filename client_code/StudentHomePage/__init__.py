from ._anvil_designer import StudentHomePageTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StudentHomePage(StudentHomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def time_table_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('StudentHomePage.StudentTimeTablePage')

  def account_information_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('StudentHomePage.StudentAccountInformation')

  def dashboard_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('StudentHomePage.StudentDashboard')

  def points_tally_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('StudentHomePage.StudentPointsTally')

  def event_signup_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('StudentHomePage.StudentEventSignup')

  def chats_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('StudentHomePage.StudentChatPage')
