import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { TrackedStock } from '../models/tracked-stocks.interface';
@Injectable({
  providedIn: 'root'
})
export class ChartDataService {
  private chartDataSource = new BehaviorSubject<TrackedStock | null>(null);
  chartData$ = this.chartDataSource.asObservable();

  constructor() { }
  updateChartData(data: TrackedStock) {
    this.chartDataSource.next(data);
  }
}
