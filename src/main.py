from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.v1.router import router as api_v1_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="FastAPI project with structured project layout",
    version="1.0.0"
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(api_v1_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", 
        host=settings.API_HOST, 
        port=settings.API_PORT, 
        reload=settings.API_RELOAD
    ) 