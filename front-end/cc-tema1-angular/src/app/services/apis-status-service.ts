import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { ServicesStatus } from '../models/running-web-model';

@Injectable()
export class ApisStatusService {

  constructor(private readonly http: HttpClient) {

  }
  protected handleError(error: any): Promise<any> {
    return Promise.reject(error);
  }


  public getAPIsStatus(): Promise<ServicesStatus> {
    const url = 'http://localhost:31338/status';
    return this.http.get<ServicesStatus>(url).
      toPromise();

  }




}
