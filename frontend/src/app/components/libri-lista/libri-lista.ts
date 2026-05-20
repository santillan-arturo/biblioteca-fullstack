import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms'; // <-- Fondamentale per la barra di ricerca
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-libri-lista',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './libri-lista.html',
  styleUrl: './libri-lista.css'
})
export class LibriLista implements OnInit {
  categoriaId!: number;
  libriList: any[] = [];
  searchQuery: string = '';
  loading = true;

  constructor(
    private route: ActivatedRoute,
    private dataService: DataService
  ) { }

  ngOnInit(): void {
    // Recuperiamo l'id della categoria dall'URL
    this.route.params.subscribe(params => {
      this.categoriaId = +params['id'];
      this.caricaLibri();
    });
  }

  // Funzione che richiede i dati al backend (chiamata sia all'inizio sia quando si cerca)
  caricaLibri(): void {
    this.loading = true;
    this.dataService.getLibri(this.categoriaId, this.searchQuery).subscribe({
      next: (data) => {
        this.libriList = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.loading = false;
      }
    });
  }

  // Viene eseguita ogni volta che l'utente scrive qualcosa nella barra di ricerca
  onSearchChange(): void {
    this.caricaLibri();
  }
}