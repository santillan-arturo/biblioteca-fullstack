import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';

@Component({
  selector: 'app-libri-lista',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './libri-lista.html',
  styleUrls: ['./libri-lista.css']
})
export class LibriLista implements OnInit {
  caricamento: boolean = false;
  libri: any[] = [];
  nomeGenere: string = 'Elenco Libri';

  // Database locale con 5 libri per ciascuno dei 6 generi
  private databaseLibri: { [key: number]: { genere: string, lista: any[] } } = {
    1: {
      genere: 'Fantasy',
      lista: [
        { id: 101, titolo: 'Il Signore degli Anelli', autore: 'J.R.R. Tolkien', anno: 1954 },
        { id: 102, titolo: 'Harry Potter e la Pietra Filosofale', autore: 'J.K. Rowling', anno: 1997 },
        { id: 103, titolo: 'Le Cronache di Narnia', autore: 'C.S. Lewis', anno: 1950 },
        { id: 104, titolo: 'Lo Hobbit', autore: 'J.R.R. Tolkien', anno: 1937 },
        { id: 105, titolo: 'Il Trono di Spade', autore: 'George R.R. Martin', anno: 1996 }
      ]
    },
    2: {
      genere: 'Giallo',
      lista: [
        { id: 201, titolo: 'Assassinio sull\'Orient Express', autore: 'Agatha Christie', anno: 1934 },
        { id: 202, titolo: 'Il Mastino dei Baskerville', autore: 'Arthur Conan Doyle', anno: 1902 },
        { id: 203, titolo: 'La forma dell\'acqua', autore: 'Andrea Camilleri', anno: 1994 },
        { id: 204, titolo: 'Dieci Piccoli Indiani', autore: 'Agatha Christie', anno: 1939 },
        { id: 205, titolo: 'Il suggeritore', autore: 'Donato Carrisi', anno: 2009 }
      ]
    },
    3: {
      genere: 'Fantascienza',
      lista: [
        { id: 301, titolo: 'Dune', autore: 'Frank Herbert', anno: 1965 },
        { id: 302, titolo: 'Fahrenheit 451', autore: 'Ray Bradbury', anno: 1953 },
        { id: 303, titolo: 'Guida galattica per gli autostoppisti', autore: 'Douglas Adams', anno: 1979 },
        { id: 304, titolo: 'Neuromante', autore: 'William Gibson', anno: 1984 },
        { id: 305, titolo: 'Io, Robot', autore: 'Isaac Asimov', anno: 1950 }
      ]
    },
    4: {
      genere: 'Romanzo Storico',
      lista: [
        { id: 401, titolo: 'I promessi sposi', autore: 'Alessandro Manzoni', anno: 1827 },
        { id: 402, titolo: 'Il nome della rosa', autore: 'Umberto Eco', anno: 1980 },
        { id: 403, titolo: 'I pilastri della terra', autore: 'Ken Follett', anno: 1989 },
        { id: 404, titolo: 'Q', autore: 'Luther Blissett', anno: 1999 },
        { id: 405, titolo: 'Scirocco', autore: 'Giuseppina Torregrossa', anno: 2012 }
      ]
    },
    5: {
      genere: 'Classico',
      lista: [
        { id: 501, titolo: 'Orgoglio e pregiudizio', autore: 'Jane Austen', anno: 1813 },
        { id: 502, titolo: '1984', autore: 'George Orwell', anno: 1949 },
        { id: 503, titolo: 'Il grande Gatsby', autore: 'F. Scott Fitzgerald', anno: 1925 },
        { id: 504, titolo: 'Moby Dick', autore: 'Herman Melville', anno: 1851 },
        { id: 505, titolo: 'Delitto e castigo', autore: 'Fëdor Dostoevskij', anno: 1866 }
      ]
    },
    6: {
      genere: 'Romanzo Rosa',
      lista: [
        { id: 601, titolo: 'Cime tempestose', autore: 'Emily Brontë', anno: 147 },
        { id: 602, titolo: 'Il diario di Bridget Jones', autore: 'Helen Fielding', anno: 1996 },
        { id: 603, titolo: 'Colpa delle stelle', autore: 'John Green', anno: 2012 },
        { id: 604, titolo: 'Io prima di te', autore: 'Jojo Moyes', anno: 2012 },
        { id: 605, titolo: 'Un amore splendido', autore: 'Danielle Steel', anno: 1981 }
      ]
    }
  };

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const idCategoria = +params['id'];
      const datiGenere = this.databaseLibri[idCategoria];
      
      if (datiGenere) {
        this.libri = datiGenere.lista;
        this.nomeGenere = `Elenco Libri - ${datiGenere.genere}`;
      } else {
        this.libri = [];
        this.nomeGenere = 'Elenco Libri';
      }
    });
  }
}