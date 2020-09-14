from flask import Flask,render_template
from app.requests import NewsRequests
app = Flask(__name__)


@app.route('/')
def index():
    news = NewsRequests()
    news= news.get_top_headlines( sources='')
    
    return render_template ('index.html', sport=sport_news['articles'])
    # news= news.get_top_headlines( sources='Aljazeer-news')
    # return news
    
# @app.route('/education')

# def education():
#     n=NewsRequests()
#     news_education

if __name__ == '__main__':
    app.run(debug = True)