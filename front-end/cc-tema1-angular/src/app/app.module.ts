import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { ApisStatusService } from './services/apis-status-service';
import { CatsApiRetriveMetricsService } from './services/cats-api-retrive-metrics.service';
import { HolidaysApiRetriveMetricsService } from './services/holidays-api-retrive-metrics.service';
import { RunParalelRequestsService } from './services/run-paralel-requests.service';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule, HttpClientModule
  ],
  providers: [ApisStatusService, CatsApiRetriveMetricsService, RunParalelRequestsService, HolidaysApiRetriveMetricsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
