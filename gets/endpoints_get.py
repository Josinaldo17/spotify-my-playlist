from sqlalchemy import text
import re
from config import db  # Importa db de database.py
from flask import jsonify

def select_trampo():
    query = text('SELECT * FROM app.trampo')
    result = db.session.execute(query)
    alunos = result.fetchall()

    resultado = jsonify([
        {
            'nome': aluno[0]
        } for aluno in alunos
    ])

    return resultado

def select_transacao():
    query = text('SELECT * FROM app.transacao ORDER BY id DESC ')
    result = db.session.execute(query)
    alunos = result.fetchall()

    resultado = jsonify([
        {
            'nome': aluno[0],
            'valor': re.sub(r'[^\d.-]', '', aluno[1]),
            'dia': aluno[2].isoformat(),
            'id': aluno[3]
        } for aluno in alunos
    ])

    return resultado

def select_totaisTrampo(mes, ano):
    query = text('SELECT * FROM obter_soma_transacoes(:mes_hj, :ano_hj)')
    result = db.session.execute(query, {'mes_hj': mes, 'ano_hj': ano})
    alunos = result.fetchall()
    
    
    resultado = jsonify([{
            'total': aluno[0],
            'nome': aluno[2],
            'total_hj': aluno[3],
        } for aluno in alunos
    ])

    return resultado
