import { TestBed, inject } from '@angular/core/testing';

import { RunParalelRequestsService } from './run-paralel-requests.service';

describe('RunParalelRequestsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RunParalelRequestsService]
    });
  });

  it('should be created', inject([RunParalelRequestsService], (service: RunParalelRequestsService) => {
    expect(service).toBeTruthy();
  }));
});
