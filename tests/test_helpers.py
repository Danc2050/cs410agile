from contextlib import contextmanager
from io import StringIO
import pytest
import sys


# Modified from:
# https://stackoverflow.com/questions/35851323/pytest-how-to-test-a-function-with-input-call/36377194
@contextmanager
def mock_input(user_input: str):
    """When used with "with mock_input(mystring):", replaces stdin with
    mystring to simulate user input (i.e. to mock stdin).
    """

    # Save original stdin and replace it with a StringIO stream handler.
    orig = sys.stdin
    mock = StringIO(user_input)
    sys.stdin = mock

    # Yield to program execution.
    yield

    # Teardown after context scope ends.
    sys.stdin = orig
    mock.close()
