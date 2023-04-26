from flask import Flask, render_template, redirect, url_for,request, flash
import json
import os.path
from pprint import pprint

from tesseract import Tesseract

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def home():
    return render_template('welcome.html')

@app.post('/url-shortener')
def url_shorter():
    urls = {}

    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)

    if request.form['url_name'] in urls.keys():
        flash("short name already taken")
        return redirect(url_for('home'))
    
    urls[request.form['url_name']] = {'url': request.form['url']}
    
    with open ('urls.json', 'w') as url_file:
        json.dump(urls, url_file)

    return redirect(url_for('home'))

@app.post('/file-url-shortener')
def file_url_shorter():
    urls = {}

    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)

    # if request.form['url_name'] in urls.keys():
    #     flash("short name already taken")
    #     return redirect(url_for('home'))
    
    # urls[request.form['url_name']] = {'url': request.form['url']}
    
    # with open ('urls.json', 'w') as url_file:
    #     json.dump(urls, url_file)

    return redirect(url_for('home'))

@app.get('/redirect-to-home')
def redirect_to_home():
    # url_for(<function_name>)
    return redirect(url_for('home'))

@app.post('/ocr')
def ocr():
    
    # print(request.method)
    image = request.files['image']
    
    ts = Tesseract()
    
    print("====================")
    print(ts.parse(image))
    print("====================")

    # url_for(<function_name>)
    return redirect(url_for('home'))


# create a 404 page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404