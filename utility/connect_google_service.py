from django.conf import settings
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from googleapiclient.discovery import build
from homepage.models import CredentialsModel
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import GoogleCredentials
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from oauth2client.service_account import ServiceAccountCredentials

import httplib2 
import os 

CLIENT_SECRETS = settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON
SERVICE_ACCOUNT_FILE = settings.SERVICE_ACCOUNT_FILE 
REDIRECT_URI = 'https://kaihunghuang.info/oauth2/oauth2callback'
    
# Google service scope 
SCOPE_ANALYTICS = ['https://www.googleapis.com/auth/analytics.readonly']

# Google service api name 
API_ANALYTICS = 'analytics'

class ConnectGoogleService:
    def __init__(self, name, scope, version):
        self.scope = scope 
        self.name = name 
        self.version = version 
        self.flow = flow_from_clientsecrets(CLIENT_SECRETS, scope, REDIRECT_URI)

    def get_google_service(self):
        """Get a service that communicates to a Google API.
        Args:
            name: string The name of the api to connect to.
            version: string The api version to connect to.
            scope: A list of strings representing the auth scopes to authorize for theconnection.
            client_secrets_path: string A path to a valid client secrets file.
        Returns:
            A service that is connected to the specified API.
        """
        #storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
        #credential = storage.get()
        #if credential is None or credential.invalid == True:
        #    self.flow.param

        credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, self.scope)
        http = credentials.authorize(httplib2.Http(disable_ssl_certificate_validation=True))
        service = build(self.name, self.version, http=http)
        return service


