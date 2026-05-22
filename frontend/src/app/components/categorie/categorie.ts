import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-categorie',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './categorie.html',
  styleUrls: ['./categorie.css']
})
export class Categorie implements OnInit {
  constructor() {}
  ngOnInit(): void {}
}