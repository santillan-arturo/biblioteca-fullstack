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
  categorie: any[] = []; // Qui verranno salvati i generi da mostrare

  constructor(private dataService: DataService, private router: Router) { }

  ngOnInit(): void {
    this.caricaCategorie();
  }

  caricaCategorie(): void {
    // Chiamiamo il servizio per prendere i dati reali da Flask
    this.dataService.getCategorie().subscribe({
      next: (data) => {
        console.log('Dati ricevuti con successo:', data);
        this.categorie = data; // <--- FONDAMENTALE: Questo riempie la griglia!
      },
      error: (err) => {
        console.error('Errore nel recupero delle categorie:', err);
      }
    });
  }

  selezionaCategoria(idCategoria: number): void {
    // Naviga verso il Livello 2 passando l'ID del genere cliccato
    this.router.navigate(['/libri', idCategoria]);
  }
}