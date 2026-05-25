import mysql.connector

# CONFIGURAZIONE (Dati di Aiven)
config = {
    'user': 'avnadmin',
    'password': 'AVNS_4Q-f-Sq82ujmeaJFtWO',
    'host': 'mysql-2b5b836d-iisgalvanimi-7e99.g.aivencloud.com',
    'port': 27391,
    'database': 'defaultdb',
    'ssl_ca': 'ca.pem'
}

def inizializza_database():
    try:
        print("Tentativo di connessione a Aiven Cloud...")
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        print("Connessione riuscita!")

        print("Rimozione vecchie tabelle...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        tabelle = ["SANZIONE", "PRESTITO", "COPIA_FISICA", "SCRITTO_DA", "LIBRO", "SCAFFALE", "EDIZIONE", "LETTORE", "BIBLIOTECARIO", "GENERE", "AUTORE"]
        for tabella in tabelle:
            cursor.execute(f"DROP TABLE IF EXISTS {tabella};")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

 
        print("Creazione delle 10 tabelle nel cloud...")

        # 1. GENERE
        cursor.execute("""
            CREATE TABLE GENERE (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL
            );
        """)

        # 2. AUTORE
        cursor.execute("""
            CREATE TABLE AUTORE (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                cognome VARCHAR(50) NOT NULL,
                nazionalita VARCHAR(50)
            );
        """)

        # 3. EDIZIONE
        cursor.execute("""
            CREATE TABLE EDIZIONE (
                id INT AUTO_INCREMENT PRIMARY KEY,
                casa_editrice VARCHAR(100) NOT NULL,
                lingua VARCHAR(30) DEFAULT 'Italiano'
            );
        """)

        # 4. SCAFFALE
        cursor.execute("""
            CREATE TABLE SCAFFALE (
                id INT AUTO_INCREMENT PRIMARY KEY,
                codice_zona VARCHAR(10) NOT NULL,
                numero_ripiano INT NOT NULL
            );
        """)

        # 5. BIBLIOTECARIO
        cursor.execute("""
            CREATE TABLE BIBLIOTECARIO (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                cognome VARCHAR(50) NOT NULL,
                matricola VARCHAR(20) UNIQUE NOT NULL
            );
        """)

        # 6. LETTORE
        cursor.execute("""
            CREATE TABLE LETTORE (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                cognome VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            );
        """)

        # 7. LIBRO
        cursor.execute("""
            CREATE TABLE LIBRO (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titolo VARCHAR(100) NOT NULL,
                anno_pubblicazione INT,
                isbn VARCHAR(13) UNIQUE NOT NULL,
                fk_genere INT,
                fk_edizione INT,
                FOREIGN KEY (fk_genere) REFERENCES GENERE(id),
                FOREIGN KEY (fk_edizione) REFERENCES EDIZIONE(id)
            );
        """)

        # 8. COPIA_FISICA
        cursor.execute("""
            CREATE TABLE COPIA_FISICA (
                id INT AUTO_INCREMENT PRIMARY KEY,
                codice_inventario VARCHAR(50) UNIQUE NOT NULL,
                stato_conservazione VARCHAR(20) DEFAULT 'Buono',
                fk_libro INT,
                fk_scaffale INT,
                FOREIGN KEY (fk_libro) REFERENCES LIBRO(id),
                FOREIGN KEY (fk_scaffale) REFERENCES SCAFFALE(id)
            );
        """)

        # 9. PRESTITO
        cursor.execute("""
            CREATE TABLE PRESTITO (
                id INT AUTO_INCREMENT PRIMARY KEY,
                data_inizio DATE NOT NULL,
                data_scadenza DATE NOT NULL,
                data_restituzione DATE,
                fk_copia INT,
                fk_lettore INT,
                fk_bibliotecario INT,
                FOREIGN KEY (fk_copia) REFERENCES COPIA_FISICA(id),
                FOREIGN KEY (fk_lettore) REFERENCES LETTORE(id),
                FOREIGN KEY (fk_bibliotecario) REFERENCES BIBLIOTECARIO(id)
            );
        """)

        # 10. SANZIONE
        cursor.execute("""
            CREATE TABLE SANZIONE (
                id INT AUTO_INCREMENT PRIMARY KEY,
                importo DECIMAL(5,2) NOT NULL,
                pagata BOOLEAN DEFAULT FALSE,
                fk_prestito INT,
                FOREIGN KEY (fk_prestito) REFERENCES PRESTITO(id)
            );
        """)

        # TABELLA PONTE: SCRITTO_DA (Libro <-> Autore)
        cursor.execute("""
            CREATE TABLE SCRITTO_DA (
                id_libro INT,
                id_autore INT,
                PRIMARY KEY (id_libro, id_autore),
                FOREIGN KEY (id_libro) REFERENCES LIBRO(id),
                FOREIGN KEY (id_autore) REFERENCES AUTORE(id)
            );
        """)


        print("Inserimento dati di prova...")
        cursor.execute("INSERT INTO GENERE (nome) VALUES ('Fantasy'), ('Giallo');")
        cursor.execute("INSERT INTO AUTORE (nome, cognome, nazionalita) VALUES ('J.K.', 'Rowling', 'Britannica');")
        cursor.execute("INSERT INTO EDIZIONE (casa_editrice) VALUES ('Salani');")
        cursor.execute("INSERT INTO SCAFFALE (codice_zona, numero_ripiano) VALUES ('SALA-A', 3);")
        cursor.execute("INSERT INTO BIBLIOTECARIO (nome, cognome, matricola) VALUES ('Luigi', 'Verdi', 'BIBLIO01');")
        cursor.execute("INSERT INTO LETTORE (nome, cognome, email) VALUES ('Mario', 'Rossi', 'mario@email.com');")
        
        cursor.execute("INSERT INTO LIBRO (titolo, anno_pubblicazione, isbn, fk_genere, fk_edizione) VALUES ('Harry Potter e la Pietra Filosofale', 1997, '9788876251696', 1, 1);")
        cursor.execute("INSERT INTO SCRITTO_DA (id_libro, id_autore) VALUES (1, 1);")
        
        cursor.execute("INSERT INTO COPIA_FISICA (codice_inventario, fk_libro, fk_scaffale) VALUES ('INV-0001', 1, 1);")
        
        cursor.execute("INSERT INTO PRESTITO (data_inizio, data_scadenza, fk_copia, fk_lettore, fk_bibliotecario) VALUES ('2026-05-19', '2026-06-19', 1, 1, 1);")

        conn.commit()
        print("DATABASE A 10 ENTITÀ CONFIGURATO E POPOLATO CON SUCCESSO SU AIVEN!")

    except mysql.connector.Error as err:
        print(f"Errore durante l'operazione: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    inizializza_database()