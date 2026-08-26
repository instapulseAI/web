import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

router = APIRouter(prefix="/auth", tags=["Authentication"])

# قراءة المتغيرات البيئية من Railway
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI", "https://instapulseai.up.railway.app/auth/google/callback")

# إعداد الـ OAuth وتأمين قراءة بيانات Google
config_data = {}
if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    config_data = {
        "GOOGLE_CLIENT_ID": GOOGLE_CLIENT_ID,
        "GOOGLE_CLIENT_SECRET": GOOGLE_CLIENT_SECRET
    }

config = Config(environ=config_data)
oauth = OAuth(config)

oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@router.get("/login/google")
async def login_google(request: Request):
    """توجيه المستخدم لصفحة دخول جوجل"""
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        raise HTTPException(
            status_code=500, 
            detail="Google OAuth Credentials list is missing in Railway environment variables."
        )
    return await oauth.google.authorize_redirect(request, REDIRECT_URI)

@router.get("/google/callback")
async def auth_google_callback(request: Request):
    """استلام استجابة جوجل وحفظ البيانات في الجلسة"""
    try:
        token = await oauth.google.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Authentication failed: {str(e)}")
    
    user_info = token.get('userinfo')
    if user_info:
        request.session['user'] = {
            "name": user_info.get("name"),
            "email": user_info.get("email"),
            "picture": user_info.get("picture")
        }
    
    # تحويل المستخدم بعد النجاح لـ Dashboard
    return RedirectResponse(url="/dashboard", status_code=303)

@router.get("/logout")
async def logout(request: Request):
    """مسح الجلسة وتسجيل الخروج"""
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)
