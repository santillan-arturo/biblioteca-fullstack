import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

import { routes } from './app.routes';

export const applicationConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient()

import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),      // Connette la mappa delle strade (app.routes.ts)
    provideHttpClient()         // Permette ad Angular di parlare con il backend Flask
  ]
};