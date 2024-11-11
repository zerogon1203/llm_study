# LLM & PyTorch 학습 프로젝트

FastAPI 기반의 LLM(Large Language Model)과 PyTorch를 활용한 머신러닝 학습 프로젝트입니다.

## 🚀 기술 스택

- Python 3.12.7
- FastAPI 0.110.0
- PyTorch 2.5.1
- TorchVision 0.20.1
- Uvicorn 0.27.1

## 🗂️ 프로젝트 구조
project_root/
├── src/
│ ├── api/
│ │ ├── init.py
│ │ └── v1/
│ │ ├── init.py
│ │ └── router.py
│ ├── controllers/
│ │ ├── init.py
│ │ └── health_controller.py
│ ├── services/
│ │ ├── init.py
│ │ └── health_service.py
│ ├── core/
│ │ ├── init.py
│ │ └── config.py
│ └── main.py
├── tests/
│ └── init.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


## 🛠️ 설치 방법

1. 프로젝트 클론
   ```bash
   git clone [repository_url]
   cd [project_name]
   ```
2. 가상환경 생성 및 활성화
   ```bash
   python -m venv .venv
   source .venv/bin/activate #windows: .venv\Scripts\activate
   ```
3. 필요 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```
4. 환경 변수 설정
   ```bash
   cp .env.example .env
   ```
    .env 파일을 열어서 필요한 설정 수정

## 🚀 실행 방법

1. 서버 실행
   ```bash
   cd src
   python main.py
   ```
서버가 실행되면 다음 URL에서 확인 가능합니다:
- API 문서: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📚 주요 기능

### 현재 구현된 기능
- 기본적인 API 서버 구조
- Health Check API
- 환경 설정 관리

### 예정된 기능
- LLM 모델 학습 및 추론
- PyTorch 기반 머신러닝 모델 구현
- 모델 학습 결과 시각화
- 모델 성능 평가

## 📝 API 문서

### Health Check
- GET `/api/v1/health`: 서버 상태 확인
- GET `/api/v1/`: 웰컴 메시지

## 🔧 개발 환경 설정

### 필수 요구사항
- Python 3.12.7 이상
- CUDA 지원 GPU (PyTorch 사용시 권장)

### IDE 설정
- VSCode 사용시 Python, Pylance 확장 설치 권장
- Python 인터프리터를 가상환경의 Python으로 설정

## 🤝 기여 방법

1. 프로젝트 Fork
2. 새로운 Feature 브랜치 생성
3. 변경사항 Commit
4. 브랜치에 Push
5. Pull Request 생성

## 📜 라이센스

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 📞 문의사항

프로젝트에 대한 문의사항이나 버그 리포트는 GitHub Issues를 통해 남겨주세요.