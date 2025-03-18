from fastapi import FastAPI
import requests

app = FastAPI()

GITHUB_JSON_URL = "https://raw.githubusercontent.com/JunyeongYun-0118/-source/main/sources.json"

# 깃허브에서 데이터를 가져오고, 실패하면 오류 메시지를 출력
def fetch_github_json():
    response = requests.get(GITHUB_JSON_URL)
    if response.status_code == 200:
        try:
            return response.json()  # JSON 데이터 반환
        except Exception as e:
            return {"error": "Invalid JSON format", "details": str(e)}
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

@app.get("/sources")
async def get_sources():
    return fetch_github_json()
