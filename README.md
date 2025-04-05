# 🚀 SimpleAPIServer

FastAPI 기반의 간단한 API 서버입니다.  

---

## 📦 프로젝트 설치 및 실행 (Installation & Setup)

### 1. 가상환경 생성 및 종속성 설치 (Create Python Virtual Environment)

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
source venv/bin/activate        # Windows: venv\Scripts\activate

# 종속성 설치
pip install -r requirements.txt
```

> `requirements.txt`가 없다면 직접 설치:
> ```bash
> pip install fastapi uvicorn
> ```

---

### 2. PM2 설치 및 설정 (Install and Setup PM2)

```bash
# Node.js 설치 (Ubuntu 예시)
sudo apt update
sudo apt install nodejs npm

# PM2 전역 설치
npm install -g pm2
```

> ❗ PM2는 Node.js 기반 도구이기 때문에 `node`와 `npm`이 반드시 필요합니다.

---

## 🚀 FastAPI 앱 PM2로 실행하기 (Run FastAPI App with PM2)

터미널을 닫아도 서버가 종료되지 않도록 백그라운드 실행하며, 로그 모니터링과 재시작, 재부팅 자동 실행까지 지원합니다.

---

### ✅ 방법 1: ecosystem.config.js 파일 사용 (Using ecosystem config file)

#### 📄 ecosystem.config.js 예시

```javascript
// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: "SimpleAPIServer",
      script: "./venv/bin/uvicorn",
      args: "main:app --host 0.0.0.0 --port 8000",
      interpreter: "none",
    },
  ],
};

```

#### 실행

```bash
pm2 start ecosystem.config.js
```


---

## 🔧 PM2 명령어 정리 (PM2 Command Summary)

| 기능                | 명령어                                      |
|-------------------|-------------------------------------------|
| 상태 확인           | `pm2 status`                              |
| 실시간 로그 확인     | `pm2 logs`                                |
| 대시보드 로그 모니터링 | `pm2 monit`                               |
| 앱 재시작           | `pm2 restart SimpleAPIServer`             |
| 앱 중단            | `pm2 stop SimpleAPIServer`                |
| 앱 삭제            | `pm2 delete SimpleAPIServer`              |
| 전체 앱 중지        | `pm2 stop all`                            |
| 전체 앱 삭제        | `pm2 delete all`                          |
| 현재 상태 저장       | `pm2 save`                                |

---

## 🔄 부팅 시 자동 실행 설정 (Auto-start on System Boot)

서버 재부팅 시 자동으로 FastAPI 앱이 실행되도록 설정합니다.

```bash
pm2 startup
pm2 save
```

> `pm2 startup` 실행 후 표시되는 명령어(예: `sudo env PATH=$PATH ...`)를 복사하여 터미널에 한 번 실행해야 합니다.

---

## 📁 프로젝트 구조 예시 (Project Structure Example)

```
SimpleAPIServer/
├── main.py
├── venv/
├── requirements.txt
├── ecosystem.config.js
└── README.md
```

