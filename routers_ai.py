import os
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from google import genai
from templates import layout

router = APIRouter(prefix="/ai", tags=["AI Generation"])

@router.post("/generate-caption", response_class=HTMLResponse)
async def generate_caption(request: Request, topic: str = Form(...), tone: str = Form("حماسي")):
    """توليد كابشن وأفكار منشورات باستخدام الذكاء الاصطناعي"""
    user = request.session.get("user")
    
    # حماية المسار: التأكد من تسجيل الدخول
    if not user:
        return RedirectResponse(url="/auth/login/google", status_code=303)
        
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is missing in Railway environment variables.")

    try:
        # استدعاء نموذج Gemini الرسمي
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
        أنت خبير في تسويق إنستغرام وإنشاء المحتوى الجذاب.
        قم بكتابة كابشن احترافي لمنشور إنستغرام حول الموضوع التالي: '{topic}'.
        نبرة الصوت المطلوبة: {tone}.
        
        يرجى تقديم الإجابة مقسمة كالتالي:
        1. ✍️ الكابشن الرئيسي (جذاب ومشوق للجمهور).
        2. 🎯 دعوة لاتخاذ إجراء (Call to Action - CTA).
        3. 🏷️ قائمة بأفضل 10 هاشتاغات ذات تفاعل عالٍ ومناسبة للموضوع.
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
        except Exception:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt,
            )
        
        ai_result = response.text.replace("\n", "<br>")
        
    except Exception as e:
        ai_result = f"حدث خطأ أثناء التواصل مع الذكاء الاصطناعي: {str(e)}"

    content = f"""
    <section class="py-8 space-y-6 max-w-3xl mx-auto">
        <a href="/dashboard" class="text-blue-400 hover:underline flex items-center space-x-2 space-x-reverse mb-4">
            <span>← العودة للوحة التحكم</span>
        </a>

        <div class="bg-slate-800 p-6 rounded-2xl border border-slate-700 space-y-4">
            <h2 class="text-2xl font-bold text-blue-400">✨ نتيجة الذكاء الاصطناعي</h2>
            <div class="p-4 bg-slate-900 rounded-xl text-slate-200 leading-relaxed border border-slate-800">
                {ai_result}
            </div>
            <div class="pt-4">
                <a href="/dashboard" class="inline-block bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-xl transition">
                    توليد محتوى جديد
                </a>
            </div>
        </div>
    </section>
    """
    return layout("نتيجة الـ AI - Instapulse AI", content, user=user)
