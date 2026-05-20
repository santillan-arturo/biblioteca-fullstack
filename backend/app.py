from flask import Flask, jsonify
from flask_cors import CORS  # <-- Controlla che ci sia questa riga!

app = Flask(__name__)
CORS(app)  # <-- Questo sblocca definitivamente il box rosso!


app = Flask(__name__)
CORS(app)  # Consente ad Angular di connettersi a Flask senza blocchi di sicurezza

DB_CONFIG = {
    'user': 'avnadmin',
    'password': 'AVNS_4Q-f-Sq82ujmeaJFtWO',
    'host': 'mysql-2b5b836d-iisgalvanimi-7e99.g.aivencloud.com',
    'port': 27391,
    'database': 'defaultdb',
    'ssl_ca': 'ca.pem'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ==========================================================
# 1. GET /api/categorie (Lista per il 1° livello di navigazione)
# ==========================================================
@app.route('/api/categorie', methods=['GET'])
def get_categorie():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, descrizione FROM generi ORDER BY nome ASC")
        categorie = cursor.fetchall()
        return jsonify(categorie), 200
    except Error as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close(), conn.close()

# ==========================================================
# 2. GET /api/libri?categoria_id=... (2° livello + filtro ricerca)
# ==========================================================
@app.route('/api/libri', methods=['GET'])
def get_libri():
    categoria_id = request.args.get('categoria_id')
    search_query = request.args.get('search', '')
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Query base con JOIN per estrarre anche il nome del genere
        query = """
            SELECT l.id, l.titolo, l.isbn, l.anno_pubblicazione, g.nome AS genere 
            FROM libri l
            JOIN generi g ON l.fk_genere = g.id
            WHERE 1=1
        """
        params = []
        
        if categoria_id:
            query += " AND l.fk_genere = %s"
            params.append(categoria_id)
            
        if search_query:
            query += " AND l.titolo LIKE %s"
            params.append(f"%{search_query}%")
            
        cursor.execute(query, tuple(params))
        libri = cursor.fetchall()
        return jsonify(libri), 200
    except Error as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close(), conn.close()

# ==========================================================
# 3. GET /api/libri/<id> (3° livello: scheda libro con JOIN prestiti)
# ==========================================================
@app.route('/api/libri/<int:libro_id>', methods=['GET'])
def get_libro_dettaglio(libro_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Recupero info libro ed edizione associata
        query_libro = """
            SELECT l.id, l.titolo, l.isbn, l.anno_pubblicazione, g.nome AS genere, e.casa_editrice, e.lingua
            FROM libri l
            LEFT JOIN generi g ON l.fk_genere = g.id
            LEFT JOIN edizioni e ON l.fk_edizione = e.id
            WHERE l.id = %s
        """
        cursor.execute(query_libro, (libro_id,))
        libro = cursor.fetchone()
        
        if not libro:
            return jsonify({"error": "Libro non trovato"}), 404
            
        # JOIN complessa: trova lo storico dei lettori che hanno preso in prestito le copie di questo libro
        query_prestiti = """
            SELECT p.data_inizio, p.data_scadenza, p.data_restituzione, let.nome, let.cognome, let.email
            FROM prestiti p
            JOIN copie_fisiche cf ON p.fk_copia = cf.id
            JOIN lettori let ON p.fk_lettore = let.id
            WHERE cf.fk_libro = %s
            ORDER BY p.data_inizio DESC
        """
        cursor.execute(query_prestiti, (libro_id,))
        libro['cronologia_prestiti'] = cursor.fetchall()
        
        return jsonify(libro), 200
    except Error as e:
        return jsonify({"error": "Errore server", "details": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close(), conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)