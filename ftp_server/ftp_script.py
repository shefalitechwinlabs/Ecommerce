import ftplib
import argparse

# Connect to FTP server
#  default port will be 21 if port=0
def connect(FTP, host, port=0):
  try:
    FTP.connect(host=host, port=port, timeout=20)
    status = f'Connected to FTP server host - {host}'
    print(status)
  except Exception as e:
    status = f'Exception while connecting to server: {e}'
    print(status)
  return status

# For anonymous login, username and password will be None 
def login(FTP, username=None, password=None):
  try:
    FTP.login(user=username, passwd=password)
    status = 'Login successfully'
    print(status)
  except Exception as e:
    print(f'Exception while server login: {e}')
    status = e
  return status

# Uploading a file default path will be a root folder
#  permissions required for I/O file operations
def upload_file(FTP, filepath, serverpath=''):
  try:
    FTP.encoding = 'utf-8'
    if serverpath:
      FTP.cwd(serverpath)
    with open(filepath, 'rb') as file:
      # Command for Uploading the file "STOR filename"
      FTP.storbinary(f'STOR {filepath}', file)
    status = f'Uploaded {filepath} to server {serverpath}'
    print(status)
  except Exception as e:
    print(f'Exception while uploading file: {e}')
    status = e
  return status

# Connect, authenticate, and upload files to FTP server
def upload_to_ftp(host=None, port=0, username=None,
    password=None, serverpath=None, filepath=None
):
  FTP = ftplib.FTP() # Create FTP server instance
  status = connect(FTP, host, port=port)
  status = login(FTP, username=username, password=password)
  status = upload_file(FTP, filepath, serverpath=serverpath)
  return status

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description = 'Connect and upload files to FTP server'
  )
  parser.add_argument(
    '--host',
    help = 'Please specify the FTP server host.',
    type = str,
    default = 'ftp.dlptest.com',
  )
  parser.add_argument(
    '--port',
    help = 'Please specify the port to connect.',
    type = int,
    default = 0
  )
  parser.add_argument(
    '--username',
    help = 'Ftp username to connect to.',
    type = str,
    default = 'dlpuser'
  )
  parser.add_argument(
    '--password',
    help = 'Password',
    type = str,
    default = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
  )
  parser.add_argument(
    '--serverpath',
    help = 'Enter the server path to upload file to.',
    type = str,
    default = ''
  )
  parser.add_argument(
    '--filepath',
    help = 'Enter the path of the file to upload.',
    type = str,
    default = '__init__.py'
  )
  args = parser.parse_args()

  upload_to_ftp(
    host=args.host, port=args.port,
    username=args.username, password=args.password,
    serverpath=args.serverpath, filepath=args.filepath
  )
