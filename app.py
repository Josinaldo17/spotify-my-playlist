from flask import Flask, redirect, render_template, request, jsonify
from flask_cors import CORS
import os
from config import Config, db 
from gets.endpoints_get import select_trampo, select_transacao, select_totaisTrampo
from posts.endpoints_posts import  adicionar_transacao, adicionar_trampo
from puts.endpoints_put import update_transacao

app = Flask(__name__)
app.config.from_object(Config) 
CORS(app)
db.init_app(app)


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

@app.route('/trampo', methods=['GET'])
def get_trampo():
    return select_trampo()

@app.route('/transacao', methods=['GET'])
def get_transacao():
    return select_transacao()

@app.route('/totais/<int:mes>/<string:ano>', methods=['GET'])
def get_totaisTrampo(mes,ano):
    return select_totaisTrampo(mes,ano)


@app.route('/addtransacao', methods=['POST'])
def post_transacao():
    data = request.json
    return adicionar_transacao() 
    
@app.route('/addtrampo', methods=['POST'])
def post_trampo():
    data = request.json
    return adicionar_trampo()

@app.route('/updatetransacao/<int:id>', methods=['PUT'])
def put_transacao(id):
    return update_transacao(id)

if __name__ == '__main__':
    app.run(debug=True)
