import os
import requests
from fastapi import FastAPI
from typing import Dict, Any
from pydantic import BaseModel

app = FastAPI()

GITHUB_JSON_URL = "https://raw.githubusercontent.com/JunyeongYun-0118/-source/main/sources.json"

# ✅ FastAPI 문서에 JSON 예시를 추가하기 위해 Pydantic 모델 사용!
class SourceResponse(BaseModel):
    example_data: Dict[str, Any]

def fetch_github_json() -> Dict[str, Any]:
    response = requests.get(GITHUB_JSON_URL)

    if response.status_code == 200:
        try:
            data = response.json()
            return {"example_data": data}  # ✅ JSON 데이터를 Pydantic 모델 형식으로 감싸기!
        except Exception as e:
            return {"example_data": {"error": "Invalid JSON format", "details": str(e)}}
    else:
        return {"example_data": {"error": "Failed to fetch data", "status_code": response.status_code}}

@app.get("/sources", response_model=SourceResponse)  # ✅ FastAPI 문서에서 JSON 예시가 올바르게 표시되도록 설정!
async def get_sources():
    return fetch_github_json()

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
