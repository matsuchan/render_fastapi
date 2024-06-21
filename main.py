from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

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
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="bootstrap.css">
</head>
<body>
  <header style="background-color:#C0C0C0"></header>
  <div class="container-fluid text-white">
    <div class="row g-0">
      <div class="d-flex flex-row-reverse">
      <div class="card mt-2 mb-2 p-2" style="max-width: 70px;">
            <img src="./img/AdobeStock_693723033_Preview.jpeg" class="img-fluid rounded-start" alt="user-1">
      </div>
    </div>

      <div class="list-group">
        <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
          ユーザーリスト
        </a>
      <li class="list-group-item">
        <div class="card mt-2 mb-2" style="max-width: 540px;">
          <div class="row g-0">
            <div class="col-md-4">
              <img src="./img/AdobeStock_715372169_Preview.png" class="img-fluid rounded-start" alt="user-1">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title">User-1</h5>
                <p class="card-text">相手のメッセージ:Test1</p>
                <p class="card-text"><small class="text-body-secondary">最後のメッセージ:3分前</small></p>
                <button type="button" class="btn btn-primary position-relative">
                  チャットを開く
                </button>
                <button type="button" class="btn btn-primary position-relative">
                  未読のメッセージ
                  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                    1
                    <span class="visually-hidden">unread messages</span>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="list-group-item">
        <div class="card mt-2 mb-2" style="max-width: 540px;">
          <div class="row g-0">
            <div class="col-md-4">
              <img src="./img/AdobeStock_717380354_Preview.png" class="img-fluid rounded-start" alt="user-1">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title">User-2</h5>
                <p class="card-text">こちらのメッセージ:Test2</p>
                <p class="card-text"><small class="text-body-secondary">最後のメッセージ:30分前</small></p>
                <button type="button" class="btn btn-primary position-relative">
                  チャットを開く
                </button>
                <button type="button" class="btn btn-primary position-relative">
                  未読のメッセージ
                  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                    3
                    <span class="visually-hidden">unread messages</span>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="list-group-item">
        <div class="card mt-2 mb-2" style="max-width: 540px;">
        <div class="row g-0">
          <div class="col-md-4">
            <img src="./img/AdobeStock_717351671_Preview.png" class="img-fluid rounded-start" alt="user-1">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">User-3</h5>
              <p class="card-text">相手のメッセージ:Test3</p>
              <p class="card-text"><small class="text-body-secondary">最後のメッセージ:3時間前</small></p>
              <button type="button" class="btn btn-primary position-relative">
                チャットを開く
              </button>
              <button type="button" class="btn btn-primary position-relative">
                未読のメッセージ
                <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                  4
                  <span class="visually-hidden">unread messages</span>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
      </li>
      </div>
      </div>
      </div>
    </div>
  </div>
</div>
</div>
  <footer style="background-color:#C0C0C0"></footer>
</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)