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
    """لوحة التحكم - مع أداة توليد المحتوى بالذكاء الاصطناعي"""
    user = request.session.get("user")
    
    # حماية الصفحة: إذا لم يسجل الدخول، يتم تحويله لصفحة Google
    if not user:
        return RedirectResponse(url="/auth/login/google", status_code=303)

    content = f"""
    <section class="py-8 space-y-8 max-w-4xl mx-auto">
        <!-- معلومات المستخدم -->
        <div class="flex items-center space-x-4 space-x-reverse bg-slate-800 p-6 rounded-2xl border border-slate-700">
            <img src="{user.get('picture', 'https://ui-avatars.com/api/?name=User')}" alt="Profile" class="w-16 h-16 rounded-full border-2 border-blue-500">
            <div>
                <h1 class="text-2xl font-bold">مرحباً بك، {user.get('name')} 👋</h1>
                <p class="text-slate-400">{user.get('email')}</p>
            </div>
        </div>

        <!-- أداة الذكاء الاصطناعي لتوليد المحتوى -->
        <div class="bg-slate-800 p-6 rounded-2xl border border-blue-500/50 space-y-6 shadow-xl">
            <div class="flex items-center space-x-3 space-x-reverse">
                <span class="text-2xl">✨</span>
                <div>
                    <h2 class="text-xl font-bold text-blue-400">صانع المحتوى الذكي (AI Content Generator)</h2>
                    <p class="text-slate-400 text-sm">اكتب موضوع المنشور وسيصنع لك الذكاء الاصطناعي كابشن احترافي مع الهاشتاغات.</p>
                </div>
            </div>

            <form action="/ai/generate-caption" method="POST" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-slate-300 mb-2">عن ماذا يتحدث منشورك؟</label>
                    <textarea name="topic" rows="3" required placeholder="مثال: إطلاق منتج جديد للقهوة المختصة، أو نصائح لزيادة المبيعات في التجارة الإلكترونية..." class="w-full p-4 bg-slate-900 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-blue-500"></textarea>
                </div>

                <div>
                    <label class="block text-sm font-medium text-slate-300 mb-2">نبرة الصوت (Tone of Voice):</label>
                    <select name="tone" class="w-full p-3 bg-slate-900 border border-slate-700 rounded-xl text-white focus:outline-none focus:border-blue-500">
                        <option value="حماسي ومشوق">🔥 حماسي ومشوق</option>
                        <option value="احترافي ورسمي">💼 احترافي ورسمي</option>
                        <option value="ودي وفكاهي">😊 ودي وفكاهي</option>
                        <option value="تعليمي ومباشر">📚 تعليمي ومباشر</option>
                    </select>
                </div>

                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-blue-500/20">
                    توليد المحتوى بالذكاء الاصطناعي 🚀
                </button>
            </form>
        </div>

        <!-- بطاقات الإحصائيات -->
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
