from flask import Flask

app = Flask(__name__)

@app.route('/')
def heme():
    return "Hello Flask!"