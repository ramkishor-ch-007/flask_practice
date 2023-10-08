from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "welcome flask"

@app.route('/about')
def about():
    return 'This is the About page.'

@app.route('/contact')
def contact():
    return 'Contact us at contact@example.com'
