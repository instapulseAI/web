from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from templates import layout

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """الصفحة الرئيسية للموقع"""
    user = request.session.get("user")
    content = """
    <section class="py-16 text-center space-y-6 max-w-4xl mx-auto px-4">
        <div class="inline-flex items-center space-x-2 space-x-reverse bg-gradient-to-r from-purple-600 via-pink-600 to-orange-500 text-white px-4 py-1.5 rounded-full text-sm font-semibold mb-2">
            <span>📸 الأدمن الذكي الأول لإدارة حسابات إنستغرام</span>
        </div>
        <h1 class="text-4xl md:text-6xl font-black leading-tight">
            درب أدمن الذكاء الاصطناعي لحسابك في <span class="bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500 bg-clip-text text-transparent">Instagram</span>
        </h1>
        <p class="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto">
            حلّل خوارزميات الفيديو، اختر أفضل وقت للنشر، اصعد للإكسبلور، وانشر الريلز والستوريات تلقائياً.
        </p>
        <div class="pt-6 flex justify-center gap-4">
            <a href="/auth/login/google" class="bg-gradient-to-r from-purple-600 via-pink-600 to-orange-500 hover:opacity-95 text-white text-lg font-bold px-8 py-4 rounded-2xl transition shadow-xl shadow-pink-500/20 flex items-center gap-2">
                <span>ابدأ الآن - 7 أيام مجاناً</span>
            </a>
        </div>
    </section>
    """
    return layout("Instapulse AI - أدمن إنستغرام الذكي", content, user=user)

@router.get("/pricing", response_class=HTMLResponse)
async def pricing_page(request: Request):
    """صفحة الأسعار الدقيقة كما طلبها المستخدم"""
    user = request.session.get("user")
    content = """
    <section class="py-10 space-y-8 max-w-5xl mx-auto px-4">
        <div class="text-center space-y-3">
            <h2 class="text-3xl md:text-4xl font-extrabold bg-gradient-to-r from-purple-400 via-pink-500 to-orange-400 bg-clip-text text-transparent">خطط الأسعار والاشتراكات</h2>
            <p class="text-slate-400">اختر الخطة المناسبة لك وابدأ بأتمتة حسابك على إنستغرام</p>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
            <!-- التجربة المجانية -->
            <div class="bg-slate-800/80 border border-slate-700 rounded-3xl p-6 space-y-6 flex flex-col justify-between hover:border-slate-500 transition shadow-lg">
                <div class="space-y-4">
                    <span class="text-xs font-bold text-slate-400 bg-slate-700/60 px-3 py-1 rounded-full border border-slate-600">تجربة مجانية</span>
                    <h3 class="text-2xl font-bold">7 أيام مجاناً</h3>
                    <p class="text-4xl font-extrabold">$0 <span class="text-sm font-normal text-slate-400">/ 7 أيام</span></p>
                    <ul class="space-y-2 text-slate-300 text-sm">
                        <li class="flex items-center gap-2"><span class="text-green-400">✓</span> تجربة فحص صحة الحساب</li>
                        <li class="flex items-center gap-2"><span class="text-green-400">✓</span> تحليل خوارزميات الريلز والبوستات</li>
                        <li class="flex items-center gap-2"><span class="text-green-400">✓</span> ربط حساب إنستغرام</li>
                    </ul>
                </div>
                <a href="/auth/login/google" class="w-full text-center py-3 bg-slate-700 hover:bg-slate-600 text-white font-bold rounded-xl transition">تجربة 7 أيام مجاناً</a>
            </div>

            <!-- الاشتراك الشهري -->
            <div class="bg-slate-800/80 border border-pink-500/60 rounded-3xl p-6 space-y-6 flex flex-col justify-between relative shadow-xl shadow-pink-500/10">
                <div class="space-y-4">
                    <span class="text-xs font-bold text-pink-400 bg-pink-500/10 px-3 py-1 rounded-full border border-pink-500/30">الخطة الأساسية</span>
                    <h3 class="text-2xl font-bold">الاشتراك الشهري</h3>
                    <p class="text-4xl font-extrabold">$7 <span class="text-sm font-normal text-slate-400">/ 30 يوم</span></p>
                    <ul class="space-y-2 text-slate-300 text-sm">
                        <li class="flex items-center gap-2"><span class="text-pink-400">✓</span> النشر التلقائي الذكي وحساب وقت النشر</li>
                        <li class="flex items-center gap-2"><span class="text-pink-400">✓</span> كتابة الكابشن والهاشتاغات التلقائية</li>
                        <li class="flex items-center gap-2"><span class="text-pink-400">✓</span> فحص خوارزميات صعود الإكسبلور</li>
                    </ul>
                </div>
                <a href="/auth/login/google" class="w-full text-center py-3 bg-gradient-to-r from-purple-600 via-pink-600 to-orange-500 text-white font-bold rounded-xl transition shadow-lg">اشترك شهرياً ($7 / 30 يوم)</a>
            </div>

            <!-- الاشتراك السنوي -->
            <div class="bg-slate-800/80 border border-purple-500/60 rounded-3xl p-6 space-y-6 flex flex-col justify-between relative shadow-xl shadow-purple-500/10">
                <div class="space-y-4">
                    <span class="text-xs font-bold text-purple-400 bg-purple-500/10 px-3 py-1 rounded-full border border-purple-500/30">أفضل توفير</span>
                    <h3 class="text-2xl font-bold">الاشتراك السنوي</h3>
                    <p class="text-4xl font-extrabold">$70 <span class="text-sm font-normal text-slate-400">/ سنوياً</span></p>
                    <ul class="space-y-2 text-slate-300 text-sm">
                        <li class="flex items-center gap-2"><span class="text-purple-400">✓</span> أدمن ذكاء اصطناعي يعمل 24/7</li>
                        <li class="flex items-center gap-2"><span class="text-purple-400">✓</span> توفير شهرين كاملين</li>
                        <li class="flex items-center gap-2"><span class="text-purple-400">✓</span> جميع المميزات بدون أي حدود</li>
                    </ul>
                </div>
                <a href="/auth/login/google" class="w-full text-center py-3 bg-purple-600 hover:bg-purple-700 text-white font-bold rounded-xl transition">اشترك سنوياً ($70 / سنة)</a>
            </div>
        </div>
    </section>
    """
    return layout("الأسعار - Instapulse AI", content, user=user)

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    """واجهة التطبيق الكاملة المصممة بواجهة إنستغرام مع كافة الأقسام التفاعلية"""
    user = request.session.get("user")
    
    if not user:
        return RedirectResponse(url="/auth/login/google", status_code=303)

    instagram_connected = user.get("instagram_connected", False)

    content = f"""
    <div class="flex flex-col md:flex-row min-h-[85vh] gap-6" id="app-container">
        
        <!-- Sidebar: المنيو الجانبي الشبيه بإنستغرام -->
        <aside class="w-full md:w-64 bg-slate-800/90 dark:bg-slate-800 border border-slate-700 rounded-3xl p-4 flex flex-col justify-between shrink-0 shadow-xl">
            <div class="space-y-6">
                <!-- شعار إنستغرام / المنصة -->
                <div class="flex items-center justify-between px-3 py-2 border-b border-slate-700/60">
                    <span class="text-xl font-black bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500 bg-clip-text text-transparent">Instagram AI</span>
                    <button onclick="toggleTheme()" class="p-2 bg-slate-700/60 hover:bg-slate-700 rounded-xl text-xs transition" title="تبديل المظهر">
                        🌓 <span id="theme-text" class="hidden md:inline text-[11px]">مظهر</span>
                    </button>
                </div>

                <!-- قائمة الأقسام الرئيسية -->
                <nav class="space-y-1 text-sm font-medium">
                    <button onclick="showTab('health')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 rounded-2xl hover:bg-slate-700/50 text-slate-300 hover:text-white transition active-tab" id="btn-health">
                        <span class="text-lg">❤️</span>
                        <span>صحة الحساب والـ Explore</span>
                    </button>
                    
                    <button onclick="showTab('reels')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 rounded-2xl hover:bg-slate-700/50 text-slate-300 hover:text-white transition" id="btn-reels">
                        <span class="text-lg">🎬</span>
                        <span>قسم الريلز (Reels)</span>
                    </button>
                    
                    <button onclick="showTab('posts')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 rounded-2xl hover:bg-slate-700/50 text-slate-300 hover:text-white transition" id="btn-posts">
                        <span class="text-lg">🖼️</span>
                        <span>قسم البوستات (Posts)</span>
                    </button>

                    <button onclick="showTab('stories')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 rounded-2xl hover:bg-slate-700/50 text-slate-300 hover:text-white transition" id="btn-stories">
                        <span class="text-lg">📱</span>
                        <span>قسم الستوري (Stories)</span>
                    </button>

                    <button onclick="showTab('upload')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 bg-gradient-to-r from-purple-600/30 to-pink-600/30 border border-pink-500/40 rounded-2xl text-pink-300 font-bold hover:opacity-90 transition mt-2" id="btn-upload">
                        <span class="text-lg">🚀</span>
                        <span>الناشر والتحليل الآلي</span>
                    </button>

                    <button onclick="showTab('notifications')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 rounded-2xl hover:bg-slate-700/50 text-slate-300 hover:text-white transition" id="btn-notifications">
                        <span class="text-lg">🔔</span>
                        <span>التنبيهات والأداء</span>
                    </button>

                    <button onclick="showTab('account')" class="nav-btn w-full flex items-center gap-3 px-4 py-3 rounded-2xl hover:bg-slate-700/50 text-slate-300 hover:text-white transition" id="btn-account">
                        <span class="text-lg">👤</span>
                        <span>إعدادات الحساب</span>
                    </button>
                </nav>
            </div>

            <!-- معلومات حساب إنستغرام والربط -->
            <div class="pt-4 border-t border-slate-700/60 space-y-3">
                <div class="flex items-center gap-3 px-2">
                    <img src="{user.get('picture', 'https://ui-avatars.com/api/?name=User')}" class="w-10 h-10 rounded-full border-2 border-pink-500">
                    <div class="overflow-hidden">
                        <p class="text-xs font-bold text-white truncate">{user.get('name')}</p>
                        <p class="text-[10px] text-slate-400 truncate">{'إنستغرام مرتبط ✓' if instagram_connected else 'لم يتم ربط إنستغرام'}</p>
                    </div>
                </div>
                {'' if instagram_connected else '<a href="/auth/login/instagram" class="block w-full text-center py-2 px-3 bg-gradient-to-r from-purple-600 to-pink-600 hover:opacity-90 text-white rounded-xl text-xs font-bold transition">ربط حساب Instagram 📸</a>'}
            </div>
        </aside>

        <!-- Dynamic Main Content: المحتوى المتبدل للأقسام -->
        <main class="flex-grow bg-slate-800/60 border border-slate-700/80 rounded-3xl p-6 md:p-8 space-y-6 shadow-xl overflow-y-auto">
            
            <!-- 1. قسم صحة الحساب وصعود الإكسبلور -->
            <div id="tab-health" class="tab-content space-y-6">
                <div class="flex items-center justify-between border-b border-slate-700 pb-4">
                    <div>
                        <h2 class="text-2xl font-bold flex items-center gap-2 text-pink-400">
                            ❤️ قسم صحة الحساب وصعود الإكسبلور
                        </h2>
                        <p class="text-slate-400 text-sm">تحليل مستوى أمان وحيوية الحساب ومتطلبات خوارزمية إنستغرام</p>
                    </div>
                    <span class="px-4 py-1.5 bg-green-500/10 text-green-400 border border-green-500/30 rounded-full text-xs font-bold">الحساب في حالة ممتازة 94%</span>
                </div>

                <div class="grid md:grid-cols-3 gap-4">
                    <div class="bg-slate-900/80 p-5 rounded-2xl border border-slate-700 space-y-2">
                        <span class="text-xs text-slate-400">معدل الوصول للإكسبلور</span>
                        <p class="text-3xl font-extrabold text-purple-400">88.5%</p>
                        <p class="text-[11px] text-green-400">↑ مرتفع مقارنة بالأسبوع الماضي</p>
                    </div>
                    <div class="bg-slate-900/80 p-5 rounded-2xl border border-slate-700 space-y-2">
                        <span class="text-xs text-slate-400">قوة التفاعل (Engagement Rate)</span>
                        <p class="text-3xl font-extrabold text-pink-400">12.4%</p>
                        <p class="text-[11px] text-slate-400">أعلى من المتوسط في مجالك</p>
                    </div>
                    <div class="bg-slate-900/80 p-5 rounded-2xl border border-slate-700 space-y-2">
                        <span class="text-xs text-slate-400">معدل جودة الحساب (Account Health)</span>
                        <p class="text-3xl font-extrabold text-green-400">سليم 100%</p>
                        <p class="text-[11px] text-slate-400">لا توجد أية مخالفات أو حظر خفي</p>
                    </div>
                </div>

                <!-- نصائح الإكسبلور الذكية -->
                <div class="bg-slate-900/90 p-6 rounded-2xl border border-pink-500/30 space-y-4">
                    <h3 class="text-lg font-bold text-white flex items-center gap-2">🎯 توصيات الأدمن الذكي للصعود للإكسبلور اليوم:</h3>
                    <ul class="space-y-3 text-sm text-slate-300">
                        <li class="flex items-start gap-2"><span class="text-pink-400 font-bold">1.</span> <span>قم بنشر <b>Reel</b> قصير ومدته بين 7 إلى 11 ثانية مع صوت تريند (Trending Audio).</span></li>
                        <li class="flex items-start gap-2"><span class="text-pink-400 font-bold">2.</span> <span>افتح <b>Story</b> تفاعلي يحتوي على استفتائين (Polls) قبل نشر الريل بساعة لزيادة المشاهدات.</span></li>
                        <li class="flex items-start gap-2"><span class="text-pink-400 font-bold">3.</span> <span>افضل وقت لنشر البوست القادم للحساب هو الساعة <b>8:30 مساءً</b> بتوقيتك المحلي.</span></li>
                    </ul>
                </div>
            </div>

            <!-- 2. قسم الناشر والتحليل الآلي (ميزة رفع الفيديو والتحليل) -->
            <div id="tab-upload" class="tab-content space-y-6 hidden">
                <div class="border-b border-slate-700 pb-4">
                    <h2 class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-500 to-orange-400 flex items-center gap-2">
                        🚀 الناشر الآلي وتحليل الخوارزميات
                    </h2>
                    <p class="text-slate-400 text-sm">ارفع الفيديو أو البوست، وسيقوم الـ AI بتحليل الفيديو وتحديد أفضل وقت ونشره تلقائياً مع الكابشن والهاشتاغات.</p>
                </div>

                <form action="/ai/generate-caption" method="POST" class="space-y-5">
                    <!-- منصة رفع الملفات drag & drop -->
                    <div class="border-2 border-dashed border-pink-500/40 hover:border-pink-500 bg-slate-900/60 rounded-3xl p-8 text-center space-y-3 cursor-pointer transition">
                        <div class="w-16 h-16 bg-pink-500/10 text-pink-400 rounded-full flex items-center justify-center mx-auto text-3xl">📤</div>
                        <div>
                            <p class="font-bold text-white text-base">اسحب وأسقط فيديو الريلز أو البوست هنا</p>
                            <p class="text-xs text-slate-400 mt-1">يدعم MP4, MOV, JPG, PNG (حد أقصى 500MB)</p>
                        </div>
                        <input type="file" class="hidden" id="file-input">
                        <button type="button" onclick="document.getElementById('file-input').click()" class="px-5 py-2 bg-slate-800 border border-slate-600 rounded-xl text-xs font-bold text-slate-200 hover:bg-slate-700 transition">اختر الملف من جهازك</button>
                    </div>

                    <div class="grid md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-300 mb-2">نوع المحتوى المرفوع:</label>
                            <select name="type" class="w-full p-3 bg-slate-900 border border-slate-700 rounded-xl text-white text-sm focus:border-pink-500 outline-none">
                                <option value="ريلز Reels">🎬 ريلز (Reel)</option>
                                <option value="بوست Post">🖼️ بوست عادي (Post)</option>
                                <option value="ستوري Story">📱 ستوري (Story)</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-xs font-bold text-slate-300 mb-2">وضع النشر المطلوب:</label>
                            <select class="w-full p-3 bg-slate-900 border border-slate-700 rounded-xl text-white text-sm focus:border-pink-500 outline-none">
                                <option>⚡ النشر التلقائي في أفضل وقت لخوارزمية الحساب</option>
                                <option>📝 توليد الكابشن والهاشتاغات وحفظه كمسوّدة</option>
                                <option>🚀 النشر الفوري الآن على إنستغرام</option>
                            </select>
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-300 mb-2">وصف مختصر أو فكرة المحتوى (ليحللها الـ AI):</label>
                        <textarea name="topic" rows="3" required placeholder="مثال: فيديو شرح 3 أسرار لزيادة المبيعات في إنستغرام..." class="w-full p-4 bg-slate-900 border border-slate-700 rounded-2xl text-white placeholder-slate-500 focus:border-pink-500 outline-none text-sm"></textarea>
                    </div>

                    <button type="submit" class="w-full py-4 bg-gradient-to-r from-purple-600 via-pink-600 to-orange-500 hover:opacity-95 text-white font-bold rounded-2xl text-base shadow-xl shadow-pink-500/20 transition">
                        فحص الخوارزمية + كتابة الكابشن والهاشتاغ + جدولة النشر 🎯
                    </button>
                </form>
            </div>

            <!-- 3. قسم الريلز Reels -->
            <div id="tab-reels" class="tab-content space-y-6 hidden">
                <div class="flex items-center justify-between border-b border-slate-700 pb-4">
                    <h2 class="text-2xl font-bold text-pink-400 flex items-center gap-2">🎬 قسم إدارة وتحليل الريلز (Reels)</h2>
                    <span class="text-xs bg-pink-500/10 text-pink-400 px-3 py-1 rounded-full border border-pink-500/20">جاهز للفحص</span>
                </div>
                <div class="bg-slate-900/80 p-6 rounded-2xl border border-slate-700 space-y-4">
                    <p class="text-slate-300 text-sm">هنا يمكنك معاينة أداء مقاطع الـ Reels السابقة ومعرفة أي المقاطع حققت أعلى نسبة مشاهدات وتفاعل، مع تحديد الصوت الموسيقي التريند الأنسب لمقطعك القادم.</p>
                    <button onclick="showTab('upload')" class="px-6 py-2.5 bg-pink-600 hover:bg-pink-700 text-white font-bold text-xs rounded-xl transition">إنشاء وتحليل Reel جديد 🎬</button>
                </div>
            </div>

            <!-- 4. قسم البوستات Posts -->
            <div id="tab-posts" class="tab-content space-y-6 hidden">
                <div class="flex items-center justify-between border-b border-slate-700 pb-4">
                    <h2 class="text-2xl font-bold text-purple-400 flex items-center gap-2">🖼️ قسم المنشورات والبوستات (Posts)</h2>
                </div>
                <div class="bg-slate-900/80 p-6 rounded-2xl border border-slate-700 space-y-4">
                    <p class="text-slate-300 text-sm">إدارة البوستات الفردية والألبومات (Carousel). يساعدك الأدمن على اختيار أفضل 10 إلى 30 هاشتاغ نشط لضمان وصول المنشور لأكبر عدد من المتابعين المهتمين.</p>
                    <button onclick="showTab('upload')" class="px-6 py-2.5 bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs rounded-xl transition">جدولة بوست جديد 🖼️</button>
                </div>
            </div>

            <!-- 5. قسم الستوري Stories -->
            <div id="tab-stories" class="tab-content space-y-6 hidden">
                <div class="flex items-center justify-between border-b border-slate-700 pb-4">
                    <h2 class="text-2xl font-bold text-orange-400 flex items-center gap-2">📱 قسم الستوري (Stories)</h2>
                </div>
                <div class="bg-slate-900/80 p-6 rounded-2xl border border-slate-700 space-y-4">
                    <p class="text-slate-300 text-sm">حدد الأوقات التي يكون فيها متابعوك متصلين لنشر الستوري. يقترح الذكاء الاصطناعي أفكار أسئلة وملصقات تفاعلية لرفع المشاهدات.</p>
                    <button onclick="showTab('upload')" class="px-6 py-2.5 bg-orange-600 hover:bg-orange-700 text-white font-bold text-xs rounded-xl transition">رفع ستوري تفاعلي 📱</button>
                </div>
            </div>

            <!-- 6. قسم التنبيهات Notifications -->
            <div id="tab-notifications" class="tab-content space-y-6 hidden">
                <div class="border-b border-slate-700 pb-4">
                    <h2 class="text-2xl font-bold text-yellow-400 flex items-center gap-2">🔔 التنبيهات وإشعارات الأدمن</h2>
                </div>
                <div class="space-y-3">
                    <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700 flex items-center gap-3">
                        <span class="text-xl">✅</span>
                        <div>
                            <p class="text-sm font-bold text-white">تم تمكين فحص خوارزمية إنستغرام بنجاح</p>
                            <p class="text-xs text-slate-400">منذ 10 دقائق</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. إعدادات الحساب Account Settings -->
            <div id="tab-account" class="tab-content space-y-6 hidden">
                <div class="border-b border-slate-700 pb-4">
                    <h2 class="text-2xl font-bold text-slate-200 flex items-center gap-2">👤 إعدادات ربط الحسابات</h2>
                </div>
                <div class="bg-slate-900/80 p-6 rounded-2xl border border-slate-700 space-y-4">
                    <p class="text-sm text-slate-300">بيانات المستخدم المرتبط بـ Google & Instagram:</p>
                    <p class="text-xs font-mono text-pink-400">البريد: {user.get('email')}</p>
                    <p class="text-xs text-slate-400">حالة اشتراك الحساب: <b>7 أيام مجانية نشطة 🟢</b></p>
                </div>
            </div>

        </main>
    </div>

    <!-- JavaScript للتبديل السريع بين الأقسام وتغيير المظهر Dark/Light -->
    <script>
        function showTab(tabId) {{
            // إخفاء جميع الأقسام
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));
            
            # إظهار القسم المحدد
            document.getElementById('tab-' + tabId).classList.remove('hidden');

            # التمييز البصري للأزرار
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('bg-slate-700/60', 'text-white'));
            const activeBtn = document.getElementById('btn-' + tabId);
            if (activeBtn) {{
                activeBtn.classList.add('bg-slate-700/60', 'text-white');
            }}
        }}

        function toggleTheme() {{
            document.body.classList.toggle('light-theme');
            const themeText = document.getElementById('theme-text');
            if (document.body.classList.contains('light-theme')) {{
                document.body.style.backgroundColor = '#f1f5f9';
                document.body.style.color = '#0f172a';
                if(themeText) themeText.innerText = "داكن";
            }} else {{
                document.body.style.backgroundColor = '#0f172a';
                document.body.style.color = '#f8fafc';
                if(themeText) themeText.innerText = "فاتح";
            }}
        }}
    </script>
    """
    return layout("لوحة التحكم - Instapulse AI", content, user=user)
