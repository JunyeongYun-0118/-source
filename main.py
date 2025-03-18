from fastapi import FastAPI
import requests

app = FastAPI()

GITHUB_JSON_URL = "https://raw.githubusercontent.com/JunyeongYun-0118/-source/main/sources.json"

# 깃허브에서 JSON 데이터 가져오기
def fetch_github_json():
    response = requests.get(GITHUB_JSON_URL)  
    if response.status_code == 200:
        return response.json()  # JSON 데이터 반환
    else:
        return {"error": "Failed to fetch data from GitHub"}

@app.get("/sources")
async def get_sources():
    return fetch_github_json()
