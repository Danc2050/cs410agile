import pysftp


ERROR_PREFACE = "Error:" 

def remove_dir_remote(sftp: pysftp.Connection, remotepath: str):
	try:
		sftp.rmdir(remotepath)
		return True

	except OSError as e:
		if e.strerror is None:
			print(ERROR_PREFACE, "could not remove directory " + remotepath)
		else:
			print(ERROR_PREFACE, e.strerror)
		return False