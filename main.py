# main.py
from fastapi import FastAPI

# استيراد الملفات التي قمنا بإنشائها
import routers_ui
import routers_auth

# تهيئة التطبيق
app = FastAPI(
    title="Instapulse AI",
    description="Professional Instagram Management Platform",
    version="1.0.0"
)

# ربط الملفات بالتطبيق الرئيسي
app.include_router(routers_ui.router)
app.include_router(routers_auth.router)
