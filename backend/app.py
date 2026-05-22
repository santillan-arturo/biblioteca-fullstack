from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# Configurazione CORS super aperta per evitare qualsiasi blocco con GitHub Codespaces
CORS(app, resources={r"/*": {"origins": "*"}})

def get_db_connection():
    # Sostituisci questi parametri se i dati di accesso del tuo database locale sono diversi
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca"
    )

@app.route('/api/categorie', methods=['GET'])
def get_categorie():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, descrizione FROM generi ORDER BY nome ASC")
        categorie = cursor.fetchall()
        return jsonify(categorie), 200
    except Exception as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/libri', methods=['GET'])
def get_libri():
    try:
        categoria_id = request.args.get('categoria_id', type=int)
        search = request.args.get('search', '').strip()
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Query base
        query = "SELECT id, titolo, autore, anno_pubblicazione, genere_id FROM libri WHERE 1=1"
        params = []
        
        # Filtro per categoria
        if categoria_id:
            query += " AND genere_id = %s"
            params.append(categoria_id)
        
        # Filtro per ricerca di titolo (case-insensitive)
        if search:
            query += " AND titolo LIKE %s"
            params.append(f"%{search}%")
        
        query += " ORDER BY titolo ASC"
        
        cursor.execute(query, params)
        libri = cursor.fetchall()
        return jsonify(libri), 200
    except Exception as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/libri/<int:libro_id>', methods=['GET'])
def get_libro_dettaglio(libro_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT l.id, l.titolo, l.autore, l.anno_pubblicazione, l.descrizione, g.nome as genere "
            "FROM libri l "
            "JOIN generi g ON l.genere_id = g.id "
            "WHERE l.id = %s",
            (libro_id,)
        )
        libro = cursor.fetchone()
        if libro:
            return jsonify(libro), 200
        else:
            return jsonify({"error": "Libro non trovato"}), 404
    except Exception as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)