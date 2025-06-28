# Roblox Backend FastAPI

A simple, modular, and async-ready backend API using FastAPI for Roblox game integrations. Built with clean structure, CORS + GZip middleware, and MySQL async pooling using aiomysql.

## 📁 Project Structure

```bash
.
├── app.py                # FastAPI app entrypoint
├── router.py             # All routers registered here
├── .env                  # Environment variables
├── models/               # Response schemas
│   └── ResponseModel.py
├── api/                  # API routes
│   ├── ping.py
│   ├── test.py
│   └── playerjoin.py
└── test/                 # Test scripts
    └── TestAsyncRequest.py
```

---

## 🚀 Getting Started

1. Clone repository
```bash
git clone https://github.com/superevilstockholm/Roblox-Backend-FastAPI.git
cd Roblox-Backend-FastAPI
```
2. Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt # or pip install fastapi pydantic aiomysql aiohttp dotenv
```
3. Create .env file
```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=my_db
```
| You can also use .env.example as reference with `cp .env.example .env`
4. Run the API
```bash
uvicorn app:app --reload --port 23237 # or python -m uvicorn app:app --reload --port 23237
```

---

## ✅ Features

- 🌐 CORS enabled for all origins
- 🗜️ GZip middleware for better performance
- ⚡ Async I/O compatible
- 🧩 Modular routing
- 🐬 Uses aiomysql with connection pooling

---

## 📦 Main Dependencies

- FastAPI
- aiohttp
- aiomysql
- python-dotenv
- Uvicorn

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or improve.

---

Made with ❤️ by superevilstockholm  
Inspired by the need for fast Roblox game integrations.