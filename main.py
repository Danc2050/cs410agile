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

    # won't pass test cases for quoted or escaped strings
    tokens = raw_input.split(' ')

    return tokens

# ==============
# SECTION: Tests
# ==============


def test_input_length():
    """Test that read_user_input() returns the correct number of tokens."""

    # To mock standard input for specific values, we'll set module.input
    # to various lambdas that return the string our "user" types.
    # We'll test various edge cases, starting with the simplest: nothing.

    with mock_input("\n"):
        assert len(read_user_input()) == 0

    with mock_input("Hi1234@#$"):
        assert len(read_user_input()) == 1
#
#     # TODO Catch EOFError


# Note: capsys is a pytest fixture that's automatically passed in.
def test_user_prompt(capsys):
    """Test that the user prompt is printed correctly."""

    with mock_input("Any string will do"):
        read_user_input()

    assert capsys.readouterr().out == USER_PROMPT
