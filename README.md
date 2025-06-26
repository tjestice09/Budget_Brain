# Budget Brain
A personal finance chatbot demo using FastAPI and an optional (preferred) OPENAI

## Features 
- Chat web app with simple UI
- Runs in mock mode (no LLM required)
- Optional real OPENAI server mode interaction
- Easy to switch modes for demo, production, or fun use

## Project Structure Update
- Modular backend logic: Main chat/budget logic moved to utils/reply_logic.py
- Automated tests: All core logic is now tested in tests/test_reply_logic.py

## Setup
1. **Clone the repo:**
- Copy this into your terminal:
- git clone https://github.com/YOUR_USERNAME/Budget_Brain.git...make sure you enter your actual username
- cd Budget_Brain

2. **Install requirements:**
- Run this command:
- pip install -r requirements.txt

3. **(Optional) For real AI interaction mode:** 
- Create a '.env' file with your Open API key inside from the OpenAI website 
- Get your OpenAi key from [OpenAI Website](https://platform.openai.com/api-keys)
- put this in your '.env' file:
    ```
    OPENAI_API_KEY=(your actual API key..)
    ```

4. **Start the server**
```

uvicorn main:app --reload
```

5. **Open your browser at:**
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Switching Between Mock Mode and OpenAI

- The app defaults to mock mode (It has a small amount of hardwired replies).
- To enable OpenAI replies:
- Install 'openai' (already in requirements.txt)
- Add your API key to '.env'
- Set 'USE_OPENAI = True' near the top of 'main.py'

---

## License

MIT License. Use Freely!

---

*Created by Tommmy Jestice*
