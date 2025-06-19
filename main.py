from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": ""})

USE_OPENAI = False

@app.post("/chat")
async def chat(request: Request, message: str = Form(...)):
    if USE_OPENAI:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Budget Brain, an expert financial assistant."},
                    {"role": "user", "content": message},
                ],
                max_tokens=150
            )
            reply = response.choices[0].message['content'].strip()
        except Exception as e:
            reply = f"Sorry, there was an error: {e}"
    else:
        if "groceries" in message.lower():
            reply = "Budget Brain: The groceries should be about 15 percent of your budget..please budget wisely."
        elif "spend" in message.lower():
            reply = "Budget Brain: You spent $150 this week on groceries."
        elif "save" in message.lower():
            reply = "Budget Brain: You saved $200 this week..way to go!"
        else:
            reply = "Can you repeat that? I didn't understand your message."
    return templates.TemplateResponse("index.html", {"request": request, "message": reply})