import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http'; // <-- Aggiunto HttpClientModule
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-categorie',
  standalone: true,
  imports: [CommonModule, RouterModule, HttpClientModule], // <-- Inserito anche qui negli imports
  templateUrl: './categorie.html'
})
export class Categorie implements OnInit {
  categorie: any[] = [];
  loading: boolean = true;
  errore: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.caricaCategorie();
  }

  caricaCategorie(): void {
    this.loading = true;
    this.errore = '';
    
    this.http.get<any[]>(`${environment.apiUrl}/api/categorie`).subscribe({
      next: (data) => {
        this.categorie = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Errore dettagliato:', err);
        this.errore = 'Errore nel caricamento delle categorie. Verifica la connessione a Flask!';
        this.loading = false;
      }
    });
  }
}