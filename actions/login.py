import pysftp
from tests import test_server

#Connect to Server
def login(HOST, USERNAME, PASSWORD):
    """Processes the login request specified. Note that pysftp handles
      all edge cases neatly, raising well-documented exceptions if any problems are found
      (e.g., Invalid hostname, username, password, etc.).
      """
    return pysftp.Connection(host=HOST, username=USERNAME, password=PASSWORD)