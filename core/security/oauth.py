from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request

oauth = OAuth()

def configure_oauth(app):
    oauth.register(
    name='google',
    client_id='TU_CLIENT_ID',
    client_secret='TU_CLIENT_SECRET',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params={'scope': 'openid email profile'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    userinfo_params=None,
    client_kwargs={'scope': 'openid email profile'} 
    )

    app.add_middleware(SessionMiddleware, secret_key="random_key")

async def get_user_info(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)
    return user_info
