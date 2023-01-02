from google_code import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'credentials.json'
API_VERSION = 'drive'
API_NAME = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_VERSION, API_NAME, SCOPES)

#CREATE/UPLOAD FILE
path = '/Users/techwin/Downloads/{0}'
file_names = ['fashion.jpeg']
mime_type = ['application/']

for file_name, mime_type in zip(file_names, mime_type):
    metadata = {
        'name': file_name,
        'mimeType': mime_type,
    }
    media = MediaFileUpload(path.format(file_name), mimetype=mime_type)
    service.files().create(
        body = metadata,
        media_body = media,
        fields = 'id'
    ).execute()
    