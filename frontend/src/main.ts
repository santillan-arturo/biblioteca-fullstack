import { bootstrapApplication } from '@angular/platform-browser';
import { applicationConfig } from './app/app.config'; // <-- Prende la configurazione corretta
import { AppComponent } from './app/app';           // <-- Prende la classe AppComponent dal file app.ts

bootstrapApplication(AppComponent, applicationConfig)
  .catch((err) => console.error(err));