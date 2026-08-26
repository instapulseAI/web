from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from templates import layout

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """الصفحة الرئيسية للموقع"""
    user = request.session.get("user")
    
    content = """
    <section class="py-20 text-center space-y-6">
        <h1 class="text-5xl font-extrabold tracking-tight">إدارة إنستغرام أسهل مع <span class="text-blue-500">Instapulse AI</span></h1>
        <p class="text-xl text-slate-400 max-w-2xl mx-auto">منصتك الذكية لأتمتة المنشورات، تحسين التفاعل، وتوليد أفكار المحتوى بالذكاء الاصطناعي.</p>
        <div class="pt-4">
            <a href="/auth/login/google" class="bg-blue-600 hover:bg-blue-700 text-white text-lg font-semibold px-8 py-3 rounded-xl transition shadow-lg shadow-blue-500/20">
                ابدأ مجاناً مع Google
            </a>
        </div>
    </section>
    """
    return layout("الرئيسية - Instapulse AI", content, user=user)

@router.get("/pricing", response_class=HTMLResponse)
async def pricing_page(request: Request):
    """صفحة الأسعار"""
    user = request.session.get("user")
    
    content = """
    <section class="py-12 space-y-8">
        <h2 class="text-3xl font-bold text-center">خطط الأسعار</h2>
        <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
            <div class="p-6 bg-slate-800 rounded-2xl border border-slate-700 space-y-4">
                <h3 class="text-2xl font-bold">الخطة المجانية</h3>
                <p class="text-3xl font-extrabold">$0 <span class="text-sm font-normal text-slate-400">/ شهرياً</span></p>
                <ul class="space-y-2 text-slate-300">
                    <li>✓ إدارة حساب واحد</li>
                    <li>✓ توليد 10 أفكار محتوى</li>
                </ul>
            </div>
            <div class="p-6 bg-blue-900/40 rounded-2xl border border-blue-500 space-y-4">
                <h3 class="text-2xl font-bold">الخطة الاحترافية</h3>
                <p class="text-3xl font-extrabold">$19 <span class="text-sm font-normal text-slate-400">/ شهرياً</span></p>
                <ul class="space-y-2 text-slate-300">
                    <li>✓ إدارة حسابات غير محدودة</li>
                    <li>✓ أتمتة كاملة مع الذكاء الاصطناعي</li>
                </ul>
            </div>
        </div>
    </section>
    """
    return layout("الأسعار - Instapulse AI", content, user=user)

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    """لوحة التحكم - محمية بالكامل"""
    user = request.session.get("user")
    
    # حماية الصفحة: إذا لم يسجل الدخول، يتم تحويله لصفحة Google
    if not user:
        return RedirectResponse(url="/auth/login/google", status_code=303)

    content = f"""
    <section class="py-8 space-y-6">
        <div class="flex items-center space-x-4 space-x-reverse bg-slate-800 p-6 rounded-2xl border border-slate-700">
            <img src="{user.get('picture', '')}" alt="Profile" class="w-16 h-16 rounded-full border-2 border-blue-500">
            <div>
                <h1 class="text-2xl font-bold">مرحباً بك، {user.get('name')} 👋</h1>
                <p class="text-slate-400">{user.get('email')}</p>
            </div>
        </div>
        
        <div class="grid md:grid-cols-3 gap-6">
            <div class="p-6 bg-slate-800 rounded-xl border border-slate-700">
                <h3 class="text-lg font-semibold text-slate-300">الحسابات المربوطة</h3>
                <p class="text-3xl font-bold mt-2">0</p>
            </div>
            <div class="p-6 bg-slate-800 rounded-xl border border-slate-700">
                <h3 class="text-lg font-semibold text-slate-300">المنشورات المجدولة</h3>
                <p class="text-3xl font-bold mt-2">0</p>
            </div>
            <div class="p-6 bg-slate-800 rounded-xl border border-slate-700">
                <h3 class="text-lg font-semibold text-slate-300">نقاط AI المتبقية</h3>
                <p class="text-3xl font-bold mt-2 text-blue-400">100</p>
            </div>
        </div>
    </section>
    """
    return layout("لوحة التحكم - Instapulse AI", content, user=user)
