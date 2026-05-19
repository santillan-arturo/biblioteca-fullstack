from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app) # Permette ad Angular (frontend) di dialogare con Flask senza blocchi di sicurezza

db_config = {
    'user': 'avnadmin',
    'password': 'AVNS_4Q-f-Sq82ujmeaJFtWO', 
    'host': 'mysql-2b5b836d-iisgalvanimi-7e99.g.aivencloud.com',
    'port': 27391,
    'database': 'defaultdb',
    'ssl_ca': os.path.join(os.path.dirname(__file__), '../database/ca.pem')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# ==========================================================
# ROTTA COMPITO STUDENTE A: INSERIMENTO NUOVO LIBRO (POST)
# ==========================================================
@app.route('/api/libri', methods=['POST'])
def aggiungi_libro():
    data = request.json # Riceve i dati inviati dal form Angular
    
    # Controllo di sicurezza: dati minimi obbligatori
    if not data or 'titolo' not in data or 'isbn' not in data:
        return jsonify({'errore': 'Titolo e ISBN sono obbligatori'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Query di inserimento per le 10 entità (collega fk_genere e fk_edizione)
        query = """
            INSERT INTO LIBRO (titolo, anno_pubblicazione, isbn, fk_genere, fk_edizione)
            VALUES (%s, %s, %s, %s, %s)
        """
        valori = (
            data['titolo'],
            data.get('anno_pubblicazione'), # .get evita errori se il campo non viene compilato
            data['isbn'],
            data.get('fk_genere'),  # ID del genere scelto dal menu a tendina
            data.get('fk_edizione') # ID dell'edizione scelta dal menu a tendina
        )
        
        cursor.execute(query, valori)
        conn.commit()
        
        nuovo_id = cursor.lastrowid
        
        return jsonify({
            'messaggio': 'Libro inserito con successo nel database a 10 entità!',
            'id_libro_creato': nuovo_id
        }), 201

    except mysql.connector.Error as err:
        return jsonify({'errore': f'Errore Database: {err}'}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    # Facciamo girare Flask sulla porta 5000
    app.run(debug=True, host='0.0.0.0', port=5000)