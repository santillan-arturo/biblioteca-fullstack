-- Creazione del database
CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

-- Tabella generi
CREATE TABLE IF NOT EXISTS generi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descrizione TEXT
);

-- Tabella libri
CREATE TABLE IF NOT EXISTS libri (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titolo VARCHAR(255) NOT NULL,
    autore VARCHAR(255) NOT NULL,
    anno_pubblicazione INT,
    genere_id INT NOT NULL,
    descrizione TEXT,
    FOREIGN KEY (genere_id) REFERENCES generi(id)
);

-- Inserimento generi
INSERT INTO generi (nome, descrizione) VALUES
('Fantascienza', 'Storie ambientate in futuri alternativi o mondi immaginari'),
('Fantasy', 'Mondi magici con creature e poteri sovrumani'),
('Mistero', 'Thriller con investigazioni e colpi di scena'),
('Romanzo', 'Storie di amore e relazioni umane'),
('Horror', 'Storie che suscitano terrore e paura'),
('Avventura', 'Storie di esplorazioni e sfide pericolose'),
('Storico', 'Ambientate in periodi storici reali'),
('Giallo', 'Storie poliziesche con crimini da risolvere');

-- Inserimento libri per Fantascienza
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('Neuromante', 'William Gibson', 1984, 1, 'Capolavoro del cyberpunk che ha definito il genere'),
('Fondazione', 'Isaac Asimov', 1951, 1, 'L\'epica della caduta e rinascita di un impero galattico'),
('Il Marziano', 'Andy Weir', 2011, 1, 'Un astronauta cerca di sopravvivere su Marte'),
('Duna', 'Frank Herbert', 1965, 1, 'Un giovane uomo su un pianeta desertico pieno di pericoli'),
('Ubik', 'Philip K. Dick', 1969, 1, 'Una realtà sempre più strana e inaffidabile'),
('Ender\'s Game', 'Orson Scott Card', 1985, 1, 'Un bambino prodigio preparato per una guerra intergalattica'),
('1984', 'George Orwell', 1949, 1, 'Un regime totalitario opprime la popolazione'),
('Il Pianeta dei Primati', 'Pierre Boulle', 1963, 1, 'Gli umani sono schiavi di scimmie intelligenti'),
('Bicentennial Man', 'Isaac Asimov', 1976, 1, 'Un robot persegue l\'umanità attraverso i secoli'),
('Cronos', 'Michael Chabon', 2004, 1, 'Un'avventura su mondi distopici'),
('Il Termine della Notte', 'Liu Cixin', 2008, 1, 'Prima parte della trilogia dei Tre Corpi'),
('La Strada', 'Cormac McCarthy', 2006, 1, 'Padre e figlio dopo l\'apocalisse'),
('Iperion', 'Dan Simmons', 1989, 1, 'Un'opera monumentale tra fantascienza e poesia'),
('La Mano Sinistra della Tenebra', 'Ursula K. Le Guin', 1969, 1, 'Su un pianeta alieno con abitanti androgini'),
('Tutti su di me', 'Philip K. Dick', 1974, 1, 'In un futuro dove i ricordi possono essere manipolati');

-- Inserimento libri per Fantasy
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('Il Signore degli Anelli', 'J.R.R. Tolkien', 1954, 2, 'L\'epica avventura per distruggere l\'anello unico'),
('Il Nome del Vento', 'Patrick Rothfuss', 2007, 2, 'La storia di un giovane mago talentuoso'),
('Un Gioco di Troni', 'George R.R. Martin', 1996, 2, 'Intrighi politici e magia in un continente fantastico'),
('Harry Potter', 'J.K. Rowling', 1997, 2, 'Un giovane mago scopre di avere poteri straordinari'),
('Il Cilantro e la Rosa', 'Jasper Fforde', 2001, 2, 'Un mondo dove le persone possono entrare nei libri'),
('La Ruota del Tempo', 'Robert Jordan', 1990, 2, 'Un ciclo epico di 14 libri'),
('Mistborn', 'Brandon Sanderson', 2006, 2, 'Un'empire oppressivo di immortali'),
('Le Cronache di Narnia', 'C.S. Lewis', 1950, 2, 'Bambini scoprono un mondo magico'),
('Le Spade di Fuoco', 'Robin Hobb', 1995, 2, 'Un giovane assassino con doni magici'),
('La Terra di Mezzo', 'Tolkien', 1977, 2, 'Il mitico continente di fantasy'),
('Sette Regni', 'George R.R. Martin', 2000, 2, 'Guerre e intrighi per il trono'),
('La Casa della Memoria', 'Eva García Sáenz', 2016, 2, 'Una città con magia nascosta'),
('Trono di Spade', 'George R.R. Martin', 1996, 2, 'Battaglia per il trono del Trono di Spade'),
('Il Cristallo Nero', 'Stephen King', 2004, 2, 'Una torre nera in un mondo dark fantasy'),
('Eragon', 'Christopher Paolini', 2003, 2, 'Un giovane cavaliere e il suo drago');

-- Inserimento libri per Mistero
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('Il Codice Da Vinci', 'Dan Brown', 2003, 3, 'Un mistico codice tra arte e religione'),
('Shutter Island', 'Dennis Lehane', 2003, 3, 'Un investigatore indaga su un misterioso ospedale'),
('La Sesta Sense', 'Bruce Willis', 2000, 3, 'Un bambino può vedere i morti'),
('Il Labirinto dei Versi', 'Carlos Ruiz Zafón', 2001, 3, 'Segreti tra i libri di una biblioteca'),
('Rebecca', 'Daphne du Maurier', 1938, 3, 'Una misteriosa prima moglie tormenta il presente'),
('L\'Uomo della Pioggia', 'John Grisham', 1995, 3, 'Un avvocato e un misterioso caso'),
('Angeli e Demoni', 'Dan Brown', 2000, 3, 'Il mondo dell\'arte nasconde pericoli'),
('Il Nome della Rosa', 'Umberto Eco', 1980, 3, 'Un monaco indaga omicidi in un monastero'),
('L\'Assassinio in Oriente Express', 'Agatha Christie', 1934, 3, 'Un giallo storico in treno'),
('Assassinio sul Nilo', 'Agatha Christie', 1937, 3, 'Un delitto durante una crociera'),
('Il Coltello di Cristallo', 'Philip Pullman', 2007, 3, 'Misteri tra mondi paralleli'),
('Gone Girl', 'Gillian Flynn', 2012, 3, 'Uno sparizione misteriosa e bugie'),
('Il Segreto della Casa Buia', 'Kate Morton', 2008, 3, 'Una casa nasconde segreti dal passato'),
('L\'Innocenza dei Criminali', 'John Grisham', 2007, 3, 'Un avvocato difende un innocente'),
('Il Mistero di Sardar', 'Agatha Christie', 1941, 3, 'Investigazione in Medio Oriente');

-- Inserimento libri per Romanzo
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('Orgoglio e Pregiudizio', 'Jane Austen', 1813, 4, 'Il classico amore tra Elizabeth e Darcy'),
('Cime Tempestose', 'Emily Brontë', 1847, 4, 'L\'amore passionale di Heathcliff e Catherine'),
('La Grande Bellezza', 'Paolo Sorrentino', 2013, 4, 'Roma e i segreti del lusso'),
('Buongiorno Tristezza', 'Françoise Sagan', 1954, 4, 'L\'estate di una ragazza spensierata'),
('Il Diario di Anna Frank', 'Anna Frank', 1947, 4, 'Le speranze e i sogni di una giovane in guerra'),
('La Signora di Piccadilly', 'Arnold Bennett', 1902, 4, 'L\'ascesa di una donna ambiziosa'),
('Amore e Guerra', 'Lev Tolstoj', 1869, 4, 'L\'epica delle famiglie nobili russe'),
('Il Mulino sulla Floss', 'George Eliot', 1860, 4, 'Due fratelli divisi dal destino e dal cuore'),
('Addio alle Armi', 'Ernest Hemingway', 1929, 4, 'Amore tra un soldato e un\'infermiera'),
('Lolita', 'Vladimir Nabokov', 1955, 4, 'Un amore ossessivo e trasgressivo'),
('La Lettera di Lord Henry', 'Oscar Wilde', 1890, 4, 'Decadenza e corruzione della bellezza'),
('Il Ritratto della Gioventù', 'F. Scott Fitzgerald', 1925, 4, 'Sogni e disillusioni del Jazz Age'),
('Jane Eyre', 'Charlotte Brontë', 1847, 4, 'Una governante trova amore e riscatto'),
('Wuthering Heights', 'Emily Brontë', 1847, 4, 'Tormenta di passioni su una brughiera'),
('Madame Bovary', 'Gustave Flaubert', 1856, 4, 'Una donna sognante e insoddisfatta');

-- Inserimento libri per Horror
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('Frankenstein', 'Mary Shelley', 1818, 5, 'Un mostro creato dalla scienza terrifica il mondo'),
('Dracula', 'Bram Stoker', 1897, 5, 'Il vampiro più famoso della letteratura'),
('L\'Esorcista', 'William Peter Blatty', 1971, 5, 'Una bambina posseduta da forze oscure'),
('Shining', 'Stephen King', 1977, 5, 'Un albergo invernale nasconde orrori sovrumani'),
('The Stand', 'Stephen King', 1978, 5, 'Un virus sterminatore con sovrumani sopravvissuti'),
('La Mosca', 'George Langelaan', 1957, 5, 'Un esperimento genetico produce orrore'),
('Carrie', 'Stephen King', 1974, 5, 'Una ragazza con poteri telecinetici si vendica'),
('L\'Inferno di Dante', 'Dante Alighieri', 1320, 5, 'Un viaggio attraverso i gironi infernali'),
('Il Fantasma dell\'Opera', 'Gaston Leroux', 1910, 5, 'Un genio musicale deforme terrorizza'),
('Rebecca', 'Daphne du Maurier', 1938, 5, 'Un passato misterioso e inquietante'),
('Insidious', 'Leigh Whannell', 2010, 5, 'Una dimensione parallela piena di demoni'),
('Sinister', 'Scott Derrickson', 2012, 5, 'Filmati di suicidi di massa inquietano'),
('La Notte dei Morti Viventi', 'George A. Romero', 1968, 5, 'Zombie attaccano i vivi'),
('The Ring', 'Gore Verbinski', 2002, 5, 'Una videocassetta assassina'),
('Occhio di Satana', 'William Castle', 1960, 5, 'Uno specchio malefico amplifica il male');

-- Inserimento libri per Avventura
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('Il Conte di Montecristo', 'Alexandre Dumas', 1844, 6, 'Un uomo tradito si vendica dalle prigioni'),
('L\'Isola del Tesoro', 'Robert Louis Stevenson', 1883, 6, 'Una ricerca di tesoro su isole esotiche'),
('Ventimila Leghe Sotto i Mari', 'Jules Verne', 1870, 6, 'Un sottomarino tecnologico esplora i mari'),
('Il Giro del Mondo in Ottanta Giorni', 'Jules Verne', 1873, 6, 'Una sfida per circumnavigare il globo'),
('Robinson Crusoe', 'Daniel Defoe', 1719, 6, 'Un naufrago sopravvive su un\'isola deserta'),
('Le Avventure di Tom Sawyer', 'Mark Twain', 1876, 6, 'Un ragazzaccio tra fiumi e avventure'),
('Le Avventure di Huckleberry Finn', 'Mark Twain', 1884, 6, 'Fuga e libertà lungo il Mississippi'),
('King Kong', 'Delos W. Lovelace', 1932, 6, 'Un mostro gigante su un\'isola perduta'),
('Moby Dick', 'Herman Melville', 1851, 6, 'Una caccia ossessiva a una balena bianca'),
('Lo Hobbit', 'J.R.R. Tolkien', 1937, 6, 'Un piccolo essere va in avventura eroica'),
('L\'Avventura del Naufrago', 'Daniel Defoe', 1719, 6, 'Sopravvivenza e adattamento su un\'isola'),
('Indiana Jones', 'Philip Kaufman', 1981, 6, 'Un archeologo cerca artefatti perduti'),
('Tarzan delle Scimmie', 'Edgar Rice Burroughs', 1912, 6, 'Un uomo cresciuto dalla giungla'),
('Capitano Nemo', 'Jules Verne', 1870, 6, 'Il misterioso capitano di un sottomarino'),
('Pirati dei Caraibi', 'Ted Elliott', 2003, 6, 'Avventure tra pirati e tesori');

-- Inserimento libri per Storico
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('La Citadella', 'A.J. Cronin', 1937, 7, 'Un medico affronta la medicina e la società'),
('La Rivolta dei Figli', 'Riccardo Bacchelli', 1968, 7, 'L\'Italia durante il Risorgimento'),
('La Trama Nera', 'Vincenzo Consolo', 1986, 7, 'La Sicilia di fine ottocento'),
('Il Gattopardo', 'Giuseppe Tomasi di Lampedusa', 1958, 7, 'L\'aristocrazia siciliana durante il Risorgimento'),
('La Giovane Signora', 'Honoré de Balzac', 1847, 7, 'Parigi durante il secondo Impero'),
('I Miserabili', 'Victor Hugo', 1862, 7, 'La Francia rivoluzionaria e il suo popolo'),
('La Rivoluzione Francese', 'Carlyle', 1837, 7, 'Cronaca della caduta della monarchia'),
('Guerra e Pace', 'Lev Tolstoj', 1869, 7, 'La Russia napoleonica attraverso mille vite'),
('La Notte di Fuoco', 'Ken Burns', 2012, 7, 'La Guerra Civile americana'),
('L\'Ombra del Vento', 'Carlos Ruiz Zafón', 2001, 7, 'Barcellona post-guerra civile'),
('Il Segreto della Casa Amarilla', 'Rosario Castellanos', 1963, 7, 'La Spagna coloniale'),
('Ben-Hur', 'Lew Wallace', 1880, 7, 'Il Medio Oriente ai tempi di Cristo'),
('Quo Vadis', 'Henryk Sienkiewicz', 1896, 7, 'Roma pagana durante il cristianesimo'),
('La Città della Gioia', 'Dominique Lapierre', 1985, 7, 'Calcutta e le sue vite intrecciate'),
('Radetzky March', 'Joseph Roth', 1932, 7, 'L\'Impero austro-ungarico in declino');

-- Inserimento libri per Giallo
INSERT INTO libri (titolo, autore, anno_pubblicazione, genere_id, descrizione) VALUES
('La Pallottola Magica', 'Agatha Christie', 1926, 8, 'Un primo caso di Hercule Poirot'),
('L\'Assassinio di Roger Ackroyd', 'Agatha Christie', 1926, 8, 'Un detective e un crimine in un villaggio'),
('Delitto e Castigo', 'Fyodor Dostoevskij', 1866, 8, 'Un crimine tormenta la coscienza'),
('Il Mistero della Chambre Jaune', 'Gaston Leroux', 1907, 8, 'Un giallo impossibile in una stanza gialla'),
('Le Avventure di Sherlock Holmes', 'Arthur Conan Doyle', 1892, 8, 'Il celebre detective e i suoi casi'),
('L\'Esperimento Filby', 'Julian Symons', 1967, 8, 'Un caso complesso e irrisolto'),
('Il Silenzio della Notte', 'Michael Connelly', 2000, 8, 'Un detective di Los Angeles indaga'),
('Verità Sporche', 'Michael Connelly', 1997, 8, 'Un caso di omicidio irrisolto'),
('La Confessione di Harry Quebert', 'Joel Dicker', 2012, 8, 'Un scrittore indaga su un antico delitto'),
('Il Giuramento', 'Harlan Coben', 2005, 8, 'Un uomo ricerca verità nascosta'),
('Codice 404', 'Andrea Camilleri', 2008, 8, 'Un ispettore in Sicilia indaga'),
('La Serie Nera', 'Lorenzo Marone', 2018, 8, 'Napoli e i suoi misteri'),
('Io So', 'Vincenzo Consolo', 1989, 8, 'Il mistero di una morte e una vita'),
('Il Commissario Montalbano', 'Andrea Camilleri', 1994, 8, 'Sicilia e gialli complessi'),
('La Notte Non Aspetta', 'Tana French', 2008, 8, 'Investigatori negli oscuri segreti');
