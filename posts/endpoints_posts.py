from sqlalchemy import text
from config import db
from flask import request, jsonify
from functools import wraps
import datetime
import jwt

def adicionar_transacao():
    try:
        # Dados enviados no corpo da requisição (JSON)
        dados = request.json

                # Certifique-se de que os valores numéricos estão sendo convertidos corretamente
        nome_trampo = (dados['nome_trampo'])
        valor = float(dados['valor'])
       

        # Consulta SQL com placeholders para valores
        query = text("INSERT INTO app.transacao( nome_trampo, valor) VALUES (:nome_trampo, :valor)")

        db.session.execute(query, {
            'nome_trampo': nome_trampo,
            'valor': valor
        })
        db.session.commit()

        # Resposta de sucesso
        return jsonify({'message': 'trasaçao registrada com sucesso!'}), 200

    except Exception as e:
        print(f"Erro ao adicionar avaliação: {e}")
        return jsonify({f"message": "Erro ao adicionar trasaçao {e}"}), 500
    
    
def adicionar_trampo():
    try:
        # Recebendo os dados do JSON
        dados = request.json
        nome = dados['nome']

        # Query SQL
        query = text("""
            INSERT INTO app.trampo (nome)
            VALUES (:nome)
        """)

        # Executando a query
        db.session.execute(query, {'nome': nome})
        db.session.commit()

        return jsonify({'message': 'Trabalho adicionado com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        print(f"Erro ao adicionar trabalho: {e}")
        return jsonify({'message': f"Erro ao adicionar trabalho: {e}"}), 500
