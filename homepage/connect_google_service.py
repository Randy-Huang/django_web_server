from django.conf import settings
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials

import os 

class connect_google_service:
    # Google analytics service 
    SCOPE = ['https://www.googleapis.com/auth/analytics.readonly'] 
    CLIENT_SECRETS = os.path.join(settings.STATIC_ROOT, 'google/', 'client_secrets.json')

    def __init__(self, name, version):
        self.scope = SCOPE
        self.key_file = CLIENT_SECRETS 
        self.service = None 
        self.name = None
        self.version = None 

    def get_google_service(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.CLIENT_SECRETS, self.SCOPE)
        http = credentials.authorize(httplib2.Http(disable_ssl_certificate_validation=True))
        service = build(self.name, self.version, http=http)
        return service


