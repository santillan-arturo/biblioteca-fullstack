#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
import time

# Attendi che MySQL sia pronto
print("Connessione a MySQL...")
for i in range(10):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="biblioteca"
        )
        print("✓ Connesso!")
        break
    except:
        time.sleep(1)

cursor = conn.cursor()

# 10 libri per genere
libri_per_genere = {
    1: [  # Fantascienza
        ('Neuromante', 'William Gibson', 1984),
        ('Fondazione', 'Isaac Asimov', 1951),
        ('Il Marziano', 'Andy Weir', 2011),
        ('Duna', 'Frank Herbert', 1965),
        ('Ubik', 'Philip K. Dick', 1969),
        ('Ender\'s Game', 'Orson Scott Card', 1985),
        ('1984', 'George Orwell', 1949),
        ('Il Pianeta dei Primati', 'Pierre Boulle', 1963),
        ('Iperion', 'Dan Simmons', 1989),
        ('La Mano Sinistra della Tenebra', 'Ursula K. Le Guin', 1969),
    ],
    2: [  # Fantasy
        ('Il Signore degli Anelli', 'J.R.R. Tolkien', 1954),
        ('Il Nome del Vento', 'Patrick Rothfuss', 2007),
        ('Un Gioco di Troni', 'George R.R. Martin', 1996),
        ('Harry Potter', 'J.K. Rowling', 1997),
        ('La Ruota del Tempo', 'Robert Jordan', 1990),
        ('Mistborn', 'Brandon Sanderson', 2006),
        ('Le Cronache di Narnia', 'C.S. Lewis', 1950),
        ('Eragon', 'Christopher Paolini', 2003),
        ('Il Cristallo Nero', 'Stephen King', 2004),
        ('Lo Hobbit', 'J.R.R. Tolkien', 1937),
    ],
    3: [  # Mistero
        ('Il Codice Da Vinci', 'Dan Brown', 2003),
        ('Shutter Island', 'Dennis Lehane', 2003),
        ('Il Labirinto dei Versi', 'Carlos Ruiz Zafón', 2001),
        ('Rebecca', 'Daphne du Maurier', 1938),
        ('Angeli e Demoni', 'Dan Brown', 2000),
        ('Il Nome della Rosa', 'Umberto Eco', 1980),
        ('L\'Assassinio in Oriente Express', 'Agatha Christie', 1934),
        ('Assassinio sul Nilo', 'Agatha Christie', 1937),
        ('Gone Girl', 'Gillian Flynn', 2012),
        ('Il Segreto della Casa Buia', 'Kate Morton', 2008),
    ],
    4: [  # Romanzo
        ('Orgoglio e Pregiudizio', 'Jane Austen', 1813),
        ('Cime Tempestose', 'Emily Brontë', 1847),
        ('La Grande Bellezza', 'Paolo Sorrentino', 2013),
        ('Buongiorno Tristezza', 'Françoise Sagan', 1954),
        ('Amore e Guerra', 'Lev Tolstoj', 1869),
        ('Addio alle Armi', 'Ernest Hemingway', 1929),
        ('Lolita', 'Vladimir Nabokov', 1955),
        ('Jane Eyre', 'Charlotte Brontë', 1847),
        ('Wuthering Heights', 'Emily Brontë', 1847),
        ('Madame Bovary', 'Gustave Flaubert', 1856),
    ],
    5: [  # Horror
        ('Frankenstein', 'Mary Shelley', 1818),
        ('Dracula', 'Bram Stoker', 1897),
        ('L\'Esorcista', 'William Peter Blatty', 1971),
        ('Shining', 'Stephen King', 1977),
        ('The Stand', 'Stephen King', 1978),
        ('Carrie', 'Stephen King', 1974),
        ('Il Fantasma dell\'Opera', 'Gaston Leroux', 1910),
        ('La Notte dei Morti Viventi', 'George A. Romero', 1968),
        ('The Ring', 'Gore Verbinski', 2002),
        ('Insidious', 'Leigh Whannell', 2010),
    ],
    6: [  # Avventura
        ('Il Conte di Montecristo', 'Alexandre Dumas', 1844),
        ('L\'Isola del Tesoro', 'Robert Louis Stevenson', 1883),
        ('Ventimila Leghe Sotto i Mari', 'Jules Verne', 1870),
        ('Il Giro del Mondo in Ottanta Giorni', 'Jules Verne', 1873),
        ('Robinson Crusoe', 'Daniel Defoe', 1719),
        ('Le Avventure di Tom Sawyer', 'Mark Twain', 1876),
        ('Moby Dick', 'Herman Melville', 1851),
        ('Indiana Jones', 'Philip Kaufman', 1981),
        ('Tarzan delle Scimmie', 'Edgar Rice Burroughs', 1912),
        ('Pirati dei Caraibi', 'Ted Elliott', 2003),
    ],
    7: [  # Storico
        ('La Citadella', 'A.J. Cronin', 1937),
        ('Il Gattopardo', 'Giuseppe Tomasi di Lampedusa', 1958),
        ('I Miserabili', 'Victor Hugo', 1862),
        ('Guerra e Pace', 'Lev Tolstoj', 1869),
        ('L\'Ombra del Vento', 'Carlos Ruiz Zafón', 2001),
        ('Ben-Hur', 'Lew Wallace', 1880),
        ('Quo Vadis', 'Henryk Sienkiewicz', 1896),
        ('La Città della Gioia', 'Dominique Lapierre', 1985),
        ('La Giovane Signora', 'Honoré de Balzac', 1847),
        ('La Rivolta dei Figli', 'Riccardo Bacchelli', 1968),
    ],
    8: [  # Giallo
        ('La Pallottola Magica', 'Agatha Christie', 1926),
        ('L\'Assassinio di Roger Ackroyd', 'Agatha Christie', 1926),
        ('Delitto e Castigo', 'Fyodor Dostoevskij', 1866),
        ('Il Mistero della Chambre Jaune', 'Gaston Leroux', 1907),
        ('Le Avventure di Sherlock Holmes', 'Arthur Conan Doyle', 1892),
        ('Il Silenzio della Notte', 'Michael Connelly', 2000),
        ('La Confessione di Harry Quebert', 'Joel Dicker', 2012),
        ('Codice 404', 'Andrea Camilleri', 2008),
        ('Il Commissario Montalbano', 'Andrea Camilleri', 1994),
        ('La Notte Non Aspetta', 'Tana French', 2008),
    ],
}

try:
    # Cancella i libri precedenti se ce ne sono
    print("Pulisci la tabella libri...")
    cursor.execute("DELETE FROM libri")
    
    # Inserisci i 10 libri per ogni genere
    print("Inserimento 10 libri per genere...")
    total = 0
    for genere_id, libri in libri_per_genere.items():
        for titolo, autore, anno in libri:
            cursor.execute(
                "INSERT INTO libri (genere_id, titolo, autore, anno_pubblicazione) VALUES (%s, %s, %s, %s)",
                (genere_id, titolo, autore, anno)
            )
            total += 1
    
    conn.commit()
    print(f"✓ {total} libri inseriti con successo!")
    
    # Verifica
    cursor.execute("SELECT COUNT(*) as count FROM libri")
    result = cursor.fetchone()
    print(f"✓ Totale libri nel database: {result[0]}")
    
except Error as e:
    print(f"Errore: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
