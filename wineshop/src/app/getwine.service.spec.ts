import { TestBed } from '@angular/core/testing';

import { GetwineService } from './getwine.service';

describe('GetwineService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GetwineService = TestBed.get(GetwineService);
    expect(service).toBeTruthy();
  });
});
