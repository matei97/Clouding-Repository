import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { ServicesStatus } from '../models/running-web-model';

@Injectable()
export class RunParalelRequestsService {

  constructor(private readonly http: HttpClient) {

  }
  protected handleError(error: any): Promise<any> {
    return Promise.reject(error);
  }


  public runParallelRequests(): void {
    const url = 'http://localhost:31338/runScripts';
    this.http.get(url).toPromise();

  }




}
