import { Routes } from '@angular/router';
import { Categorie } from './components/categorie/categorie';
import { LibriLista } from './components/libri-lista/libri-lista';
import { LibroDettaglio } from './components/libro-dettaglio/libro-dettaglio';

export const routes: Routes = [
  { path: '', pathMatch: 'full', component: Categorie },
  { path: 'categoria/:id', component: LibriLista },
  { path: 'libro/:id', component: LibroDettaglio },
  { path: '**', redirectTo: '' }

import { ListaLibriComponent } from './lista-libri/lista-libri';

export const routes: Routes = [
  { path: 'lista', component: ListaLibriComponent }
 
];