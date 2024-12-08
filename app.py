from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def teste():
    return redirect('/playlist')
    
@app.route('/playlist')
def index():
    return render_template('index.html')

@app.before_request
def force_https():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://'), code=301)

if __name__ == '__main__':
    app.run(debug=True)