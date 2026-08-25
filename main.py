import os
from fastapi import FastAPI, Form, HTTPException, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(title="Instapulse AI - Instagram Edition")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Instapulse AI</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1 style="color: #4CAF50;">🚀 Instapulse AI is Online and Working!</h1>
            <p>السيرفر يعمل الآن بنجاح على منصة Railway.</p>
        </body>
    </html>
    """
