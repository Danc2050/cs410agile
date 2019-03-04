from actions.searchLocal import searchLocal
import os
import shutil

def test_search_existing_file():
    flag = searchLocal("test")
    assert flag > 0

def test_search_non_existant_file():
    flag = searchLocal("alkdsjhfasdklfhadshfaldksf")
    assert flag < 1

def test_no_permission_in_current_folder():
    os.mkdir("no_perm")
    os.chdir("no_perm")
    os.mkdir("a folder")
    os.chmod(".", mode=222) # 333 allows write and execute, not read. 111 is very important...it allows us to
    assert searchLocal("a folder") is 0 # the folder is not searchable, so return value should be 0
    os.chdir("..")
    shutil.rmtree("no_perm", True)

def test_no_permission_in_sub_folder():
    os.mkdir("perm")
    os.chdir("perm")
    os.mkdir("perm2")
    os.chdir("perm2")
    os.mkdir("a folder")
    os.chdir("..")
    os.chmod("don't_search", mode=111)
    assert searchLocal("a folder") is 0 # should return false, because no such file exists
    shutil.rmtree("no_permission", True)
