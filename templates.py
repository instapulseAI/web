def layout(title: str, content: str, user=None) -> str:
    """الهيكل العام والتصميم الموحد لصفحات المنصة"""
    
    # الجزء الخاص بزر تسجيل الدخول أو صورة المستخدم في الهيدر
    if user:
        nav_user_part = f"""
        <div class="flex items-center space-x-4 space-x-reverse">
            <span class="text-slate-300 font-medium text-sm">{user.get('name', 'المستخدم')}</span>
            <a href="/dashboard" class="text-xs bg-blue-600 hover:bg-blue-700 text-white px-3 py-1.5 rounded-lg transition">لوحة التحكم</a>
            <a href="/auth/logout" class="text-xs text-red-400 hover:text-red-300 transition">خروج</a>
        </div>
        """
    else:
        nav_user_part = """
        <div class="flex items-center space-x-3 space-x-reverse">
            <a href="/admin/login" class="text-xs text-slate-400 hover:text-white transition">دخول الأدمن</a>
            <a href="/auth/login/google" class="bg-blue-600 hover:bg-blue-700 text-white text-sm px-4 py-2 rounded-xl transition">تسجيل الدخول</a>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Tajawal', sans-serif;
        }}
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col justify-between">
    
    <!-- Header / Navigation -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="/" class="text-2xl font-bold text-blue-500">Instapulse <span class="text-white">AI</span></a>
            
            <nav class="hidden md:flex space-x-6 space-x-reverse text-slate-300 font-medium">
                <a href="/" class="hover:text-white transition">الرئيسية</a>
                <a href="/pricing" class="hover:text-white transition">الأسعار</a>
            </nav>

            {nav_user_part}
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-6xl mx-auto px-4 py-8 flex-grow w-full">
        {content}
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 py-6 text-center text-slate-500 text-sm">
        <p>© 2026 Instapulse AI - جميع الحقوق محفوظة.</p>
    </footer>

</body>
</html>
"""
