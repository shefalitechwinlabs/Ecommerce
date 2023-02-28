import pysftp


# Connect to FTP server using SFTP
#  get sftp instance by host, username and key
def connect(host, user, key): 
    try:
        sftp = pysftp.Connection(
            host = host, 
            username = user, 
            private_key = key
        )
        return sftp
    except Exception as e:
        print(e)
    return e
    
def upload_file(sftp, file, path):
    try:
        sftp.put(file, path)
        status = 'File uploaded'
    except Exception as e:
        print(e)
        status = e
    return status

def get_dir(sftp):
    dirs = []
    try:
        dirs = sftp.listdir()
    except Exception as e:
        print(e)
    return dirs
