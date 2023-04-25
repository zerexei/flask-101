from flask import Flask, render_template, redirect, url_for,request, flash
import json
import os.path
from pprint import pprint

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def home():
    pprint(request.form)
    print("asd")
    return render_template('welcome.html')

# TODO: test form input
@app.post('/url-shorter')
def url_shorter():
    urls = {}

    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)

    if request.form['code'] in urls.keys():
        flash("short name already taken")
        return redirect(url_for('home'))
    
    urls[request.form['code']] = {'url': request.form['url']}
    with open ('urls.json', 'w') as url_file:
        json.dump(urls, url_file)
    return "shorter"

@app.get('/redirect-to-home')
def redirect_to_home():
    # url_for(<function_name>)
    return redirect(url_for('home'))