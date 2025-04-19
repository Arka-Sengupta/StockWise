# 📈 StockWise – Smart Indian Stock Market Companion

StockWise is a sleek, full-stack web application tailored for Indian stock market enthusiasts. It features live index tracking, AI-powered analysis, exchange comparisons, and a smart chatbot named **Mr. Market**, all wrapped in a modern, animated UI.

---

## 🚀 Features

- 📊 **Live Index Data** – Real-time updates for NIFTY 50, Bank NIFTY, and NIFTY IT indices.
- 📰 **Curated News Feed** – Top market news delivered via NewsAPI.
- 🔍 **Exchange Comparison** – View and analyze stock prices across NSE and BSE.
- 🤖 **Mr. Market Chatbot** – AI assistant powered by OpenRouter for stock-related queries.
- 🔐 **User Authentication** – Secure login and signup via Flask-Login.
- 🎨 **Glassmorphism UI** – Modern design using Bootstrap 5, Animate.css, and custom styling.

---

## 🧠 Technologies Used

**Frontend**
- HTML5, CSS3, JavaScript
- Bootstrap 5, Animate.css
- Chart.js

**Backend**
- Python 3
- Flask (with Blueprints)
- Flask-Login for auth
- Flask-SQLAlchemy for ORM
- OpenAI SDK (for OpenRouter)

**APIs**
- [OpenRouter](https://openrouter.ai/) – AI chatbot
- [NewsAPI](https://newsapi.org/) – News integration

---

## 🔧 Installation & Setup

### 📦 Required Python Packages

Before running StockWise, install the necessary packages:

```bash
pip install flask flask_sqlalchemy flask_login openai requests
git clone https://github.com/your-username/stockwise.git
cd stockwise
```

**Set API Keys**
In views.py, replace the NewsAPI key and OpenRouter key if needed

Run the app
```bash
python main.py
```
---

## 👥 Contributors

| Role | Contributors |
|----------|----------|
| 🧠 Frontend & Backend | Arka Sengupta & Saurish Chandra |
| 🎨 Graphics & UI Design | Saurish Chandra & Arka Sengupta |


---

## 🤝 Contributing

We love community contributions! To contribute:

Fork this repo.

Create a feature branch: git checkout -b feature-xyz

Commit your changes: git commit -am 'Add awesome feature'

Push the branch: git push origin feature-xyz

Submit a pull request 🚀

Suggestions, issues, and ideas are all welcome!

