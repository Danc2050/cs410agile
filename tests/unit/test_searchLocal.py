from actions.searchLocal import searchLocal
import os


def test_search_existing_file():
    flag = searchLocal("test")
    assert flag > 0


def test_search_non_existant_file():
    flag = searchLocal("alkdsjhfasdklfhadshfaldksf")
    assert flag < 1


def test_no_permission_in_current_folder():
    # create directories
    os.mkdir("no_perm")
    os.chdir("no_perm")
    os.mkdir("a folder")
    os.chmod(".", mode=222) # 222 is write only
    assert searchLocal("a folder") is 0 # the folder is not searchable, so return value should be 0
    # Cleanup
    os.rmdir("a folder")
    os.chdir("..")
    os.rmdir("no_perm")


def test_no_permission_in_sub_folder():
    # create directories
    os.mkdir("perm")
    os.chdir("perm")
    os.mkdir("perm2")
    os.chdir("perm2")
    os.mkdir("a folder")
    os.chdir("..")
    os.chmod("perm2", mode=222)
    os.chdir("..") # We will be in perm folder, searching for "a folder" inside the non-readable perm2 folder
    assert searchLocal("a folder") is 0 # should return false, because we can't search perm2
    # cleanup
    os.chdir("perm")
    os.chdir("perm2")
    os.rmdir("a folder")
    os.chdir("..")
    os.rmdir("perm2")
    os.chdir("..")
    os.rmdir("perm")
