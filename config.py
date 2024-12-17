from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, jsonify
import os
db = SQLAlchemy()

usuario =  os.environ.get('USUARIO_SPOTIFY')
senha =  os.environ.get('SENHA_SPOTIFY')
porta = '5432' 
host =  os.environ.get('BOT_SPOTIFY')
banco_de_dados = 'postgres'


class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False