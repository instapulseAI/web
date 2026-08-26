from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from templates import layout

router = APIRouter(prefix="/admin", tags=["Admin Panel"])

# بيانات دخول الأدمين الخاص بك
ADMIN_EMAIL = "admin_alimaher@admin.com"
ADMIN_PASSWORD = "admminalialiadmin1010admin momo"

# قائمة الحسابات المعفاة من الاشتراك (مجاناً مدى الحياة)
free_lifetime_users = ["vip_user@example.com"]

@router.get("/login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    """صفحة تسجيل دخول الأدمين"""
    user = request.session.get("user")
    
    content = """
    <section class="py-12 max-w-md mx-auto">
        <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700 space-y-6">
            <h2 class="text-2xl font-bold text-center text-blue-400">لوحة دخول الإدارة (Admin)</h2>
            <form action="/admin/login" method="POST" class="space-y-4">
                <div>
                    <label class="block text-sm text-slate-300 mb-1">البريد الإلكتروني للأدمين</label>
                    <input type="email" name="email" required class="w-full p-3 bg-slate-900 border border-slate-700 rounded-xl text-white focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-sm text-slate-300 mb-1">كلمة المرور</label>
                    <input type="password" name="password" required class="w-full p-3 bg-slate-900 border border-slate-700 rounded-xl text-white focus:outline-none focus:border-blue-500">
                </div>
                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition">
                    تسجيل الدخول كـ Admin
                </button>
            </form>
        </div>
    </section>
    """
    return layout("دخول الأدمين - Instapulse AI", content, user=user)

@router.post("/login")
async def admin_login_submit(request: Request, email: str = Form(...), password: str = Form(...)):
    """التحقق من كلمة المرور والبريد"""
    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        request.session["user"] = {
            "name": "علي ماهر (Admin)",
            "email": email,
            "is_admin": True,
            "picture": "https://ui-avatars.com/api/?name=Admin+Ali&background=0D8ABC&color=fff"
        }
        return RedirectResponse(url="/admin/dashboard", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="بيانات الدخول غير صحيحة.")

@router.get("/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    """لوحة تحكم الأدمين الخاصة"""
    user = request.session.get("user")
    
    # حماية الصفحة: التأكد من أن المسجل هو الأدمين
    if not user or not user.get("is_admin"):
        return RedirectResponse(url="/admin/login", status_code=303)

    users_list_html = "".join([f"<li class='py-1 text-slate-300'>✓ {u} (مجاني مدى الحياة)</li>" for u in free_lifetime_users])

    content = f"""
    <section class="py-8 space-y-6">
        <div class="bg-slate-800 p-6 rounded-2xl border border-blue-500 space-y-2">
            <h1 class="text-3xl font-bold text-blue-400">مرحباً بك في لوحة تحكم الأدمين 👑</h1>
            <p class="text-slate-300">البريد الحالي: {user.get('email')}</p>
        </div>

        <div class="grid md:grid-cols-2 gap-6">
            <!-- إحصائيات المنصة -->
            <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
                <h3 class="text-xl font-bold">إحصائيات المنصة</h3>
                <div class="flex justify-between items-center bg-slate-900 p-4 rounded-lg">
                    <span>إجمالي المشتركين المسجلين:</span>
                    <span class="text-2xl font-bold text-blue-400">1</span>
                </div>
                <div class="flex justify-between items-center bg-slate-900 p-4 rounded-lg">
                    <span>الحسابات المجانية مدى الحياة:</span>
                    <span class="text-2xl font-bold text-green-400">{len(free_lifetime_users)}</span>
                </div>
            </div>

            <!-- إضافة مستخدم مجاني -->
            <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-4">
                <h3 class="text-xl font-bold">منح اشتراك مجاني مدى الحياة</h3>
                <form action="/admin/add-free-user" method="POST" class="space-y-3">
                    <input type="email" name="target_email" placeholder="أدخل إيميل المستخدم" required class="w-full p-3 bg-slate-900 border border-slate-700 rounded-xl text-white">
                    <button type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 rounded-xl transition">
                        تفعيل الاشتراك المجاني
                    </button>
                </form>
            </div>
        </div>

        <!-- قائمة الحسابات المعفاة -->
        <div class="bg-slate-800 p-6 rounded-xl border border-slate-700 space-y-3">
            <h3 class="text-xl font-bold">قائمة الحسابات المجانية مدى الحياة:</h3>
            <ul class="list-disc pl-5">
                {users_list_html}
            </ul>
        </div>
    </section>
    """
    return layout("لوحة تحكم الأدمين - Instapulse AI", content, user=user)

@router.post("/add-free-user")
async def add_free_user(request: Request, target_email: str = Form(...)):
    """إضافة حساب مجاني جديد"""
    user = request.session.get("user")
    if not user or not user.get("is_admin"):
        raise HTTPException(status_code=403, detail="غير مصرح لك.")
    
    if target_email not in free_lifetime_users:
        free_lifetime_users.append(target_email)
        
    return RedirectResponse(url="/admin/dashboard", status_code=303)
