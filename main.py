import pysftp
import re
from test_helpers import mock_input

# =========================
# SECTION: Global constants
# =========================

# The text displayed when a user is prompted for input.
USER_PROMPT = "sftp>"

# TODO Delete this stub main.
if __name__ == "__main__":
    with mock_input(" \n"):
        string = input("Type here:")
        print(string, len(string))

# ======================
# SECTION: Input handler
# ======================


def read_user_input():
    raw_input = input(USER_PROMPT)

    # Before breaking up into tokens, let's handle the edge case of empty
    # strings, since that can be hard to properly tokenize to an empty list.
    if raw_input == '':
        return []

    # Regex pattern to match any filenames as single tokens. We don't check
    # for illegal characters; we just tokenize in a way that recognizes
    # escaped spaces and single/double quotes.
    #
    # Pattern in detail:
    # ".+" matches double-quoted strings
    # '.+' matches single-quoted strings
    # (?:\\ |\S)+ matches strings with escaped spaces.
    #   (Note: \S must come after "\\ " or \S will match the slash
    #   and "\\ " won't match!)
    pattern = r'''".+"|'.+'|(?:\\ |\S)+'''
    tokens = re.findall(pattern, raw_input)

    return tokens


# ===================
# SECTION: Controller
# ===================


def main_loop(sftp: pysftp.Connection):
    """Main controller loop. Asks the user for input, attempts to decipher
    user input, and invoke the appropriate actions with the desired arguments.
    """

    return

# ==============
# SECTION: Tests
# ==============


def test_input_length():
    """Test that read_user_input() returns the correct number of tokens."""

    # To mock standard input for specific values, we'll set module.input
    # to various lambdas that return the string our "user" types.
    # We'll test various edge cases, starting with the simplest: nothing.

    # Capture empty user input. Oddly, we have to pass "\n" rather than
    # "" or input() will see EOF and throw an exception (as though the
    # user had pressed Ctrl-D, which is a different test case).
    with mock_input("\n"):
        assert len(read_user_input()) == 0

    # One-word input
    with mock_input("Hi1234@#$"):
        assert len(read_user_input()) == 1

    # Multi-word input
    with mock_input("A B C 3 #"):
        assert len(read_user_input()) == 5


def test_correct_tokenization():
    """Test that read_read_user_input() returns the correct tokenizations
    for both simple and complex input cases.
    """

    # In order to reduce redundancy and make it easier to add test cases,
    # we'll define our test cases as a list, and we'll run each list item
    # as a test case.
    #
    # test_cases: a list of test cases. Each test case has the format:
    #   [input string, correct tokenization]
    #
    # Note that there are lots of crazy, wacky corner cases involving
    # file names that no one should ever really use (e.g. file names
    # with quotes or backslashes in them), and read_user_input()
    # should capture them correctly, but we're not testing for them.
    test_cases = [
        # Case: one-word file name.
        ["First", ["First"]],

        # Case: two one-word file names.
        ["Hello, Dolly", ["Hello,", "Dolly"]],

        # Case: one escaped-space multi-word file name.
        [r"Filename\ with\ escaped\ spaces",
            [r"Filename\ with\ escaped\ spaces"]],

        # Case: one double-quoted multi-word file name.
        ['"Filename with double quotes"',
            ['"Filename with double quotes"']],

        # Case: one single-quoted multi-word file name.
        ["'Filename with single quotes'",
            ["'Filename with single quotes'"]],

        # Case: multi-word filenames, one of each.
        [r'''"File 1.png" 'File 2.png' File\ 3.png''',
            ['"File 1.png"', "'File 2.png'", r"File\ 3.png"]]
    ]

    for input_string, tokens in test_cases:
        with mock_input(input_string):
            assert read_user_input() == tokens

# TODO Catch EOFError in controller.


# Note: capsys is a pytest fixture that's automatically passed in.
def test_user_prompt(capsys):
    """Test that the user prompt is printed correctly."""

    with mock_input("Any string will do"):
        read_user_input()

    assert capsys.readouterr().out == USER_PROMPT
