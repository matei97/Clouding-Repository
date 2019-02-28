import { Component } from '@angular/core';
import { ServicesStatus } from './models/running-web-model';
import { CatAPIMetrics } from './models/cat-api-metrics';
import { HolidaysApiRetriveMetricsService } from './services/holidays-api-retrive-metrics.service';
import { ApisStatusService } from './services/apis-status-service';
import { CatsApiRetriveMetricsService } from './services/cats-api-retrive-metrics.service';
import { HolidayAPIMetrics } from './models/holiday-api-metrics';
import { jsonpCallbackContext } from '@angular/common/http/src/module';
import { RunParalelRequestsService } from './services/run-paralel-requests.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApisStatusService, CatsApiRetriveMetricsService, HolidaysApiRetriveMetricsService, RunParalelRequestsService],
})
export class AppComponent {
  public StatusModel: ServicesStatus = new ServicesStatus();
  public CatApiMetricModel: CatAPIMetrics = new CatAPIMetrics();
  public HolidayApiMetricModel: HolidayAPIMetrics = new HolidayAPIMetrics();
  constructor(private readonly AppsStatusServices: ApisStatusService,
    private readonly CatApiMetricsService: CatsApiRetriveMetricsService,
    private readonly HolidayApiMetricService: HolidaysApiRetriveMetricsService,
    private readonly RunParalelRequestsService: RunParalelRequestsService) {
  }

  public getStatusFromService(): void {
    this.AppsStatusServices.getAPIsStatus().then(codes => {
      this.StatusModel = codes;
      console.log(this.StatusModel.HolidayAPIStatus);
      console.log(this.StatusModel.CatAPIStatus);

    });
  }
  public getCatAPIMetric(): void {
    this.HolidayApiMetricModel = new HolidayAPIMetrics();
    this.CatApiMetricsService.getCatApiMetrics().then(metric => {
      this.CatApiMetricModel = metric;
      console.log(this.CatApiMetricModel);

    });
  }
  public getHolidayAPIMetric(): void {
    this.CatApiMetricModel = new CatAPIMetrics();
    this.HolidayApiMetricService.getHolidayApiMetrics().then(metric => {
      this.HolidayApiMetricModel = metric;
      console.log(this.HolidayApiMetricModel);
    });
  }

  public runScripts(): void {
    this.RunParalelRequestsService.runParallelRequests();
  }


}
