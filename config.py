import os

class Config:
    # ...
    STEAM_OAUTH_CLIENT_ID = os.environ.get('STEAM_OAUTH_CLIENT_ID')
    STEAM_OAUTH_CLIENT_SECRET = os.environ.get('STEAM_OAUTH_CLIENT_SECRET')
    STEAM_OAUTH_REDIRECT_URI = 'http://localhost:5000/login/steam/authorized'