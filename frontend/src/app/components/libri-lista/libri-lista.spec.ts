import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LibriLista } from './libri-lista';

describe('LibriLista', () => {
  let component: LibriLista;
  let fixture: ComponentFixture<LibriLista>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LibriLista],
    }).compileComponents();

    fixture = TestBed.createComponent(LibriLista);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
