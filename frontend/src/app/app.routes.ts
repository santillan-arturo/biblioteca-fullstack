import { Routes } from '@angular/router';
import { Categorie } from './components/categorie/categorie';
import { LibriLista } from './components/libri-lista/libri-lista';
import { LibroDettaglio } from './components/libro-dettaglio/libro-dettaglio';

export const routes: Routes = [
  // Livello 1: Home Categorie
  { path: '', component: Categorie },
  
  // Livello 2: Lista Libri per Categoria
  { path: 'categoria/:id', component: LibriLista },
  
  // Livello 3: Dettaglio Libro
  { path: 'libro/:id', component: LibroDettaglio },
  
  // Fallback
  { path: '**', redirectTo: '' }
];