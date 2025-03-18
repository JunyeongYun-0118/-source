import os
from fastapi import FastAPI
import requests

app = FastAPI()

GITHUB_JSON_URL = "https://raw.githubusercontent.com/JunyeongYun-0118/-source/main/sources.json"

def fetch_github_json():
    response = requests.get(GITHUB_JSON_URL)  
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from GitHub"}

@app.get("/sources")
async def get_sources():
    return fetch_github_json()

# 서버 실행 코드
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Render에서 자동으로 포트 설정
    uvicorn.run(app, host="0.0.0.0", port=port)
