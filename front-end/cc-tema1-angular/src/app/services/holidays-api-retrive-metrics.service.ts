import { Injectable } from '@angular/core';
import 'rxjs/add/operator/catch';
import { HttpClient } from '@angular/common/http';
import { HolidayAPIMetrics } from '../models/holiday-api-metrics';

@Injectable()
export class HolidaysApiRetriveMetricsService {

  constructor(private readonly http: HttpClient) {

  }
  protected handleError(error: any): Promise<any> {
    return Promise.reject(error);
  }


  public getHolidayApiMetrics(): Promise<HolidayAPIMetrics> {
    const url = 'http://localhost:31338/metricsHoliday';
    return this.http.get<HolidayAPIMetrics>(url).toPromise().catch();
  }




}