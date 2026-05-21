import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router'; 
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-categorie',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './categorie.html',
  styleUrls: ['./categorie.css']
})
export class Categorie implements OnInit {
  categorie: any[] = [
    { id: 1, nome: 'Fantasy', descrizione: 'Avventura, magia e mondi immaginari.' },
    { id: 2, nome: 'Giallo', descrizione: 'Mistero, indagini e suspense.' },
    { id: 3, nome: 'Fantascienza', descrizione: 'Tecnologia, futuri e immaginazione.' },
    { id: 4, nome: 'Romanzo Storico', descrizione: 'Storie ambientate nel passato.' },
    { id: 5, nome: 'Classici', descrizione: 'Opere intramontabili della letteratura.' },
    { id: 6, nome: 'Romanzo Rosa', descrizione: 'Amore e sentimenti al centro della trama.' }
  ];

  private categorieDiFallback = [...this.categorie];

  constructor(private dataService: DataService, private router: Router) { }

  ngOnInit(): void {
    this.caricaCategorie();
  }

  caricaCategorie(): void {
    // Chiamiamo il servizio per prendere i dati reali da Flask
    this.dataService.getCategorie().subscribe({
      next: (data) => {
        console.log('Dati ricevuti con successo:', data);
        this.categorie = data.length ? data : this.categorieDiFallback;
      },
      error: (err) => {
        console.error('Errore nel recupero delle categorie:', err);
        this.categorie = this.categorieDiFallback;
      }
    });
  }

  selezionaCategoria(idCategoria: number): void {
    // Naviga verso il Livello 2 passando l'ID del genere cliccato
    this.router.navigate(['/categoria', idCategoria]);
  }
}