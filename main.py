import os
from fastapi import FastAPI
import requests

app = FastAPI()

GITHUB_JSON_URL = "https://raw.githubusercontent.com/JunyeongYun-0118/-source/main/sources.json"

def fetch_github_json():
    response = requests.get(GITHUB_JSON_URL)
    if response.status_code == 200:
        try:
            return response.json()
        except Exception as e:
            return {"error": "Invalid JSON format", "details": str(e)}
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

@app.get("/sources")  # <-- 반드시 존재해야 함!
async def get_sources():
    return fetch_github_json()

# 🚀 Render에서 실행할 때 포트 설정을 자동으로 받도록 설정
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))  # Render의 환경 변수를 사용!
    uvicorn.run(app, host="0.0.0.0", port=port)
