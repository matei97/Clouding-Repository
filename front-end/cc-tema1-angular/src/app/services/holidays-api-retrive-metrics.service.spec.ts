import { TestBed, inject } from '@angular/core/testing';
import { HolidaysApiRetriveMetricsService } from './holidays-api-retrive-metrics.service';


describe('HolidaysApiRetriveMetricsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HolidaysApiRetriveMetricsService]
    });
  });

  it('should be created', inject([HolidaysApiRetriveMetricsService], (service: HolidaysApiRetriveMetricsService) => {
    expect(service).toBeTruthy();
  }));
});
