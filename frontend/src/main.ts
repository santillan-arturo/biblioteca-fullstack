import { bootstrapApplication } from '@angular/platform-browser';
import { applicationConfig } from './app/app.config'; // <-- Prende la configurazione corretta
import { AppComponent } from './app/app';           // <-- Prende la classe AppComponent dal file app.ts

bootstrapApplication(AppComponent, applicationConfig)

import 'zone.js';
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app'; // <-- Guarda dentro app/app.ts

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));