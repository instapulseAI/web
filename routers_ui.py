# routers_ui.py
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from templates import get_base_html

# إنشاء راوتر خاص بصفحات الواجهة
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def landing_page():
    content = """
    <div class="text-center py-12 md:py-24">
        <h1 class="text-4xl md:text-6xl font-bold mb-6">أدر حساب إنستغرام الخاص بك <br> بذكاء واحترافية</h1>
        <p class="text-lg md:text-xl text-gray-500 dark:text-gray-400 mb-10 max-w-2xl mx-auto">
            منصة متكاملة لتحليل تفاعل الزبائن، إدارة المحتوى، وزيادة مبيعاتك. لا حاجة لبطاقة ائتمان للبدء.
        </p>
        <div class="flex flex-col md:flex-row gap-4 justify-center">
            <a href="/login" class="bg-instaBlue text-white px-8 py-3 rounded-xl font-bold text-lg hover:bg-blue-600 transition shadow-lg">
                ابدأ الآن مجاناً عبر جوجل
            </a>
            <a href="/pricing" class="bg-white dark:bg-black text-black dark:text-white border border-gray-300 dark:border-gray-700 px-8 py-3 rounded-xl font-bold text-lg hover:bg-gray-50 transition">
                اطلع على الأسعار
            </a>
        </div>
    </div>
    """
    return get_base_html("الرئيسية", content)

@router.get("/pricing", response_class=HTMLResponse)
async def pricing_page():
    content = """
    <div class="text-center mb-12">
        <h2 class="text-3xl font-bold mb-4">خطط تناسب طموحك</h2>
    </div>
    <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
        <!-- خطة مجانية -->
        <div class="border border-instaBorder rounded-2xl p-8 bg-white dark:bg-black flex flex-col">
            <h3 class="text-xl font-bold text-gray-500 mb-2">التجربة المجانية</h3>
            <div class="text-4xl font-bold mb-4">مجاناً <span class="text-sm text-gray-400">/ 7 أيام</span></div>
            <a href="/login" class="mt-auto w-full block text-center border border-instaBlue text-instaBlue font-bold py-2 rounded-lg">ابدأ التجربة</a>
        </div>
        <!-- خطة شهرية -->
        <div class="border-2 border-instaBlue rounded-2xl p-8 bg-white dark:bg-black relative shadow-xl flex flex-col transform md:-translate-y-4">
            <h3 class="text-xl font-bold text-instaBlue mb-2">الاشتراك الشهري</h3>
            <div class="text-4xl font-bold mb-4">$6 <span class="text-sm text-gray-400">/ شهرياً</span></div>
            <a href="/login" class="mt-auto w-full block text-center bg-instaBlue text-white font-bold py-2 rounded-lg">اشترك الآن</a>
        </div>
        <!-- خطة سنوية -->
        <div class="border border-instaBorder rounded-2xl p-8 bg-white dark:bg-black flex flex-col">
            <h3 class="text-xl font-bold text-gray-500 mb-2">الاشتراك السنوي</h3>
            <div class="text-4xl font-bold mb-4">$70 <span class="text-sm text-gray-400">/ سنوياً</span></div>
            <a href="/login" class="mt-auto w-full block text-center border border-gray-300 text-black dark:text-white font-bold py-2 rounded-lg">اشترك الآن</a>
        </div>
    </div>
    """
    return get_base_html("الأسعار", content)

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page():
    content = """
    <div class="bg-white dark:bg-black border border-instaBorder rounded-xl p-8 text-center">
        <h2 class="text-2xl font-bold mb-4">لوحة التحكم</h2>
        <p class="mb-4">لم تقم بربط حساب إنستغرام بعد.</p>
        <button class="bg-instaBlue text-white px-6 py-2 rounded-lg font-medium">+ ربط حساب إنستغرام</button>
    </div>
    """
    return get_base_html("لوحة التحكم", content)
