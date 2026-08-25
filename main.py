import os
import psycopg2
from psycopg2 import pool
from fastapi import FastAPI, Form, HTTPException, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(title="Instapulse AI - Instagram Edition")

# رابط الاتصال بقاعدة البيانات في Supabase
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:[YOUR-PASSWORD]@db.zfqtbdsbxzcvoktislgt.supabase.co:5432/postgres"
)

# نظام الاتصال السريع المباشر (Connection Pool)
try:
    db_pool = psycopg2.pool.ThreadedConnectionPool(2, 50, DATABASE_URL)
except Exception as e:
    print(f"خطأ في الاتصال بقاعدة البيانات: {e}")

def get_db():
    conn = db_pool.getconn()
    try:
        yield conn
    finally:
        db_pool.putconn(conn)

@app.on_event("startup")
def startup_db():
    """تهيئة الجداول مع دعم الحسابات المجانية المخصصة"""
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT UNIQUE NOT NULL,
                    username VARCHAR(100),
                    user_code VARCHAR(100),
                    status VARCHAR(20) DEFAULT 'active',
                    is_free BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE INDEX IF NOT EXISTS idx_users_id ON users(user_id);
                CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
                CREATE INDEX IF NOT EXISTS idx_users_is_free ON users(is_free);
            """)
            conn.commit()
    finally:
        db_pool.putconn(conn)

# ==========================================
# 1. واجهة التسجيل بتصميم انستغرام (داكن / فاتح)
# ==========================================
@app.get("/", response_class=HTMLResponse)
def home_page():
    return """
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instapulse AI - تسجيل الدخول والتفعيل</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --bg-color: #000000;
                --card-bg: #121212;
                --text-color: #f5f5f5;
                --subtext-color: #a8a8a8;
                --border-color: #262626;
                --input-bg: #121212;
                --btn-bg: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
                --qi-card-bg: #1e1e1e;
            }

            [data-theme="light"] {
                --bg-color: #fafafa;
                --card-bg: #ffffff;
                --text-color: #262626;
                --subtext-color: #8e8e8e;
                --border-color: #dbdbdb;
                --input-bg: #fafafa;
                --btn-bg: #0095f6;
                --qi-card-bg: #f0fdf4;
            }

            * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; transition: background 0.3s, color 0.3s; }
            body { background-color: var(--bg-color); color: var(--text-color); display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
            
            .theme-toggle { position: absolute; top: 20px; left: 20px; background: var(--card-bg); border: 1px solid var(--border-color); color: var(--text-color); padding: 10px 16px; border-radius: 20px; cursor: pointer; font-weight: bold; display: flex; align-items: center; gap: 8px; }
            
            .container { background-color: var(--card-bg); border: 1px solid var(--border-color); padding: 40px; border-radius: 12px; width: 100%; max-width: 380px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
            .logo { font-size: 32px; font-weight: 800; margin-bottom: 20px; background: var(--btn-bg); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            
            .payment-box { background: var(--qi-card-bg); border: 1px dashed #10b981; border-radius: 8px; padding: 12px; margin-bottom: 20px; text-align: right; font-size: 13px; color: var(--text-color); }
            .payment-box strong { color: #10b981; font-size: 15px; display: block; margin-top: 4px; direction: ltr; text-align: center; }
            
            .form-group { margin-bottom: 12px; }
            input { width: 100%; padding: 12px; background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 6px; color: var(--text-color); font-size: 14px; outline: none; }
            input:focus { border-color: #a8a8a8; }
            
            button.submit-btn { width: 100%; padding: 12px; background: var(--btn-bg); color: white; border: none; border-radius: 8px; font-weight: bold; font-size: 14px; cursor: pointer; margin-top: 10px; }
            button.submit-btn:hover { opacity: 0.9; }
            
            .footer-text { font-size: 12px; color: var(--subtext-color); margin-top: 25px; }
        </style>
    </head>
    <body>
        <button class="theme-toggle" onclick="toggleTheme()">
            <i class="fa-solid fa-circle-half-stroke"></i> <span id="theme-text">الوضع الفاتح</span>
        </button>

        <div class="container">
            <div class="logo">Instapulse AI</div>
            
            <!-- قسم تعليمات الدفع برقم الـ Ki Card الخاص بك -->
            <div class="payment-box">
                <i class="fa-solid fa-credit-card" style="color:#10b981;"></i> <strong>للحصول على كود التفعيل:</strong>
                قم بتحويل مبلغ الاشتراك إلى حساب الـ Ki Card الخاص بنا:
                <strong>3397630066</strong>
            </div>

            <form action="/register" method="post">
                <div class="form-group">
                    <input type="number" name="user_id" placeholder="معرف المستخدم (User ID)" required />
                </div>
                <div class="form-group">
                    <input type="text" name="username" placeholder="اسم حساب الانستغرام (Username)" required />
                </div>
                <div class="form-group">
                    <input type="text" name="user_code" placeholder="كود الاشتراك (أو اتركه إذا حسابك مجاني)" />
                </div>
                <button type="submit" class="submit-btn">تفعيل الحساب الآن</button>
            </form>
            
            <div class="footer-text">تصميم واجهة انستغرام الحديثة © 2026</div>
        </div>

        <script>
            function toggleTheme() {
                const body = document.body;
                const themeText = document.getElementById('theme-text');
                if (body.getAttribute('data-theme') === 'light') {
                    body.removeAttribute('data-theme');
                    themeText.innerText = 'الوضع الفاتح';
                } else {
                    body.setAttribute('data-theme', 'light');
                    themeText.innerText = 'الوضع الداكن';
                }
            }
        </script>
    </body>
    </html>
    """

@app.post("/register")
def register_user(user_id: int = Form(...), username: str = Form(...), user_code: str = Form(None), db=Depends(get_db)):
    try:
        with db.cursor() as cur:
            # التحقق هل الحساب مضاف مسبقاً كحساب مجاني من قبل الأدمن
            cur.execute("SELECT is_free FROM users WHERE user_id = %s OR username = %s;", (user_id, username))
            existing_user = cur.fetchone()

            is_free_status = False
            if existing_user and existing_user[0] is True:
                is_free_status = True
            elif not user_code or user_code.strip() == "":
                # إذا لم يدخل كود ولم يكن مخصصاً كمجاني
                return HTMLResponse("""
                    <body style="background:#000;color:#ef4444;text-align:center;padding-top:80px;font-family:sans-serif;">
                        <h2>❌ ينبغي إدخال كود اشتراك أو التواصل مع الأدمن لتخصيص حسابك مجاناً!</h2>
                        <p style="color:#aaa;">رقم التحويل للـ Ki Card: 3397630066</p>
                        <a href="/" style="color:#0095f6;">العودة للخلف</a>
                    </body>
                """)

            cur.execute("""
                INSERT INTO users (user_id, username, user_code, is_free) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE 
                SET username = EXCLUDED.username, 
                    user_code = COALESCE(EXCLUDED.user_code, users.user_code),
                    is_free = users.is_free OR EXCLUDED.is_free;
            """, (user_id, username, user_code, is_free_status))
            db.commit()

        return HTMLResponse("""
            <body style="background:#000;color:#10b981;text-align:center;padding-top:80px;font-family:sans-serif;">
                <h1>✅ تم تفعيل حسابك بنجاح!</h1>
                <p style="color:#aaa;">أهلاً بك في منصة Instapulse AI</p>
                <a href="/" style="color:#0095f6;text-decoration:none;font-weight:bold;">العودة للرئيسية</a>
            </body>
        """)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"خطأ في عملية التسجيل: {str(e)}")

# ==========================================
# 2. لوحة تحكم الأدمن المتقدمة (إضافة حسابات مجانية)
# ==========================================
@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard(db=Depends(get_db)):
    with db.cursor() as cur:
        # إحصائيات
        cur.execute("SELECT COUNT(*) FROM users;")
        total_users = cur.fetchone()[0]
        
        cur.execute("SELECT COUNT(*) FROM users WHERE is_free = TRUE;")
        free_users_count = cur.fetchone()[0]

        # جلب أحدث المشتركين
        cur.execute("SELECT user_id, username, user_code, is_free, created_at FROM users ORDER BY id DESC LIMIT 50;")
        recent_users = cur.fetchall()

    rows_html = ""
    for u in recent_users:
        type_badge = '<span style="background:#10b98122;color:#10b981;padding:4px 8px;border-radius:12px;font-weight:bold;">مجاني (VIP)</span>' if u[3] else '<span style="background:#3b82f622;color:#3b82f6;padding:4px 8px;border-radius:12px;">مشترك بكود</span>'
        date_str = str(u[4])[:19] if u[4] else "غير محدد"
        rows_html += f"""
        <tr>
            <td><code>{u[0]}</code></td>
            <td><strong>@{u[1]}</strong></td>
            <td><span style="background:#1e293b;padding:4px 8px;border-radius:4px;color:#f5f5f5;">{u[2] if u[2] else 'بدون كود'}</span></td>
            <td>{type_badge}</td>
            <td style="color:#a8a8a8;">{date_str}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>لوحة الأدمن - Instapulse Instagram Edition</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {{ --bg: #000; --card: #121212; --text: #fff; --border: #262626; }}
            [data-theme="light"] {{ --bg: #fafafa; --card: #fff; --text: #262626; --border: #dbdbdb; }}
            body {{ background: var(--bg); color: var(--text); font-family: system-ui, sans-serif; padding: 30px; margin: 0; transition: 0.3s; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; border-bottom: 1px solid var(--border); padding-bottom: 20px; }}
            .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }}
            .card {{ background: var(--card); border: 1px solid var(--border); padding: 20px; border-radius: 12px; text-align: center; }}
            .card h3 {{ margin: 0; font-size: 14px; color: #8e8e8e; }}
            .card .num {{ font-size: 36px; font-weight: bold; color: #0095f6; margin-top: 8px; }}
            
            .free-user-form {{ background: var(--card); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-bottom: 30px; }}
            .free-user-form input {{ padding: 10px; background: var(--bg); border: 1px solid var(--border); color: var(--text); border-radius: 6px; margin-left: 10px; width: 200px; }}
            .free-user-form button {{ padding: 10px 20px; background: #10b981; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
            
            table {{ width: 100%; border-collapse: collapse; background: var(--card); border-radius: 12px; overflow: hidden; border: 1px solid var(--border); }}
            th, td {{ padding: 14px; text-align: right; border-bottom: 1px solid var(--border); font-size: 14px; }}
            th {{ background: var(--border); color: var(--text); }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛡️ لوحة إدارتك المركزية (Instagram Standard)</h1>
            <button onclick="document.body.classList.toggle('light-mode'); document.body.setAttribute('data-theme', document.body.getAttribute('data-theme')==='light'?'dark':'light');" style="padding:8px 16px; border-radius:8px; cursor:pointer;">💡 تغيير المظهر</button>
        </div>

        <div class="stats-grid">
            <div class="card">
                <h3>إجمالي الحسابات المسجلة</h3>
                <div class="num">{total_users:,}</div>
            </div>
            <div class="card">
                <h3>الحسابات المجانية المخصصة (VIP)</h3>
                <div class="num" style="color:#10b981;">{free_users_count:,}</div>
            </div>
            <div class="card">
                <h3>رقم الـ Ki Card الحالي</h3>
                <div class="num" style="font-size:18px; color:#e6683c; margin-top:15px;">3397630066</div>
            </div>
        </div>

        <!-- إضافة حساب مجاني بدون كود -->
        <div class="free-user-form">
            <h3 style="margin-top:0; color:#10b981;"><i class="fa-solid fa-user-plus"></i> تخصيص حساب مجاني (استثناء بدون كود)</h3>
            <form action="/admin/add-free-user" method="post" style="display:flex; flex-wrap:wrap; gap:10px; align-items:center;">
                <input type="number" name="user_id" placeholder="User ID" required />
                <input type="text" name="username" placeholder="اسم حساب الانستغرام" required />
                <button type="submit">إضافة كـ حساب مجاني VIP</button>
            </form>
        </div>

        <h2>جدول جميع الحسابات المسجلة</h2>
        <table>
            <thead>
                <tr>
                    <th>معرف المستخدم (ID)</th>
                    <th>اسم حساب انستغرام</th>
                    <th>الكود المستعمل</th>
                    <th>نوع الاشتراك</th>
                    <th>تاريخ الإضافة</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </body>
    </html>
    """

# إضافة حساب مجاني مباشر من الأدمن
@app.post("/admin/add-free-user")
def add_free_user(user_id: int = Form(...), username: str = Form(...), db=Depends(get_db)):
    try:
        with db.cursor() as cur:
            cur.execute("""
                INSERT INTO users (user_id, username, user_code, is_free)
                VALUES (%s, %s, 'FREE_VIP_ACCOUNT', TRUE)
                ON CONFLICT (user_id) DO UPDATE SET is_free = TRUE, username = EXCLUDED.username;
            """, (user_id, username))
            db.commit()
        return RedirectResponse(url="/admin", status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"خطأ أثناء إضافة الحساب المجاني: {str(e)}")
