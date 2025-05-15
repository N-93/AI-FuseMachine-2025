# 💸 Investment Calculator API

A simple and modern API built with **FastAPI** that calculates the future value of an investment using compound interest. Designed to follow best practices including the 12-Factor App principles, containerization, and testing.

---

## 🚀 Features

- 📈 Calculate compound interest
- ⚙️ Environment variable-based configuration
- 📁 Clean project structure
- 🧪 Basic test with pytest
- 🐳 Docker support
- 🧰 Swagger docs with FastAPI

---

## 🧮 How It Works

Send a POST request with investment data:

```json
{
  "principal": 1000,
  "rate": 0.05,
  "time": 3
}

You’ll receive:
{
  "total": 1157.63
}
Formula used: A = P × (1 + r)^t


Set up a virtual environment

python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate


pip install -r requirements.txt


 Run the app
uvicorn app.main:app --reload

Open in browser: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs


Running Test
pytest