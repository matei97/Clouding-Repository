import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import 'rxjs/add/operator/catch';
import { CatAPIMetrics } from '../models/cat-api-metrics';
@Injectable()
export class CatsApiRetriveMetricsService {

  constructor(private readonly http: HttpClient) {

  }
  protected handleError(error: any): Promise<any> {
    return Promise.reject(error);
  }


  public getCatApiMetrics(): Promise<CatAPIMetrics> {
    const url = 'http://localhost:31338/metricsCat';
    return this.http.get<CatAPIMetrics>(url).toPromise().catch();
  }




}
