# routers_auth.py
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from templates import get_base_html

# إنشاء راوتر خاص بتسجيل الدخول
router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_page():
    content = """
    <div class="max-w-md mx-auto border border-instaBorder dark:border-instaDarkBorder rounded-xl p-8 bg-white dark:bg-black shadow-sm text-center">
        <h2 class="text-2xl font-bold mb-2">تسجيل الدخول</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mb-8">استخدم حساب جوجل الخاص بك للوصول إلى لوحة التحكم</p>
        
        <a href="/auth/google/login" class="w-full flex items-center justify-center gap-3 border border-gray-300 dark:border-gray-700 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition font-medium">
            <svg class="w-5 h-5" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
            المتابعة باستخدام Google
        </a>
        
        <div class="mt-6 text-xs text-gray-400">
            بتسجيلك الدخول، أنت توافق على <a href="#" class="text-instaBlue hover:underline">شروط الخدمة</a>.
        </div>
    </div>
    """
    return get_base_html("تسجيل الدخول", content)

@router.get("/auth/google/login")
async def dummy_google_login():
    # سيتم ربط هذا المسار بخدمات جوجل قريباً
    return RedirectResponse(url="/dashboard")
