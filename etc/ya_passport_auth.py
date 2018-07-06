import os


c.JupyterHub.authenticator_class = 'everware.YandexPassportOAuthenticator'
c.YandexPassportOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.YandexPassportOAuthenticator.client_id = os.environ['YA_PASSPORT_CLIENT_ID']
c.YandexPassportOAuthenticator.client_secret = os.environ['YA_PASSPORT_CLIENT_SECRET']
