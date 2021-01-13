from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/news/tech')
def tech_news():
    return '<b>technology news</b>'

@app.route('/news')
def news():
    return """<html> 
        <h1>News</h1> 
        <p>SWU News daily topics:</p>
        <ul>
            <li>Technology</li>
            <li>Sport</li>
            <li>Education</li>
        </ul>
    </html>"""

@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)

@app.route('/name/<int:num>')
def favourite_number(num):
    return f"Your favorite number is {num}, which is half of {num * 2}"




