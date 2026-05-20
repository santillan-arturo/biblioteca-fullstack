import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app'; // <-- Lascialo così se il file si chiama app.ts dentro la cartella app

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));