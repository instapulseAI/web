# templates.py

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
                darkMode: 'media',
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
