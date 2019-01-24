#delete folder from server
def delete(sftp, folder): # E.g., folder = 'folder'
    try:
        sftp.remove(folder)
    except Exception as error:
        print("Remove folder error message: " + str(error.args))
    else:
        print("Folder removed successfully")