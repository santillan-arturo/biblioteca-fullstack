import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-categorie',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './categorie.html',
  styleUrl: './categorie.css'
})
export class Categorie implements OnInit {
  categorieList: any[] = [];
  loading = true;
  errorMessage = '';

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getCategorie().subscribe({
      next: (data) => {
        this.categorieList = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.errorMessage = 'Errore nel caricamento delle categorie. Verifica che il backend sia attivo!';
        this.loading = false;
      }
    });
  }
}