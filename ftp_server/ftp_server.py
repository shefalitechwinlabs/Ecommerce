import logging

from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler

authorizer = DummyAuthorizer()
authorizer.add_user("test", "test", ".", perm="elradfmwMT")
authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
authorizer.add_anonymous(".", perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer


address = ('20.245.98.99', 2121)
server = FTPServer(('20.245.98.99', 2121), handler)
logging.basicConfig(filename='/ftp_server/pyftpd.log', level=logging.INFO)
address = ('', 2121)
server = FTPServer(('', 2121), handler)
server.serve_forever()
