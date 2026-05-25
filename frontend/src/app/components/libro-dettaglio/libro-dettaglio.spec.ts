import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LibroDettaglio } from './libro-dettaglio';

describe('LibroDettaglio', () => {
  let component: LibroDettaglio;
  let fixture: ComponentFixture<LibroDettaglio>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LibroDettaglio],
    }).compileComponents();

    fixture = TestBed.createComponent(LibroDettaglio);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
