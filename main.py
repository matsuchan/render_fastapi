from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1 style="background-color: #00ff00;">見出しレベル1</h1>
  <h2 style="color: #ffffff; background-color: #00ff00;">見出しレベル2</h2>
  <p style="color: #ff0000">あいうえお</p>
  <h2 style="color: #ffffff; background-color: #00ff00;">見出しレベル2</h2>
  <p style="color: #ff0000">かきくけこ</p>
  <a href="https://www.google.co.jp/" title="検索">ググる</a>
</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)