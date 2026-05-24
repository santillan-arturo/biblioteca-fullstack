import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
// Controlla se il percorso è giusto (se il tuo file ha la 's' o no, es: libro.service o libro.services)
import { LibroService } from '../services/libro.service'; 

@Component({
  selector: 'app-lista-libri',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista-libri.html',
  styleUrls: ['./lista-libri.css']
})
export class ListaLibriComponent implements OnInit {
  libri: any[] = [];

  constructor(private libroService: LibroService) { }

  ngOnInit(): void {
    this.caricaLibri();
  }

  caricaLibri(): void {
    this.libroService.getLibri().subscribe({
      next: (data: any[]) => { // <-- Specificato il tipo per eliminare l'errore TS7006
        this.libri = data;
      },
      error: (err: any) => {  // <-- Specificato il tipo per eliminare l'errore TS7006
        console.error('Errore nel recupero dei libri', err);
      }
    });
  }
}