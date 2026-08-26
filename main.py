import os
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

# استيراد كافة الراوترات
from routers_ui import router as ui_router
from routers_auth import router as auth_router
from routers_admin import router as admin_router
from routers_ai import router as ai_router

app = FastAPI(title="Instapulse AI")

# مفتاح التشفير للجلسات
SECRET_KEY = os.getenv("SECRET_KEY", "instapulse-super-secret-key-2026")
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# ربط جميع الراوترات بالتطبيق
app.include_router(ui_router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(ai_router)
