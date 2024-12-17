from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, jsonify
db = SQLAlchemy()
import os

class Config:
    SQLALCHEMY_DATABASE_URI =  os.environ.get('BANCO_SPOTIFY') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Sempreemforma'