import { TestBed, inject } from '@angular/core/testing';

import { CatsApiRetriveMetricsService } from './cats-api-retrive-metrics.service';

describe('CatsApiRetriveMetricsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CatsApiRetriveMetricsService]
    });
  });

  it('should be created', inject([CatsApiRetriveMetricsService], (service: CatsApiRetriveMetricsService) => {
    expect(service).toBeTruthy();
  }));
});
