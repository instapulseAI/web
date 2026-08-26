import os
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

# تهيئة التطبيق
app = FastAPI(
    title="Instapulse AI",
    description="Professional Instagram Management Platform",
    version="1.0.0"
)

# -----------------------------------------------------------------------------
# 1. تصميم الواجهة (HTML/CSS) - أسلوب مشابه لإنستغرام (نظيف، أبيض وأسود، وضع ليلي)
# استخدمنا مكتبة TailwindCSS عبر الـ CDN لبناء تصميم احترافي وسريع
# -----------------------------------------------------------------------------

def get_base_html(title: str, content: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl" class="light">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | Instapulse AI</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            tailwind.config = {{
                darkMode: 'media', // يتفاعل مع الوضع الليلي لجهاز المستخدم تلقائياً
                theme: {{
                    extend: {{
                        colors: {{
                            instaBlue: '#0095f6',
                            instaDark: '#121212',
                            instaBorder: '#dbdbdb',
                            instaDarkBorder: '#262626'
                        }}
                    }}
                }}
            }}
        </script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
            body {{ font-family: 'Tajawal', sans-serif; transition: background-color 0.3s, color 0.3s; }}
        </style>
    </head>
    <body class="bg-gray-50 text-gray-900 dark:bg-instaDark dark:text-white min-h-screen flex flex-col">
        
        <!-- الشريط العلوي (Navbar) -->
        <nav class="bg-white dark:bg-black border-b border-instaBorder dark:border-instaDarkBorder sticky top-0 z-50">
            <div class="max-w-5xl mx-auto px-4 py-3 flex justify-between items-center">
                <a href="/" class="text-xl font-bold tracking-wider">Instapulse<span class="text-instaBlue">AI</span></a>
                <div class="flex gap-4 items-center">
                    <a href="/pricing" class="text-sm font-medium hover:text-gray-500 transition">الأسعار</a>
                    <a href="/login" class="bg-instaBlue hover:bg-blue-600 text-white px-4 py-1.5 rounded-lg text-sm font-medium transition shadow-sm">
                        تسجيل الدخول
                    </a>
                </div>
            </div>
        </nav>

        <!-- محتوى الصفحة -->
        <main class="flex-grow flex items-center justify-center p-4">
            <div class="w-full max-w-5xl">
                {content}
            </div>
        </main>

        <!-- الفوتر -->
        <footer class="text-center py-6 text-xs text-gray-400 dark:text-gray-500 border-t border-instaBorder dark:border-instaDarkBorder">
            &copy; 2026 Instapulse AI. جميع الحقوق محفوظة.
        </footer>
    </body>
    </html>
    """

# -----------------------------------------------------------------------------
# 2. مسارات الصفحات (Routes)
# -----------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def landing_page():
    content = """
    <div class="text-center py-12 md:py-24">
        <h1 class="text-4xl md:text-6xl font-bold mb-6">أدر حساب إنستغرام الخاص بك <br> بذكاء واحترافية</h1>
        <p class="text-lg md:text-xl text-gray-500 dark:text-gray-400 mb-10 max-w-2xl mx-auto">
            منصة متكاملة لتحليل تفاعل الزبائن، إدارة المحتوى، وزيادة مبيعاتك. لا حاجة لبطاقة ائتمان للبدء.
        </p>
        <div class="flex flex-col md:flex-row gap-4 justify-center">
            <a href="/login" class="bg-instaBlue text-white px-8 py-3 rounded-xl font-bold text-lg hover:bg-blue-600 transition shadow-lg flex items-center justify-center gap-2">
                <svg class="w-5 h-5 bg-white rounded-full p-0.5" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
                ابدأ الآن مجاناً عبر جوجل
            </a>
            <a href="/pricing" class="bg-white dark:bg-black text-black dark:text-white border border-gray-300 dark:border-gray-700 px-8 py-3 rounded-xl font-bold text-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition">
                اطلع على الأسعار
            </a>
        </div>
    </div>
    """
    return get_base_html("الرئيسية", content)


@app.get("/pricing", response_class=HTMLResponse)
async def pricing_page():
    content = """
    <div class="text-center mb-12">
        <h2 class="text-3xl font-bold mb-4">خطط تناسب طموحك</h2>
        <p class="text-gray-500 dark:text-gray-400">اختر الباقة التي تناسب عملك. يمكنك الإلغاء في أي وقت.</p>
    </div>
    <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
        
        <!-- الباقة المجانية -->
        <div class="border border-instaBorder dark:border-instaDarkBorder rounded-2xl p-8 bg-white dark:bg-black flex flex-col">
            <h3 class="text-xl font-bold text-gray-500 mb-2">التجربة المجانية</h3>
            <div class="text-4xl font-bold mb-4">مجاناً <span class="text-sm font-normal text-gray-400">/ 7 أيام</span></div>
            <ul class="text-right space-y-3 mb-8 flex-grow text-sm">
                <li>✅ لا حاجة لبطاقة ائتمان</li>
                <li>✅ ربط حساب إنستغرام واحد</li>
                <li>✅ تحليلات أساسية</li>
            </ul>
            <a href="/login" class="w-full block text-center border border-instaBlue text-instaBlue font-bold py-2 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900/20 transition">ابدأ التجربة</a>
        </div>

        <!-- الباقة الشهرية -->
        <div class="border-2 border-instaBlue rounded-2xl p-8 bg-white dark:bg-black relative shadow-xl flex flex-col transform md:-translate-y-4">
            <div class="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-instaBlue text-white px-3 py-1 rounded-full text-xs font-bold">الأكثر طلباً</div>
            <h3 class="text-xl font-bold text-instaBlue mb-2">الاشتراك الشهري</h3>
            <div class="text-4xl font-bold mb-4">$6 <span class="text-sm font-normal text-gray-400">/ شهرياً</span></div>
            <ul class="text-right space-y-3 mb-8 flex-grow text-sm">
                <li>✅ كافة ميزات التجربة المجانية</li>
                <li>✅ ربط حسابات متعددة</li>
                <li>✅ تحليلات متقدمة والرد الذكي</li>
                <li>✅ دعم فني ذو أولوية</li>
            </ul>
            <a href="/login" class="w-full block text-center bg-instaBlue text-white font-bold py-2 rounded-lg hover:bg-blue-600 transition shadow-md">اشترك الآن</a>
        </div>

        <!-- الباقة السنوية -->
        <div class="border border-instaBorder dark:border-instaDarkBorder rounded-2xl p-8 bg-white dark:bg-black flex flex-col">
            <h3 class="text-xl font-bold text-gray-500 mb-2">الاشتراك السنوي</h3>
            <div class="text-4xl font-bold mb-2">$70 <span class="text-sm font-normal text-gray-400">/ سنوياً</span></div>
            <div class="text-xs text-green-500 font-bold mb-4">وفر أكثر من 15% </div>
            <ul class="text-right space-y-3 mb-8 flex-grow text-sm">
                <li>✅ جميع ميزات الباقة الشهرية</li>
                <li>✅ تقارير أداء مخصصة للشركات</li>
                <li>✅ مدير حساب مخصص</li>
            </ul>
            <a href="/login" class="w-full block text-center border border-gray-300 dark:border-gray-700 text-black dark:text-white font-bold py-2 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition">اشترك الآن</a>
        </div>
    </div>
    """
    return get_base_html("الأسعار", content)


@app.get("/login", response_class=HTMLResponse)
async def login_page():
    content = """
    <div class="max-w-md mx-auto border border-instaBorder dark:border-instaDarkBorder rounded-xl p-8 bg-white dark:bg-black shadow-sm text-center">
        <h2 class="text-2xl font-bold mb-2">تسجيل الدخول</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mb-8">استخدم حساب جوجل الخاص بك للوصول إلى لوحة التحكم</p>
        
        <!-- زر تسجيل الدخول الوهمي (سيتم ربطه بـ Authlib لاحقاً) -->
        <a href="/auth/google/login" class="w-full flex items-center justify-center gap-3 border border-gray-300 dark:border-gray-700 py-2.5 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition font-medium">
            <svg class="w-5 h-5" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
            المتابعة باستخدام Google
        </a>
        
        <div class="mt-6 text-xs text-gray-400">
            بتسجيلك الدخول، أنت توافق على <a href="#" class="text-instaBlue hover:underline">شروط الخدمة</a> و <a href="#" class="text-instaBlue hover:underline">سياسة الخصوصية</a>.
        </div>
    </div>
    """
    return get_base_html("تسجيل الدخول", content)

# -----------------------------------------------------------------------------
# 3. مسارات خلفية (Backend Logic Preparations)
# هنا سنقوم لاحقاً بإضافة أكواد قاعدة البيانات الحقيقية والـ OAuth
# -----------------------------------------------------------------------------

@app.get("/auth/google/login")
async def dummy_google_login():
    # هذا المسار حالياً وهمي، سنقوم في الخطوة القادمة ببرمجة نظام OAuth الحقيقي
    # وسيحتاج لتنزيل مكتبات (authlib, httpx) وإعداد Google Cloud Console.
    return RedirectResponse(url="/dashboard")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page():
    # هذه لوحة التحكم التي تظهر بعد تسجيل الدخول
    content = """
    <div class="bg-white dark:bg-black border border-instaBorder dark:border-instaDarkBorder rounded-xl p-8">
        <div class="flex justify-between items-center mb-8 border-b border-gray-100 dark:border-gray-800 pb-4">
            <h2 class="text-2xl font-bold">لوحة التحكم</h2>
            <span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1">
                <span class="w-2 h-2 rounded-full bg-green-500"></span>
                حالة الاشتراك: تجربة مجانية فعالة
            </span>
        </div>
        
        <div class="text-center py-10">
            <div class="w-20 h-20 bg-gray-100 dark:bg-gray-800 rounded-full mx-auto flex items-center justify-center mb-4">
                <svg class="w-10 h-10 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
            </div>
            <h3 class="text-lg font-bold mb-2">لم تقم بربط حساب إنستغرام بعد</h3>
            <p class="text-gray-500 text-sm mb-6 max-w-md mx-auto">للبدء في تحليل البيانات وإدارة التفاعلات، يرجى ربط حساب إنستغرام الخاص بك.</p>
            <button class="bg-instaBlue text-white px-6 py-2 rounded-lg font-medium hover:bg-blue-600 transition">
                + ربط حساب إنستغرام
            </button>
        </div>
    </div>
    """
    return get_base_html("لوحة التحكم", content)
