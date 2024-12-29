from sqlalchemy import text
from config import db
from flask import request, jsonify
from functools import wraps

def update_transacao(id):
    try:
        # Dados enviados no corpo da requisição
        dados = request.json

        # Consulta SQL para atualização
        query = text("""
            UPDATE app.transacao
            SET nome_trampo = :nome_trampo, valor = :valor
            WHERE id = :id
        """)

        # Executando a query
        db.session.execute(query, {
            'nome_trampo': dados['nome_trampo'],
            'valor': float(dados['valor']),
            'id': id
        })
        db.session.commit()

        return jsonify({'message': 'Transação atualizada com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
 
