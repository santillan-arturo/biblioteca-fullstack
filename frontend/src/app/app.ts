import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { FormsModule } from '@angular/forms';     
import { RouterOutlet } from '@angular/router';   
import { LibroService } from './services/libro.service'; 
import { Libro } from './models/libro.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterOutlet], 
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent {
  // Oggetto legato ai campi dell'HTML
  nuovoLibro: Libro = {
    titolo: '',
    anno_pubblicazione: undefined, 
    isbn: '',
    fk_genere: undefined,          
    fk_edizione: undefined         
  };

  messaggioSuccesso: string = '';
  messaggioErrore: string = '';

  constructor(private libroService: LibroService) { }

  // Funzione che si attiva quando clicchi il bottone del Form
  inviaForm(): void {
    this.libroService.aggiungiLibro(this.nuovoLibro).subscribe({
      next: (response) => {
        this.messaggioSuccesso = '🎉 Libro inserito con successo nel database!';
        this.messaggioErrore = '';
        // Svuota il form dopo l'invio
        this.nuovoLibro = { 
          titolo: '', 
          anno_pubblicazione: undefined, 
          isbn: '', 
          fk_genere: undefined, 
          fk_edizione: undefined 
        };
      },
      error: (err) => {
        this.messaggioErrore = '❌ Errore durante l\'inserimento: ' + (err.error?.errore || err.message);
        this.messaggioSuccesso = '';
      }
    });
  }
}