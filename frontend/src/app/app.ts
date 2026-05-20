import { Component } from '@angular/core';
import { RouterOutlet, RouterModule } from '@angular/router'; // <-- Aggiunto RouterModule

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterModule], // <-- Inserito anche qui
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class AppComponent {
  title = 'frontend';
}