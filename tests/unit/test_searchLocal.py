from actions import *

def test_search_existing_file():
    flag = searchLocal("test")
    assert True == flag

def test_search_non_existant_file():
    flag = searchLocal("alkdsjhfasdklfhadshfaldksf")
    assert False == flag