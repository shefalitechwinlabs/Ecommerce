# import ftplib
# from ftplib import FTP_TLS
# import socket
# import ssl


# Connect to FTP server using SFTP
#  get sftp instance by host, username and password
# def connect(host, port):
#     try:
#         ftp = ftp.connect(host, port)
#         return ftp
#     except Exception as e:
#         print(e)
#     return e

# def login(ftp, username=None, password=None):
#     ftp.login(username, )
    
# def upload_file(sftp, file, path):
#     try:
#         sftp.put(file, path)
#         status = 'File uploaded'
#     except Exception as e:
#         print(e)
#         status = e
#     return status

# def get_dir(sftp):
#     dirs = []
#     try:
#         dirs = sftp.listdir()
#     except Exception as e:
#         print(e)
#     return dirs

# class tyFTP(FTP_TLS):
#     def __init__(self, host='', user='', acct='', keyfile=None, certfile=None, timeout=60):
#         FTP_TLS.__init__(self, host, user, acct, keyfile, certfile, timeout)
#     def connect(self, host='', port=0, timeout=-999):
#         if host != '':
#             self.host = host
#         if port > 0:
#             self.port = port
#         if timeout != -999:
#             self.timeout = timeout

#         try: 
#             self.sock = socket.create_connection((self.host, self.port), self.timeout)
#             self.af = self.sock.family
#             self.sock = ssl.wrap_socket(self.sock, self.keyfile, self.certfile, ssl_version=ssl.PROTOCOL_TLSv1)
#             self.file = self.sock.makefile('rb')
#             self.welcome = self.getresp()
#         except Exception as e:
#             print (e)
#         return self.welcome
