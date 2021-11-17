from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication


credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)