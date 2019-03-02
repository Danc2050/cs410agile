import pysftp


ERROR_PREFACE = "Error:" 

def create_dir_remote(sftp: pysftp.Connection, remotepath: str):
	try:
		sftp.mkdir(remotepath, mode=755)
		return True

	except OSError as e:
		if e.strerror is None:
			print(ERROR_PREFACE, "could not create directory " + remotepath)
		else:
			print(ERROR_PREFACE, e.strerror)
		return False