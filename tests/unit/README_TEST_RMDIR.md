
In CODEOWNERS:

> \ No newline at end of file
+*   @wyat2 @pixieofhugs @edev @shwetapaliwal28
Please revert CODEOWNERS; only Molly, Shweta, and I are supposed to be listed, since we're the reviewers. It's just a GitHub policy setting.
+ Fixed : removed wyat2

In test.py:

> @@ -0,0 +1,91 @@
+from app import controller, login
I'm confused about why you're adding test.py at the root of the repository, with its own main. (I'm also confused about why there appear to be rmdir-specific tests outside the tests/ folder.) If you're not sure how to run our test suite, please talk to me or one of the other group members, and we'll be happy to show you how.
+ Edited : Removed from file from root, placed in /tests/unit/test_rmdir.py

In tests/unit/__init__.py:

> @@ -0,0 +1,2 @@
+__all__ = [
You're absolutely right that it's best practice to add your files to __all__, if it exists, but creating an __init__.py in this directory may cause issues for others, since your definition of __all__ doesn't include everyone else's files as well. (Without an __init__.py, Python seems to search the whole folder; with one, it will only search listed files, so having only one file listed can cause issues if anyone imports *.) Having said that, if you think we should create __init__.py files for our test code, please feel free to raise that as an idea at our next group meeting!
+ Fixed : deleted __init __.py file in tests/unit/

> Update info :  unit test is runable from tests/unit/test_rmdir.py
<br>Unable to use __from__ parent/parent/actions __import__ \*