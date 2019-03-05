import pysftp


# Connect to Server
def login(host, username, password):
    """Processes the login request specified. Note that pysftp handles
      all edge cases neatly, raising well-documented exceptions if any problems are found
      (e.g., Invalid hostname, username, password, etc.).
      """
    return pysftp.Connection(host=host, username=username, password=password)


