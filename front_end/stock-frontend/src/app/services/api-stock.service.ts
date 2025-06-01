import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { apiUrls } from './api-urls';
import { TrackedStock } from '../models/tracked-stocks.interface';
import { trainingMetrics } from '../models/training_data';
import { Observable } from 'rxjs';
import { predictionMetrics } from '../models/prediction-metrics';
@Injectable({
  providedIn: 'root'
})
export class ApiStockService {

  constructor(
    private httpClient: HttpClient
  ) { }

  get_tracked_stocks(): Observable<TrackedStock[]> {
    return this.httpClient.get<TrackedStock[]>(apiUrls.base_url + apiUrls.get_tracked_stocks);
  }

  get_tracked_stock_training_metrics(stock: string): Observable<trainingMetrics> {
    return this.httpClient.get<trainingMetrics>(apiUrls.base_url + apiUrls.get_training_matrics + stock);
  }

  get_predicted_error(stock: string): Observable<predictionMetrics> {
    return this.httpClient.get<predictionMetrics>(apiUrls.base_url + apiUrls.get_predicted_metrics + stock);
  }
}

