import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Libro } from '../models/libro.model';

@Injectable({
  providedIn: 'root'
})
export class LibroService {
  // L'indirizzo del nostro server Flask (quello attivo sulla porta 5000)
      private apiUrl = 'https://turbo-sniffle-pjp44qw7qjwjh6v6r-5000.app.github.dev/api/libri';
  constructor(private http: HttpClient) { }

  // Metodo per inviare il nuovo libro al database (Compito Studente A)
  aggiungiLibro(libro: Libro): Observable<any> {
    return this.http.post<any>(this.apiUrl, libro);
  }
}