from actions.searchLocal import searchLocal

def test_search_existing_file():
    flag = searchLocal("test")
    assert flag > 0

def test_search_non_existant_file():
    flag = searchLocal("alkdsjhfasdklfhadshfaldksf")
    assert flag < 1
