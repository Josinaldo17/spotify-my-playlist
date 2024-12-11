from flask import Flask, redirect, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def teste():
    return redirect('/playlist')
    
@app.route('/playlist')
def index():    
    bot_token = os.environ.get('BOT_SPOTIFY')
    return render_template("index.html", bot_token=bot_token)

@app.before_request
def force_https():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://'), code=301)

if __name__ == '__main__':
    app.run(debug=True)