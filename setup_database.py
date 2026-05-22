#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
import time
import sys

# Attendi che MySQL sia pronto
print("Attendo che MySQL sia pronto...")
for i in range(30):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        print("MySQL è pronto!")
        conn.close()
        break
    except:
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()

# Definizione dei dati
generi_data = [
    ('Fantascienza', 'Storie ambientate in futuri alternativi o mondi immaginari'),
    ('Fantasy', 'Mondi magici con creature e poteri sovrumani'),
    ('Mistero', 'Thriller con investigazioni e colpi di scena'),
    ('Romanzo', 'Storie di amore e relazioni umane'),
    ('Horror', 'Storie che suscitano terrore e paura'),
    ('Avventura', 'Storie di esplorazioni e sfide pericolose'),
    ('Storico', 'Ambientate in periodi storici reali'),
    ('Giallo', 'Storie poliziesche con crimini da risolvere')
]

libri_data = [
    # Fantascienza
    (1, 'Neuromante', 'William Gibson', 1984, 'Capolavoro del cyberpunk che ha definito il genere'),
    (1, 'Fondazione', 'Isaac Asimov', 1951, 'L\'epica della caduta e rinascita di un impero galattico'),
    (1, 'Il Marziano', 'Andy Weir', 2011, 'Un astronauta cerca di sopravvivere su Marte'),
    (1, 'Duna', 'Frank Herbert', 1965, 'Un giovane uomo su un pianeta desertico pieno di pericoli'),
    (1, 'Ubik', 'Philip K. Dick', 1969, 'Una realtà sempre più strana e inaffidabile'),
    (1, 'Ender\'s Game', 'Orson Scott Card', 1985, 'Un bambino prodigio preparato per una guerra intergalattica'),
    (1, '1984', 'George Orwell', 1949, 'Un regime totalitario opprime la popolazione'),
    (1, 'Il Pianeta dei Primati', 'Pierre Boulle', 1963, 'Gli umani sono schiavi di scimmie intelligenti'),
    (1, 'Bicentennial Man', 'Isaac Asimov', 1976, 'Un robot persegue l\'umanità attraverso i secoli'),
    (1, 'Cronos', 'Michael Chabon', 2004, 'Un\'avventura su mondi distopici'),
    (1, 'Il Termine della Notte', 'Liu Cixin', 2008, 'Prima parte della trilogia dei Tre Corpi'),
    (1, 'La Strada', 'Cormac McCarthy', 2006, 'Padre e figlio dopo l\'apocalisse'),
    (1, 'Iperion', 'Dan Simmons', 1989, 'Un\'opera monumentale tra fantascienza e poesia'),
    (1, 'La Mano Sinistra della Tenebra', 'Ursula K. Le Guin', 1969, 'Su un pianeta alieno con abitanti androgini'),
    (1, 'Tutti su di me', 'Philip K. Dick', 1974, 'In un futuro dove i ricordi possono essere manipolati'),
    
    # Fantasy
    (2, 'Il Signore degli Anelli', 'J.R.R. Tolkien', 1954, 'L\'epica avventura per distruggere l\'anello unico'),
    (2, 'Il Nome del Vento', 'Patrick Rothfuss', 2007, 'La storia di un giovane mago talentuoso'),
    (2, 'Un Gioco di Troni', 'George R.R. Martin', 1996, 'Intrighi politici e magia in un continente fantastico'),
    (2, 'Harry Potter', 'J.K. Rowling', 1997, 'Un giovane mago scopre di avere poteri straordinari'),
    (2, 'Il Cilantro e la Rosa', 'Jasper Fforde', 2001, 'Un mondo dove le persone possono entrare nei libri'),
    (2, 'La Ruota del Tempo', 'Robert Jordan', 1990, 'Un ciclo epico di 14 libri'),
    (2, 'Mistborn', 'Brandon Sanderson', 2006, 'Un\'empire oppressivo di immortali'),
    (2, 'Le Cronache di Narnia', 'C.S. Lewis', 1950, 'Bambini scoprono un mondo magico'),
    (2, 'Le Spade di Fuoco', 'Robin Hobb', 1995, 'Un giovane assassino con doni magici'),
    (2, 'La Terra di Mezzo', 'Tolkien', 1977, 'Il mitico continente di fantasy'),
    (2, 'Sette Regni', 'George R.R. Martin', 2000, 'Guerre e intrighi per il trono'),
    (2, 'La Casa della Memoria', 'Eva García Sáenz', 2016, 'Una città con magia nascosta'),
    (2, 'Trono di Spade', 'George R.R. Martin', 1996, 'Battaglia per il trono del Trono di Spade'),
    (2, 'Il Cristallo Nero', 'Stephen King', 2004, 'Una torre nera in un mondo dark fantasy'),
    (2, 'Eragon', 'Christopher Paolini', 2003, 'Un giovane cavaliere e il suo drago'),
    
    # Mistero
    (3, 'Il Codice Da Vinci', 'Dan Brown', 2003, 'Un mistico codice tra arte e religione'),
    (3, 'Shutter Island', 'Dennis Lehane', 2003, 'Un investigatore indaga su un misterioso ospedale'),
    (3, 'La Sesta Sense', 'Bruce Willis', 2000, 'Un bambino può vedere i morti'),
    (3, 'Il Labirinto dei Versi', 'Carlos Ruiz Zafón', 2001, 'Segreti tra i libri di una biblioteca'),
    (3, 'Rebecca', 'Daphne du Maurier', 1938, 'Una misteriosa prima moglie tormenta il presente'),
    (3, 'L\'Uomo della Pioggia', 'John Grisham', 1995, 'Un avvocato e un misterioso caso'),
    (3, 'Angeli e Demoni', 'Dan Brown', 2000, 'Il mondo dell\'arte nasconde pericoli'),
    (3, 'Il Nome della Rosa', 'Umberto Eco', 1980, 'Un monaco indaga omicidi in un monastero'),
    (3, 'L\'Assassinio in Oriente Express', 'Agatha Christie', 1934, 'Un giallo storico in treno'),
    (3, 'Assassinio sul Nilo', 'Agatha Christie', 1937, 'Un delitto durante una crociera'),
    (3, 'Il Coltello di Cristallo', 'Philip Pullman', 2007, 'Misteri tra mondi paralleli'),
    (3, 'Gone Girl', 'Gillian Flynn', 2012, 'Uno sparizione misteriosa e bugie'),
    (3, 'Il Segreto della Casa Buia', 'Kate Morton', 2008, 'Una casa nasconde segreti dal passato'),
    (3, 'L\'Innocenza dei Criminali', 'John Grisham', 2007, 'Un avvocato difende un innocente'),
    (3, 'Il Mistero di Sardar', 'Agatha Christie', 1941, 'Investigazione in Medio Oriente'),
    
    # Romanzo
    (4, 'Orgoglio e Pregiudizio', 'Jane Austen', 1813, 'Il classico amore tra Elizabeth e Darcy'),
    (4, 'Cime Tempestose', 'Emily Brontë', 1847, 'L\'amore passionale di Heathcliff e Catherine'),
    (4, 'La Grande Bellezza', 'Paolo Sorrentino', 2013, 'Roma e i segreti del lusso'),
    (4, 'Buongiorno Tristezza', 'Françoise Sagan', 1954, 'L\'estate di una ragazza spensierata'),
    (4, 'Il Diario di Anna Frank', 'Anna Frank', 1947, 'Le speranze e i sogni di una giovane in guerra'),
    (4, 'La Signora di Piccadilly', 'Arnold Bennett', 1902, 'L\'ascesa di una donna ambiziosa'),
    (4, 'Amore e Guerra', 'Lev Tolstoj', 1869, 'L\'epica delle famiglie nobili russe'),
    (4, 'Il Mulino sulla Floss', 'George Eliot', 1860, 'Due fratelli divisi dal destino e dal cuore'),
    (4, 'Addio alle Armi', 'Ernest Hemingway', 1929, 'Amore tra un soldato e un\'infermiera'),
    (4, 'Lolita', 'Vladimir Nabokov', 1955, 'Un amore ossessivo e trasgressivo'),
    (4, 'La Lettera di Lord Henry', 'Oscar Wilde', 1890, 'Decadenza e corruzione della bellezza'),
    (4, 'Il Ritratto della Gioventù', 'F. Scott Fitzgerald', 1925, 'Sogni e disillusioni del Jazz Age'),
    (4, 'Jane Eyre', 'Charlotte Brontë', 1847, 'Una governanta trova amore e riscatto'),
    (4, 'Wuthering Heights', 'Emily Brontë', 1847, 'Tormenta di passioni su una brughiera'),
    (4, 'Madame Bovary', 'Gustave Flaubert', 1856, 'Una donna sognante e insoddisfatta'),
    
    # Horror
    (5, 'Frankenstein', 'Mary Shelley', 1818, 'Un mostro creato dalla scienza terrifica il mondo'),
    (5, 'Dracula', 'Bram Stoker', 1897, 'Il vampiro più famoso della letteratura'),
    (5, 'L\'Esorcista', 'William Peter Blatty', 1971, 'Una bambina posseduta da forze oscure'),
    (5, 'Shining', 'Stephen King', 1977, 'Un albergo invernale nasconde orrori sovrumani'),
    (5, 'The Stand', 'Stephen King', 1978, 'Un virus sterminatore con sovrumani sopravvissuti'),
    (5, 'La Mosca', 'George Langelaan', 1957, 'Un esperimento genetico produce orrore'),
    (5, 'Carrie', 'Stephen King', 1974, 'Una ragazza con poteri telecinetici si vendica'),
    (5, 'L\'Inferno di Dante', 'Dante Alighieri', 1320, 'Un viaggio attraverso i gironi infernali'),
    (5, 'Il Fantasma dell\'Opera', 'Gaston Leroux', 1910, 'Un genio musicale deforme terrorizza'),
    (5, 'Rebecca', 'Daphne du Maurier', 1938, 'Un passato misterioso e inquietante'),
    (5, 'Insidious', 'Leigh Whannell', 2010, 'Una dimensione parallela piena di demoni'),
    (5, 'Sinister', 'Scott Derrickson', 2012, 'Filmati di suicidi di massa inquietano'),
    (5, 'La Notte dei Morti Viventi', 'George A. Romero', 1968, 'Zombie attaccano i vivi'),
    (5, 'The Ring', 'Gore Verbinski', 2002, 'Una videocassetta assassina'),
    (5, 'Occhio di Satana', 'William Castle', 1960, 'Uno specchio malefico amplifica il male'),
    
    # Avventura
    (6, 'Il Conte di Montecristo', 'Alexandre Dumas', 1844, 'Un uomo tradito si vendica dalle prigioni'),
    (6, 'L\'Isola del Tesoro', 'Robert Louis Stevenson', 1883, 'Una ricerca di tesoro su isole esotiche'),
    (6, 'Ventimila Leghe Sotto i Mari', 'Jules Verne', 1870, 'Un sottomarino tecnologico esplora i mari'),
    (6, 'Il Giro del Mondo in Ottanta Giorni', 'Jules Verne', 1873, 'Una sfida per circumnavigare il globo'),
    (6, 'Robinson Crusoe', 'Daniel Defoe', 1719, 'Un naufrago sopravvive su un\'isola deserta'),
    (6, 'Le Avventure di Tom Sawyer', 'Mark Twain', 1876, 'Un ragazzaccio tra fiumi e avventure'),
    (6, 'Le Avventure di Huckleberry Finn', 'Mark Twain', 1884, 'Fuga e libertà lungo il Mississippi'),
    (6, 'King Kong', 'Delos W. Lovelace', 1932, 'Un mostro gigante su un\'isola perduta'),
    (6, 'Moby Dick', 'Herman Melville', 1851, 'Una caccia ossessiva a una balena bianca'),
    (6, 'Lo Hobbit', 'J.R.R. Tolkien', 1937, 'Un piccolo essere va in avventura eroica'),
    (6, 'L\'Avventura del Naufrago', 'Daniel Defoe', 1719, 'Sopravvivenza e adattamento su un\'isola'),
    (6, 'Indiana Jones', 'Philip Kaufman', 1981, 'Un archeologo cerca artefatti perduti'),
    (6, 'Tarzan delle Scimmie', 'Edgar Rice Burroughs', 1912, 'Un uomo cresciuto dalla giungla'),
    (6, 'Capitano Nemo', 'Jules Verne', 1870, 'Il misterioso capitano di un sottomarino'),
    (6, 'Pirati dei Caraibi', 'Ted Elliott', 2003, 'Avventure tra pirati e tesori'),
    
    # Storico
    (7, 'La Citadella', 'A.J. Cronin', 1937, 'Un medico affronta la medicina e la società'),
    (7, 'La Rivolta dei Figli', 'Riccardo Bacchelli', 1968, 'L\'Italia durante il Risorgimento'),
    (7, 'La Trama Nera', 'Vincenzo Consolo', 1986, 'La Sicilia di fine ottocento'),
    (7, 'Il Gattopardo', 'Giuseppe Tomasi di Lampedusa', 1958, 'L\'aristocrazia siciliana durante il Risorgimento'),
    (7, 'La Giovane Signora', 'Honoré de Balzac', 1847, 'Parigi durante il secondo Impero'),
    (7, 'I Miserabili', 'Victor Hugo', 1862, 'La Francia rivoluzionaria e il suo popolo'),
    (7, 'La Rivoluzione Francese', 'Carlyle', 1837, 'Cronaca della caduta della monarchia'),
    (7, 'Guerra e Pace', 'Lev Tolstoj', 1869, 'La Russia napoleonica attraverso mille vite'),
    (7, 'La Notte di Fuoco', 'Ken Burns', 2012, 'La Guerra Civile americana'),
    (7, 'L\'Ombra del Vento', 'Carlos Ruiz Zafón', 2001, 'Barcellona post-guerra civile'),
    (7, 'Il Segreto della Casa Amarilla', 'Rosario Castellanos', 1963, 'La Spagna coloniale'),
    (7, 'Ben-Hur', 'Lew Wallace', 1880, 'Il Medio Oriente ai tempi di Cristo'),
    (7, 'Quo Vadis', 'Henryk Sienkiewicz', 1896, 'Roma pagana durante il cristianesimo'),
    (7, 'La Città della Gioia', 'Dominique Lapierre', 1985, 'Calcutta e le sue vite intrecciate'),
    (7, 'Radetzky March', 'Joseph Roth', 1932, 'L\'Impero austro-ungarico in declino'),
    
    # Giallo
    (8, 'La Pallottola Magica', 'Agatha Christie', 1926, 'Un primo caso di Hercule Poirot'),
    (8, 'L\'Assassinio di Roger Ackroyd', 'Agatha Christie', 1926, 'Un detective e un crimine in un villaggio'),
    (8, 'Delitto e Castigo', 'Fyodor Dostoevskij', 1866, 'Un crimine tormenta la coscienza'),
    (8, 'Il Mistero della Chambre Jaune', 'Gaston Leroux', 1907, 'Un giallo impossibile in una stanza gialla'),
    (8, 'Le Avventure di Sherlock Holmes', 'Arthur Conan Doyle', 1892, 'Il celebre detective e i suoi casi'),
    (8, 'L\'Esperimento Filby', 'Julian Symons', 1967, 'Un caso complesso e irrisolto'),
    (8, 'Il Silenzio della Notte', 'Michael Connelly', 2000, 'Un detective di Los Angeles indaga'),
    (8, 'Verità Sporche', 'Michael Connelly', 1997, 'Un caso di omicidio irrisolto'),
    (8, 'La Confessione di Harry Quebert', 'Joel Dicker', 2012, 'Un scrittore indaga su un antico delitto'),
    (8, 'Il Giuramento', 'Harlan Coben', 2005, 'Un uomo ricerca verità nascosta'),
    (8, 'Codice 404', 'Andrea Camilleri', 2008, 'Un ispettore in Sicilia indaga'),
    (8, 'La Serie Nera', 'Lorenzo Marone', 2018, 'Napoli e i suoi misteri'),
    (8, 'Io So', 'Vincenzo Consolo', 1989, 'Il mistero di una morte e una vita'),
    (8, 'Il Commissario Montalbano', 'Andrea Camilleri', 1994, 'Sicilia e gialli complessi'),
    (8, 'La Notte Non Aspetta', 'Tana French', 2008, 'Investigatori negli oscuri segreti'),
]

try:
    # Connessione al database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()
    
    # Creazione del database
    print("Creazione del database...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")
    cursor.execute("USE biblioteca")
    
    # Creazione delle tabelle
    print("Creazione delle tabelle...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generi (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL UNIQUE,
            descrizione TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libri (
            id INT PRIMARY KEY AUTO_INCREMENT,
            titolo VARCHAR(255) NOT NULL,
            autore VARCHAR(255) NOT NULL,
            anno_pubblicazione INT,
            genere_id INT NOT NULL,
            descrizione TEXT,
            FOREIGN KEY (genere_id) REFERENCES generi(id)
        )
    """)
    
    # Inserimento generi
    print("Inserimento generi...")
    for genere in generi_data:
        cursor.execute(
            "INSERT INTO generi (nome, descrizione) VALUES (%s, %s)",
            genere
        )
    
    # Inserimento libri
    print("Inserimento libri...")
    for libro in libri_data:
        cursor.execute(
            "INSERT INTO libri (genere_id, titolo, autore, anno_pubblicazione, descrizione) VALUES (%s, %s, %s, %s, %s)",
            libro
        )
    
    conn.commit()
    print("\n✓ Database creato e popolato con successo!")
    print(f"✓ {len(generi_data)} generi inseriti")
    print(f"✓ {len(libri_data)} libri inseriti")
    
except Error as e:
    print(f"Errore: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
