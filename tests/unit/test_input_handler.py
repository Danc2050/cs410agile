from app.input_handler import read_user_input, DEFAULT_USER_PROMPT
from app import controller
from tests.test_helpers import mock_input


def test_input_length():
    """Test that app.read_user_input() returns the correct number of tokens."""

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
    """Test that read_app.read_user_input() returns the correct tokenizations
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
    # with quotes or backslashes in them), and app.read_user_input()
    # should capture them correctly, but we're not testing for them.
    test_cases = [
        # Case: one-word file name.
        ["First",
            ["First"]],

        # Case: two one-word file names.
        ["Hello, Dolly",
            ["Hello,", "Dolly"]],

        # Case: one escaped-space multi-word file name.
        [r"Filename\ with\ escaped\ spaces",
            [r"Filename with escaped spaces"]],

        # Case: one double-quoted multi-word file name.
        ['"Filename with double quotes"',
            ['Filename with double quotes']],

        # Case: one single-quoted multi-word file name.
        ["'Filename with single quotes'",
            ["Filename with single quotes"]],

        # Case: multi-word filenames, one of each.
        [r'''"File 1.png" 'File 2.png' File\ 3.png''',
            ['File 1.png', "File 2.png", r"File 3.png"]],

        # Case: whitespace.
        ["   file   edit   tools  ",
            ["file", "edit", "tools"]],

        # Cases: escaped quotes.
        [r'\"',
            ['"']],
        [r"\'",
            ["'"]],

        # Cases: escaped quotes in other settings.
        [r"'\'a'",      # '\'a' -> 'a
            ["'a"]],
        [r'"\"a"',      # "\"a" -> "a
            ['"a']],
        [r'''"Hello\" asdf" "what " " and "''',
            ['Hello" asdf', 'what ', ' and ']]
    ]

    for input_string, tokens in test_cases:
        with mock_input(input_string):
            assert read_user_input() == tokens


# Note: capsys is a pytest fixture that's automatically passed in.
def test_user_prompt(capsys):
    """Test that the user prompt is printed correctly."""

    prompt = DEFAULT_USER_PROMPT

    with mock_input("Any string will do"):
        read_user_input(prompt)

    assert capsys.readouterr().out == prompt