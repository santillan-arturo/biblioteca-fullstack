from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
# Permette ad Angular (frontend) di dialogare con Flask senza blocchi di sicurezza
CORS(app) 

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
    print("Dati ricevuti da Angular:", data) # Questo stamperà nel terminale cosa manda Angular
    
    # Controllo di sicurezza: dati minimi obbligatori
    if not data or 'titolo' not in data or 'isbn' not in data:
        return jsonify({'errore': 'Titolo e ISBN sono obbligatori'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # Query di inserimento (Assicurati che la tabella si chiami LIBRO in maiuscolo o minuscolo)
        query = """
            INSERT INTO LIBRO (titolo, anno_pubblicazione, isbn, fk_genere, fk_edizione)
            VALUES (%s, %s, %s, %s, %s)
        """
        
        # Evitiamo errori impostando un valore di default (1) se Angular manda campi vuoti o nulli
        fk_genere = data.get('fk_genere') if data.get('fk_genere') is not None else 1
        fk_edizione = data.get('fk_edizione') if data.get('fk_edizione') is not None else 1
        
        valori = (
            data['titolo'],
            data.get('anno_pubblicazione'),
            data['isbn'],
            fk_genere,
            fk_edizione
        )
        
        cursor.execute(query, valores := valori)
        conn.commit()
        
        nuovo_id = cursor.lastrowid
        
        return jsonify({
            'messaggio': 'Libro inserito con successo nel database a 10 entità!',
            'id_libro_creato': nuovo_id
        }), 201

    except mysql.connector.Error as err:
        print(f"Errore specifico del Database: {err}") # Questo ti dice nel terminale perché fallisce
        return jsonify({'errore': f'Errore Database: {err}'}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# ==========================================================
# ROTTA PER SBLOCCARE IL TUO COMPAGNO (GET CATEGORIE)
# ==========================================================
@app.route('/api/categorie', methods=['GET'])
def get_categorie():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # Se la tabella delle categorie si chiama in un altro modo (es. 'GENERE'), cambiala qui sotto
        cursor.execute("SELECT id, nome FROM GENERE") 
        categorie = cursor.fetchall()
        
        return jsonify(categorie), 200
    except mysql.connector.Error as err:
        print(f"Errore lettura categorie: {err}")
        # Rimandiamo un elenco finto di emergenza se la tabella non esiste, così la pagina del tuo compagno si sblocca comunque!
        mock_categorie = [{"id": 1, "nome": "Fantasy"}, {"id": 2, "nome": "Romanzo"}]
        return jsonify(mock_categorie), 200
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)