import os
from fastapi import FastAPI, Form, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Instapulse AI - Instagram Edition")

# قاعدة بيانات مؤقتة في الذاكرة لتخزين الحسابات والاشتراكات
db_accounts = [
    {"username": "brand_official", "status": "نشط", "subscribed": True},
    {"username": "personal_test", "status": "مستثنى", "subscribed": False}
]

# الواجهة الرئيسية المكتملة للتطبيق
HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instapulse AI | منصة إدارة واشتراكات إنستغرام</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --ig-primary: #833ab4;
            --ig-gradient: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            --bg-dark: #0f1419;
            --card-bg: #1a202c;
            --text-color: #f7fafc;
            --border-color: #2d3748;
        }
        body {
            font-family: 'Tajawal', sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            padding: 20px 0;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 30px;
        }
        .header h1 {
            background: var(--ig-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            margin: 0;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 20px;
        }
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
        }
        .card h2 {
            margin-top: 0;
            font-size: 1.3rem;
            color: #e2e8f0;
            border-bottom: 2px solid #319795;
            padding-bottom: 8px;
            display: inline-block;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-size: 0.9rem;
            color: #a0aec0;
        }
        input, select {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background-color: #2d3748;
            color: white;
            box-sizing: border-box;
            font-family: inherit;
        }
        .btn {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background: var(--ig-gradient);
            color: white;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: opacity 0.2s;
        }
        .btn:hover {
            opacity: 0.9;
        }
        .account-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px;
            background: #2d3748;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .status-badge {
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .status-active { background: #276749; color: #9ae6b4; }
        .status-excluded { background: #742a2a; color: #feb2b2; }
        .btn-toggle {
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.8rem;
            background: #4a5568;
            color: white;
        }
        .price-tag {
            font-size: 1.8rem;
            font-weight: bold;
            color: #38b2ac;
            text-align: center;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Instapulse AI</h1>
            <p>منصة أتمتة حسابات إنستغرام والدفع الإلكتروني المباشر</p>
        </div>

        <div class="grid">
            <!-- قسم الاشتراك والدفع -->
            <div class="card">
                <h2>🚀 الترقية والاشتراك الممتاز</h2>
                <div class="price-tag">$29 / شهرياً</div>
                <form id="paymentForm">
                    <div class="form-group">
                        <label>الاسم الكامل علي البطاقة</label>
                        <input type="text" id="cardHolder" placeholder="John Doe" required>
                    </div>
                    <div class="form-group">
                        <label>رقم البطاقة البنكية (Visa / MasterCard)</label>
                        <input type="text" id="cardNumber" placeholder="4532 •••• •••• 8890" maxlength="19" required>
                    </div>
                    <div style="display: flex; gap: 10px;">
                        <div class="form-group" style="flex: 1;">
                            <label>تاريخ الانتهاء</label>
                            <input type="text" id="cardExp" placeholder="MM/YY" maxlength="5" required>
                        </div>
                        <div class="form-group" style="flex: 1;">
                            <label>رمز الأمان (CVC)</label>
                            <input type="password" id="cardCvc" placeholder="123" maxlength="3" required>
                        </div>
                    </div>
                    <button type="submit" class="btn">تأكيد الاشتراك والدفع الآن</button>
                </form>
            </div>

            <!-- قسم إدارة وتخصيص الحسابات -->
            <div class="card">
                <h2>📸 إدارة حسابات إنستغرام</h2>
                
                <form id="addAccountForm" style="margin-bottom: 20px;">
                    <div class="form-group">
                        <label>إضافة حساب إنستغرام جديد</label>
                        <input type="text" id="newUsername" placeholder="اسم المستخدم بدون @" required>
                    </div>
                    <button type="submit" class="btn" style="background: #319795;">إضافة الحساب</button>
                </form>

                <label>الحسابات المسجلة وحالتها:</label>
                <div id="accountsList">
                    <!-- سيتم تحميل الحسابات ديناميكياً -->
                </div>
            </div>
        </div>
    </div>

    <script>
        // تحميل قائمة الحسابات
        async function loadAccounts() {
            const res = await fetch('/api/accounts');
            const data = await res.json();
            const list = document.getElementById('accountsList');
            list.innerHTML = '';
            
            data.forEach(acc => {
                const badgeClass = acc.subscribed ? 'status-active' : 'status-excluded';
                const statusText = acc.subscribed ? 'مشترك' : 'مستثنى';
                const actionText = acc.subscribed ? 'استثناء' : 'تفعيل';
                
                list.innerHTML += `
                    <div class="account-item">
                        <div>
                            <strong>@${acc.username}</strong>
                            <span class="status-badge ${badgeClass}" style="margin-right: 8px;">${statusText}</span>
                        </div>
                        <button class="btn-toggle" onclick="toggleAccount('${acc.username}')">${actionText}</button>
                    </div>
                `;
            });
        }

        // إضافة حساب جديد
        document.getElementById('addAccountForm').onsubmit = async (e) => {
            e.preventDefault();
            const username = document.getElementById('newUsername').value;
            await fetch('/api/accounts/add', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: `username=${encodeURIComponent(username)}`
            });
            document.getElementById('newUsername').value = '';
            loadAccounts();
        };

        // تبديل حالة الحساب (إضافة/استثناء من الاشتراك)
        async function toggleAccount(username) {
            await fetch('/api/accounts/toggle', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: `username=${encodeURIComponent(username)}`
            });
            loadAccounts();
        }

        // معالجة معاوضة الدفع والاشتراك
        document.getElementById('paymentForm').onsubmit = async (e) => {
            e.preventDefault();
            alert('تم استلام بيانات الاشتراك والبطاقة بنجاح! سيتم تفعيل الحسابات الفعالة فوراً.');
        };

        loadAccounts();
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    return HTML_LAYOUT

@app.get("/api/accounts")
async def get_accounts():
    return db_accounts

@app.post("/api/accounts/add")
async def add_account(username: str = Form(...)):
    db_accounts.append({"username": username, "status": "نشط", "subscribed": True})
    return {"message": "Success"}

@app.post("/api/accounts/toggle")
async def toggle_account(username: str = Form(...)):
    for acc in db_accounts:
        if acc["username"] == username:
            acc["subscribed"] = not acc["subscribed"]
            acc["status"] = "نشط" if acc["subscribed"] else "مستثنى"
            break
    return {"message": "Toggled"}
