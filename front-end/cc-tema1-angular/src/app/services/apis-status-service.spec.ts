import { TestBed, inject } from '@angular/core/testing';
import { ApisStatusService } from './apis-status-service';


describe('ApisStatusServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ApisStatusService]
    });
  });

  it('should be created', inject([ApisStatusService], (service: ApisStatusService) => {
    expect(service).toBeTruthy();
  }));
});
