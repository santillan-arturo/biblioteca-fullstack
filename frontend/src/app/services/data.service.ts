import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  // 1. Recupera la lista di tutte le categorie/generi
  getCategorie(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/api/categorie`);
  }

  // 2. Recupera i libri filtrati per categoria ed eventualmente per stringa di ricerca
  getLibri(categoriaId?: number, search?: string): Observable<any[]> {
    let url = `${this.baseUrl}/api/libri?`;
    if (categoriaId) {
      url += `categoria_id=${categoriaId}&`;
    }
    if (search) {
      url += `search=${encodeURIComponent(search)}&`;
    }
    return this.http.get<any[]>(url);
  }

  // 3. Recupera la scheda di dettaglio di un singolo libro (con JOIN prestiti inclusa)
  getLibroDettaglio(id: number): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/api/libri/${id}`);
  }
}