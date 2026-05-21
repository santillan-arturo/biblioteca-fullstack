import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-libro-dettaglio',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './libro-dettaglio.html',
  styleUrl: './libro-dettaglio.css'
})
export class LibroDettaglio implements OnInit {
  libroId!: number;
  libroInfo: any = null;
  loading = true;

  constructor(
    private route: ActivatedRoute,
    private dataService: DataService
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.libroId = +params['id'];
      this.caricaDettaglio();
    });
  }

  caricaDettaglio(): void {
    this.dataService.getLibroDettaglio(this.libroId).subscribe({
      next: (data) => {
        this.libroInfo = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.loading = false;
      }
    });
  }
}