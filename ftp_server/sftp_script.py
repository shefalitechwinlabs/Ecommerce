import pysftp


# Connect to FTP server using SFTP
#  get sftp instance by host, username and key
def connect(host, user, key): 
    try:
        sftp = pysftp.Connection(
            host = host, 
            username = user, 
        )
    except Exception as e:
        sftp = e
    return sftp

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

if __name__ == '__main__':
    sftp = connect(
        host = '20.245.98.99', 
        user = 'ubuntu', 
        key = '/Users/admin/Downloads/CAI_Keys/TL/id_rsa_2.pem'
        )
    print(sftp)
    dirs = get_dir(sftp)
    print(dirs)
