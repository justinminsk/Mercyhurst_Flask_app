from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/news')
def content():
    return render_template('news_posts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/anaconda")
def slide_show():
    return render_template('anaconda.html')


@app.route("/acm")
def slide_show():
    return render_template('acm.html')


if __name__ == '__main__':
    app.run()
