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
Sure! Here's a more polished and engaging version of the **Contributing** section, with clearer formatting and friendlier tone:

---

## 🤝 **Contributing**

We’re all about collaboration — and we’d love to have you contribute to **StockWise**!

Whether it's fixing a bug, adding a new feature, improving the UI, or sharing an idea — every contribution counts. Here’s how you can get started:

### 🛠️ Steps to Contribute

1. **Fork** this repository to your GitHub account.  
2. **Clone** your forked repo locally:
   ```bash
   git clone https://github.com/your-username/stockwise.git
   ```
3. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature-yourFeatureName
   ```
4. **Make your changes** and **commit** them:
   ```bash
   git commit -m "✨ Add [your feature description]"
   ```
5. **Push** your branch to your fork:
   ```bash
   git push origin feature-yourFeatureName
   ```
6. **Open a Pull Request** on the main repository with a brief description of your changes.

---

### 💡 Suggestions, Issues & Ideas?

Found a bug? Have a cool idea or feedback?  
Feel free to [open an issue](#) or start a discussion — we’re all ears!

---

Together, we can make StockWise even smarter! 🚀

