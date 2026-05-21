import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { LibroService } from './services/libro.service';
import { Libro } from './models/libro.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent {
  title = 'Gestione Biblioteca - Inserimento';

  nuovoLibro: Libro = {
    titolo: '',
    isbn: '',
    anno_pubblicazione: undefined,
    fk_genere: undefined,
    fk_edizione: undefined
  };

  messaggioSuccesso: string = '';
  messaggioErrore: string = '';

  constructor(private libroService: LibroService) {}

  inviaForm() {
    this.messaggioSuccesso = '';
    this.messaggioErrore = '';

    this.libroService.aggiungiLibro(this.nuovoLibro).subscribe({
      next: (risposta) => {
        this.messaggioSuccesso = risposta.messaggio;
        this.resetForm();
      },
      error: (errore) => {
        this.messaggioErrore = errore.error?.errore || 'Si è verificato un errore durante il salvataggio.';
        console.error(errore);
      }
    });
  }

  resetForm() {
    this.nuovoLibro = {
      titolo: '',
      isbn: '',
      anno_pubblicazione: undefined,
      fk_genere: undefined,
      fk_edizione: undefined
    };
  }
}