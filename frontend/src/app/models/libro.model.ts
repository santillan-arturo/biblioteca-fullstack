export interface Libro {
  id?: number;
  titolo: string;
  isbn: string;
  anno_pubblicazione?: number;
  fk_genere?: number;   
  fk_edizione?: number;  
}