from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()

def get_base_html(title: str, body_content: str, user: dict = None, is_ig_connected: bool = False) -> str:
    """قالب الصفحة الأساسي بتصميم فاخر مريح للعين وخط عربي حديث"""
    user_logged_in = user is not None
    return f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Tajawal', sans-serif;
                background-color: #090a0f;
                color: #f3f4f6;
            }}
            .card-panel {{
                background-color: #111318;
                border: 1px solid #1f242d;
            }}
            .btn-primary {{
                background-color: #ffffff;
                color: #000000;
                font-weight: 700;
            }}
            .btn-primary:hover {{
                background-color: #e5e7eb;
            }}
            .tab-active {{
                background-color: #1f242d !important;
                color: #ffffff !important;
                border-right: 3px solid #ffffff;
            }}
        </style>
    </head>
    <body class="min-h-screen flex flex-col antialiased">
        
        <!-- الترويسة الرئيسية الرسمية -->
        <header class="border-b border-zinc-800 bg-zinc-950 px-6 py-4 flex items-center justify-between sticky top-0 z-50">
            <div class="flex items-center gap-3">
                <a href="/" class="text-xl font-extrabold text-white tracking-wide">InstaPulse AI</a>
                <span class="text-xs text-zinc-400 border border-zinc-800 px-2.5 py-1 rounded-full">المنصة الرسمية</span>
            </div>

            <div class="flex items-center gap-4">
                <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-zinc-300">
                    <a href="/" class="hover:text-white transition">الرئيسية</a>
                    <a href="/pricing" class="hover:text-white transition">الباقات</a>
                    {f'<a href="/dashboard" class="hover:text-white font-bold transition">لوحة التحكم</a>' if user_logged_in else ''}
                </nav>

                <!-- زر القائمة المنسدلة الجانبية -->
                <div class="relative">
                    <button onclick="toggleMenu()" class="text-lg px-3 py-1.5 border border-zinc-800 rounded bg-zinc-900 text-white hover:bg-zinc-800 transition">
                        ☰
                    </button>
                    <div id="nav-dropdown" class="hidden absolute left-0 mt-2 w-52 bg-zinc-900 border border-zinc-800 rounded-lg shadow-xl z-50 py-2 text-sm text-zinc-300">
                        <a href="/" class="block px-4 py-2 hover:bg-zinc-800 hover:text-white">الرئيسية</a>
                        <a href="/pricing" class="block px-4 py-2 hover:bg-zinc-800 hover:text-white">الباقات والأسعار</a>
                        <a href="/connect-instagram" class="block px-4 py-2 hover:bg-zinc-800 hover:text-white">ربط حساب إنستغرام</a>
                        <a href="/dashboard" class="block px-4 py-2 hover:bg-zinc-800 hover:text-white font-bold">لوحة التحكم</a>
                    </div>
                </div>
            </div>
        </header>

        <!-- المحتوى الرئيسي -->
        <main class="flex-grow p-4 md:p-8 max-w-7xl w-full mx-auto">
            {body_content}
        </main>

        <footer class="border-t border-zinc-800 bg-zinc-950 py-4 px-6 text-center text-xs text-zinc-500">
            حقوق الطبع والنشر &copy; 2026 منصة InstaPulse AI Store. جميع الحقوق محفوظة.
        </footer>

        <script>
            function toggleMenu() {{
                document.getElementById('nav-dropdown').classList.toggle('hidden');
            }}
        </script>
    </body>
    </html>
    """

# --------------------------------------------------------------------------
# 1. الصفحة الرئيسية
# --------------------------------------------------------------------------
@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    user = request.session.get("user")
    content = """
    <section class="py-16 md:py-24 text-center space-y-8 max-w-3xl mx-auto">
        <h1 class="text-3xl md:text-5xl font-extrabold text-white leading-tight">
            أهلاً بك في منصة InstaPulse Store AI
        </h1>
        <p class="text-zinc-400 text-base md:text-lg leading-relaxed">
            المنصة الذكية المتكاملة لتحليل خوارزميات إنستغرام، أتمتة نشر الريلز، البوستات، والستوريات، واحتساب أوقات ذروة المتابعين بدقة فائقة لزيادة التفاعل والوصول.
        </p>
        <div class="pt-4 flex justify-center">
            <a href="/pricing" class="btn-primary text-base px-10 py-4 rounded-xl shadow-lg transition transform hover:scale-105">
                ابدأ الآن
            </a>
        </div>
    </section>
    """
    return get_base_html("InstaPulse Store AI - الرئيسية", content, user=user)

# --------------------------------------------------------------------------
# 2. صفحة عرض الباقات
# --------------------------------------------------------------------------
@router.get("/pricing", response_class=HTMLResponse)
async def pricing_page(request: Request):
    user = request.session.get("user")
    content = """
    <section class="py-8 space-y-8 max-w-4xl mx-auto">
        <div class="text-center space-y-2">
            <h2 class="text-3xl font-bold text-white">اختر الباقة المناسبة لحسابك</h2>
            <p class="text-zinc-400 text-sm">حدد الخطة للتحويل المباشر إلى صفحة ربط حساب إنستغرام وتفعيل الذكاء الاصطناعي</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 pt-6">
            <!-- الاشتراك الشهري -->
            <div class="card-panel p-8 rounded-2xl space-y-6 flex flex-col justify-between">
                <div class="space-y-4">
                    <span class="text-xs bg-zinc-800 text-zinc-300 px-3 py-1 rounded-full">باقة شهرية</span>
                    <h3 class="text-2xl font-bold text-white">الاشتراك الشهري</h3>
                    <div class="flex items-baseline gap-1">
                        <span class="text-4xl font-extrabold text-white">$7</span>
                        <span class="text-sm text-zinc-400">/ شهرياً</span>
                    </div>
                    <ul class="space-y-3 text-sm text-zinc-300 border-t border-zinc-800 pt-4">
                        <li class="flex items-center gap-2">✓ تحليل تفاعل الريلز والبوستات والستوريات</li>
                        <li class="flex items-center gap-2">✓ جدول النشر التلقائي في وقت الذروة</li>
                        <li class="flex items-center gap-2">✓ تقارير يومية وأسبوعية وشهرية</li>
                    </ul>
                </div>
                <a href="/connect-instagram" class="btn-primary w-full text-center py-3.5 rounded-xl block">
                    اختيار الباقة وربط الإنستغرام
                </a>
            </div>

            <!-- الاشتراك السنوي -->
            <div class="card-panel p-8 rounded-2xl space-y-6 flex flex-col justify-between border-zinc-700">
                <div class="space-y-4">
                    <span class="text-xs bg-white text-black font-bold px-3 py-1 rounded-full">الأكثر توفيراً</span>
                    <h3 class="text-2xl font-bold text-white">الاشتراك السنوي</h3>
                    <div class="flex items-baseline gap-1">
                        <span class="text-4xl font-extrabold text-white">$70</span>
                        <span class="text-sm text-zinc-400">/ سنوياً</span>
                    </div>
                    <ul class="space-y-3 text-sm text-zinc-300 border-t border-zinc-800 pt-4">
                        <li class="flex items-center gap-2">✓ جميع مميزات الباقة الشهرية</li>
                        <li class="flex items-center gap-2">✓ توفير شهرين مجاناً</li>
                        <li class="flex items-center gap-2">✓ أولوية التحليل في سيرفرات AI</li>
                    </ul>
                </div>
                <a href="/connect-instagram" class="btn-primary w-full text-center py-3.5 rounded-xl block">
                    اختيار الباقة وربط الإنستغرام
                </a>
            </div>
        </div>
    </section>
    """
    return get_base_html("الباقات - InstaPulse Store AI", content, user=user)

# --------------------------------------------------------------------------
# 3. صفحة ربط حساب إنستغرام (تفتح قبل الدخول للوحة التحكم)
# --------------------------------------------------------------------------
@router.get("/connect-instagram", response_class=HTMLResponse)
async def connect_instagram_page(request: Request):
    user = request.session.get("user")
    content = """
    <section class="py-12 max-w-md mx-auto space-y-6 text-center">
        <div class="card-panel p-8 rounded-2xl space-y-6">
            <div class="w-16 h-16 bg-zinc-800 rounded-full flex items-center justify-center mx-auto text-2xl">
                📸
            </div>
            <div class="space-y-2">
                <h2 class="text-xl font-bold text-white">ربط حساب إنستغرام الرسمي</h2>
                <p class="text-xs text-zinc-400">قم بربط حسابك التجاري أو حساب صانع المحتوى لتمكين الذكاء الاصطناعي من التحليل والنشر</p>
            </div>

            <form action="/auth/instagram/callback-simulate" method="POST" class="space-y-4">
                <div class="text-right">
                    <label class="text-xs text-zinc-400 block mb-1">اسم الحساب (Username)</label>
                    <input type="text" required placeholder="@your_username" class="w-full bg-black border border-zinc-800 rounded-lg p-3 text-sm text-white focus:outline-none focus:border-zinc-500">
                </div>
                <button type="submit" class="btn-primary w-full py-3 rounded-lg text-sm font-bold shadow">
                    تأكيد الربط وتفعيل لوحة التحكم
                </button>
            </form>
        </div>
    </section>
    """
    return get_base_html("ربط إنستغرام - InstaPulse Store AI", content, user=user)

@router.post("/auth/instagram/callback-simulate")
async def process_ig_connect(request: Request):
    request.session["instagram_connected"] = True
    return RedirectResponse(url="/dashboard", status_code=303)

# --------------------------------------------------------------------------
# 4. لوحة التحكم المتكاملة (تفتح فقط بعد الربط)
# --------------------------------------------------------------------------
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    user = request.session.get("user")
    is_ig_connected = request.session.get("instagram_connected", False)

    # حماية لوحة التحكم: التحويل لصفحة الربط إذا لم يكتمل الربط
    if not is_ig_connected:
        return RedirectResponse(url="/connect-instagram", status_code=303)

    content = """
    <div class="grid grid-cols-12 gap-6">
        
        <!-- القائمة الجانبية للتنقل بين الأقسام -->
        <aside class="col-span-12 lg:col-span-3 card-panel rounded-2xl p-4 space-y-4 h-fit">
            <div class="border-b border-zinc-800 pb-3">
                <p class="text-xs text-zinc-500">الحساب المرتبط</p>
                <p class="text-sm font-bold text-white">@Instagram_Account</p>
                <span class="text-[10px] bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded-full mt-1 inline-block">نشط ومفعل</span>
            </div>

            <nav class="space-y-1 text-sm font-medium">
                <button onclick="switchTab('tab-reels')" id="btn-reels" class="w-full text-right px-4 py-3 rounded-xl tab-active transition">
                    🎬 قسم الريلز (Reels)
                </button>
                <button onclick="switchTab('tab-posts')" id="btn-posts" class="w-full text-right px-4 py-3 rounded-xl text-zinc-400 hover:bg-zinc-900 hover:text-white transition">
                    🖼️ قسم البوستات (Posts)
                </button>
                <button onclick="switchTab('tab-stories')" id="btn-stories" class="w-full text-right px-4 py-3 rounded-xl text-zinc-400 hover:bg-zinc-900 hover:text-white transition">
                    📱 قسم الستوري (Stories)
                </button>
                <button onclick="switchTab('tab-health')" id="btn-health" class="w-full text-right px-4 py-3 rounded-xl text-zinc-400 hover:bg-zinc-900 hover:text-white transition">
                    📊 صحة الحساب والتقارير
                </button>
            </nav>
        </aside>

        <!-- منطقة العرض والتفاعل الرئيسية -->
        <main class="col-span-12 lg:col-span-9 space-y-6">
            
            <!-- ======================= 1. قسم الريلز ======================= -->
            <div id="tab-reels" class="space-y-6">
                <div class="card-panel p-6 rounded-2xl space-y-4">
                    <h3 class="text-lg font-bold text-white">تحليل تفاعل مقاطع الريلز (Reels Analytics)</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">معدل الإعجابات</p>
                            <p class="text-xl font-bold text-white mt-1">24.5K</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">معدل التعليقات</p>
                            <p class="text-xl font-bold text-white mt-1">3.2K</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">الرسائل المباشرة (DMs)</p>
                            <p class="text-xl font-bold text-white mt-1">840</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">معدل الحفظ والمشاركة</p>
                            <p class="text-xl font-bold text-white mt-1">5.1K</p>
                        </div>
                    </div>
                </div>

                <!-- رفع ريل للتحليل والنشر -->
                <div class="card-panel p-6 rounded-2xl space-y-4">
                    <h3 class="text-base font-bold text-white">رفع محتوى ريل للنشر والتوقيت الآلي</h3>
                    <form onsubmit="scheduleReel(event)" class="space-y-4">
                        <div class="border-2 border-dashed border-zinc-800 p-6 rounded-xl text-center space-y-2">
                            <p class="text-xs text-zinc-400">اختر فيديو الريل للتحليل الخوارزمي</p>
                            <input type="file" required class="text-xs text-zinc-400">
                        </div>
                        <button type="submit" class="btn-primary w-full py-3 rounded-xl text-sm">
                            تحليل الجمهور واحتساب وقت الذروة
                        </button>
                    </form>

                    <!-- جدول موعد النشر بعد التحليل -->
                    <div id="reel-schedule-result" class="hidden pt-4 space-y-4 border-t border-zinc-800">
                        <h4 class="text-sm font-bold text-emerald-400">✓ تم التحليل والتجدول بنجاح في جدول الذروة</h4>
                        <div class="overflow-x-auto">
                            <table class="w-full text-right text-xs text-zinc-300">
                                <thead class="bg-black text-zinc-500">
                                    <tr>
                                        <th class="p-3">وقت النشر المقترح</th>
                                        <th class="p-3">الفئة المستهدفة</th>
                                        <th class="p-3">نسبة الصعود المتوقعة</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-t border-zinc-800">
                                        <td class="p-3 text-white font-bold">اليوم الساعة 8:30 مساءً</td>
                                        <td class="p-3">الجمهور المهتم بالتكنولوجيا والريادة</td>
                                        <td class="p-3 text-emerald-400">94.2% (إكسبلور مؤكد)</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- إمكانية تعديل الكابشن والهاشتاغات -->
                        <div class="space-y-2 pt-2">
                            <label class="text-xs text-zinc-400 block">الكابشن والهاشتاغات المستخرجة (يمكنك التعديل عليها):</label>
                            <textarea id="reel-caption" rows="3" class="w-full bg-black border border-zinc-800 p-3 rounded-xl text-xs text-zinc-200">أفضل طرق استغلال الذكاء الاصطناعي لتطوير عملك الشخصي! 🚀 #ذكاء_اصطناعي #تكنولوجيا #انستغرام #صانع_محتوى</textarea>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================= 2. قسم البوستات ======================= -->
            <div id="tab-posts" class="space-y-6 hidden">
                <div class="card-panel p-6 rounded-2xl space-y-4">
                    <h3 class="text-lg font-bold text-white">تحليل تفاعل البوستات (Posts Analytics)</h3>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">إجمالي اللايكات</p>
                            <p class="text-xl font-bold text-white mt-1">12.8K</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">التعليقات والمناقشات</p>
                            <p class="text-xl font-bold text-white mt-1">1.4K</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">تحويل الرسائل</p>
                            <p class="text-xl font-bold text-white mt-1">420</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">نقرات الرابط بالبروفايل</p>
                            <p class="text-xl font-bold text-white mt-1">930</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================= 3. قسم الستوري ======================= -->
            <div id="tab-stories" class="space-y-6 hidden">
                <div class="card-panel p-6 rounded-2xl space-y-4">
                    <h3 class="text-lg font-bold text-white">تحليل تفاعل الستوريات (Stories Analytics)</h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">معدل مشاهدات الستوري</p>
                            <p class="text-xl font-bold text-white mt-1">8.5K</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">معدل الردود والرسائل</p>
                            <p class="text-xl font-bold text-white mt-1">610</p>
                        </div>
                        <div class="bg-black p-4 rounded-xl border border-zinc-800">
                            <p class="text-xs text-zinc-500">نسبة الاحتفاظ بالمشاهدة</p>
                            <p class="text-xl font-bold text-white mt-1">87%</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================= 4. صحة الحساب والتقارير ======================= -->
            <div id="tab-health" class="space-y-6 hidden">
                <div class="card-panel p-6 rounded-2xl space-y-6">
                    <div class="flex justify-between items-center border-b border-zinc-800 pb-4">
                        <div>
                            <h3 class="text-lg font-bold text-white">صحة الحساب وتقارير نمو المتابعين</h3>
                            <p class="text-xs text-zinc-400">تحليل جودة الحساب وزيادة المتابعين الحقيقيين</p>
                        </div>
                        <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-3 py-1 rounded-full">الحساب في حالة ممتازة</span>
                    </div>

                    <!-- خيارات تحميل واستعراض التقارير -->
                    <div class="grid md:grid-cols-3 gap-4">
                        <div class="bg-black p-5 rounded-xl border border-zinc-800 space-y-3">
                            <h4 class="text-sm font-bold text-white">التقرير اليومي</h4>
                            <p class="text-xs text-zinc-400">ملخص التفاعل والرسائل خلال الـ 24 ساعة الماضية.</p>
                            <button onclick="alert('جاري استخراج التقرير اليومي...')" class="text-xs border border-zinc-700 w-full py-2 rounded-lg text-zinc-300 hover:bg-zinc-800">عرض التقرير اليومي</button>
                        </div>

                        <div class="bg-black p-5 rounded-xl border border-zinc-800 space-y-3">
                            <h4 class="text-sm font-bold text-white">التقرير الأسبوعي</h4>
                            <p class="text-xs text-zinc-400">تحليل نمو المتابعين والوصول وأعلى الريلز نجاحاً.</p>
                            <button onclick="alert('جاري استخراج التقرير الأسبوعي...')" class="text-xs border border-zinc-700 w-full py-2 rounded-lg text-zinc-300 hover:bg-zinc-800">عرض التقرير الأسبوعي</button>
                        </div>

                        <div class="bg-black p-5 rounded-xl border border-zinc-800 space-y-3">
                            <h4 class="text-sm font-bold text-white">التقرير الشهري الشامل</h4>
                            <p class="text-xs text-zinc-400">تقرير كامل مخصص لزيادة التفاعل وتحسين البروفايل.</p>
                            <button onclick="alert('جاري استخراج التقرير الشهري...')" class="text-xs border border-zinc-700 w-full py-2 rounded-lg text-zinc-300 hover:bg-zinc-800">عرض التقرير الشهري</button>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <script>
        function switchTab(tabName) {{
            const tabs = ['tab-reels', 'tab-posts', 'tab-stories', 'tab-health'];
            tabs.forEach(t => {{
                document.getElementById(t).classList.add('hidden');
                document.getElementById('btn-' + t.replace('tab-', '')).className = "w-full text-right px-4 py-3 rounded-xl text-zinc-400 hover:bg-zinc-900 hover:text-white transition";
            }});

            document.getElementById(tabName).classList.remove('hidden');
            document.getElementById('btn-' + tabName.replace('tab-', '')).className = "w-full text-right px-4 py-3 rounded-xl tab-active transition";
        }}

        function scheduleReel(e) {{
            e.preventDefault();
            document.getElementById('reel-schedule-result').classList.remove('hidden');
        }}
    </script>
    """
    return get_base_html("لوحة التحكم - InstaPulse AI", content, user=user)
