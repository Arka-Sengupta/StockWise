from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
import requests
from datetime import datetime

views = Blueprint('views', __name__)

# Fixed mock values with no random drift
def get_nse_index_data(symbol):
    mock_data = {
        "NIFTY_50": {
            "data": [{
                "lastPrice": "22800.45",
                "pChange": 0.95,
                "quantityTraded": "13458000"
            }]
        },
        "BANK_NIFTY": {
            "data": [{
                "lastPrice": "48750.20",
                "pChange": -0.42,
                "quantityTraded": "9800000"
            }]
        },
        "NIFTY_IT": {
            "data": [{
                "lastPrice": "34100.75",
                "pChange": 1.22,
                "quantityTraded": "5600000"
            }]
        }
    }

    return mock_data.get(symbol, None)

# NewsAPI fetcher
def fetch_stock_news():
    api_key = "eda84e16e2da442eb1d883146df0e7c4"  #Change your API key
    url = f"https://newsapi.org/v2/everything?q=indian+stock+market&language=en&sortBy=publishedAt&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return articles[:5]  # return top 5
    except Exception as e:
        current_app.logger.error(f"News API Error: {e}")
        return []

# Main dashboard route
@views.route('/user-details')
@login_required
def user_details():
    return render_template("user-details.html", user=current_user)
@views.route('/')
@login_required
def home():
    market_data = {
        "NIFTY_50": get_nse_index_data("NIFTY_50"),
        "BANK_NIFTY": get_nse_index_data("BANK_NIFTY"),
        "NIFTY_IT": get_nse_index_data("NIFTY_IT")
    }

    news_articles = fetch_stock_news()

    return render_template(
        "home.html",
        user=current_user,
        market_data=market_data,
        news_articles=news_articles,
        last_updated=datetime.now().strftime("%H:%M:%S")
    )
@views.route('/compare-markets')
@login_required
def compare_markets():
    return render_template("compare.html", user=current_user)