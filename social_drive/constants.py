from django.conf import settings

SERVER_ADDRESS = 'http://127.0.0.1:8000'
DROPBOX_RETRUN_URI = SERVER_ADDRESS + '/connect/'
BOX_RETRUN_URI = SERVER_ADDRESS + '/box_retrun_url/'
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
DOPBOX_CONNECT = 'https://www.dropbox.com/oauth2/authorize?client_id=lscra6gncje824j&response_type=token&redirect_uri=http://localhost:8080/'
BOX_CONNECT = 'https://account.box.com/api/oauth2/authorize?response_type=code&client_id=vtqh4e0myek3bpx7t2mdwca19xz6rgb5&redirect_uri=http://localhost:8080/&state=knlLggbUFmO6VMRqKg4nAonHW5ZE1Zaa'
BOX_AUTH_URL = 'https://api.box.com/oauth2/token'
