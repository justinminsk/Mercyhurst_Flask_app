import markdown
from flask import Flask, render_template, Markup

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/post')
def content():
    return render_template('install_python.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/slideshow")
def slide_show():
    return render_template('anaconda.html')


if __name__ == '__main__':
    app.run()
