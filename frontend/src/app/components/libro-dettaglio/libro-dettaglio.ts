import { Component, OnInit } from '@angular/core';
import { CommonModule, Location } from '@angular/common'; // Aggiunto Location qui
import { ActivatedRoute, RouterModule } from '@angular/router';

@Component({
  selector: 'app-libro-dettaglio',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './libro-dettaglio.html',
  styleUrls: ['./libro-dettaglio.css']
})
export class LibroDettaglio implements OnInit {
  caricamento: boolean = false;
  libro: any = null;

  private tuttiILibri: { [key: number]: any } = {
    101: { titolo: 'Il Signore degli Anelli', autore: 'J.R.R. Tolkien', isbn: '9788845292613', anno: 1954, categoria: 'FANTASY', prestiti: [{ utente: 'Mattia Neri', data: '12/04/2025', stato: 'Restituito' }] },
    102: { titolo: 'Harry Potter e la Pietra Filosofale', autore: 'J.K. Rowling', isbn: '31537457801', anno: 2020, categoria: 'FANTASY', prestiti: [{ utente: 'Alanta Nastri', data: '17/02/2021', stato: 'Ritiro' }, { utente: 'Jacopo Golnano', data: '17/02/2021', stato: 'Prestito' }, { utente: 'Jasmina Caverez', data: '03/02/2021', stato: 'Ritiro' }] },
    103: { titolo: 'Le Cronache di Narnia', autore: 'C.S. Lewis', isbn: '9788845293009', anno: 1950, categoria: 'FANTASY', prestiti: [] },
    104: { titolo: 'Lo Hobbit', autore: 'J.R.R. Tolkien', isbn: '9788845292620', anno: 1937, categoria: 'FANTASY', prestiti: [] },
    105: { titolo: 'Il Trono di Spade', autore: 'George R.R. Martin', isbn: '9788804711926', anno: 1996, categoria: 'FANTASY', prestiti: [] },
    
    201: { titolo: 'Assassinio sull\'Orient Express', autore: 'Agatha Christie', isbn: '9788804700012', anno: 1934, categoria: 'GIALLO', prestiti: [] },
    202: { titolo: 'Il Mastino dei Baskerville', autore: 'Arthur Conan Doyle', isbn: '9788804700029', anno: 1902, categoria: 'GIALLO', prestiti: [] },
    203: { titolo: 'La forma dell\'acqua', autore: 'Andrea Camilleri', isbn: '9788838910111', anno: 1994, categoria: 'GIALLO', prestiti: [] },
    204: { titolo: 'Dieci Piccoli Indiani', autore: 'Agatha Christie', isbn: '9788804710110', anno: 1939, categoria: 'GIALLO', prestiti: [] },
    205: { titolo: 'Il suggeritore', autore: 'Donato Carrisi', isbn: '9788830426436', anno: 2009, categoria: 'GIALLO', prestiti: [] }
  };

  // Iniettiamo "location" nel costruttore
  constructor(private route: ActivatedRoute, private location: Location) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const idLibro = +params['id'];
      this.libro = this.tuttiILibri[idLibro] || this.tuttiILibri[102];
    });
  }

  // Funzione per tornare indietro alla lista precedente nella cronologia
  tornaIndietro(): void {
    this.location.back();
  }
}