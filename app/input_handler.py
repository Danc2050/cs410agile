import re

# ==================
# SECTION: Constants
# ==================

# The text displayed when a user is prompted for input.
DEFAULT_USER_PROMPT = "sftp> "


def read_user_input(prompt=DEFAULT_USER_PROMPT):
    """User input handler. May raise EOFError if stdin is closed, e.g.
    by a user pressing Ctrl-D."""
    raw_input = input(prompt)

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


