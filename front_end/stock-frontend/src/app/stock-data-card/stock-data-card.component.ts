import { Component,Input, OnInit } from '@angular/core';
import { DatePipe } from '@angular/common'; 
import { ApiStockService } from '../services/api-stock.service';
import { trainingMetrics } from '../models/training_data';
import { predictionMetrics } from '../models/prediction-metrics';
import { CommonModule } from '@angular/common';
import { CapitalizePipe } from '../capitalize.pipe';
import {MatTooltipModule} from '@angular/material/tooltip';
import {TooltipPosition} from '@angular/material/tooltip';
import {FormControl, FormsModule, ReactiveFormsModule} from '@angular/forms';
@Component({
    selector: 'app-stock-data-card',
    standalone: true,
    imports: [DatePipe, CommonModule, CapitalizePipe, MatTooltipModule],
    templateUrl: './stock-data-card.component.html',
    styleUrl: './stock-data-card.component.css'
})
export class StockDataCardComponent implements OnInit{
  public selectedCardIndex: number | null = null;
  public stockMetric:trainingMetrics | null = null;
  public stockPredictMetric:predictionMetrics | null = null;
  ngOnInit(): void {
    this.apiService.get_tracked_stock_training_metrics(this.stockTitle).subscribe(data => {
      this.stockMetric = data;
      console.log("chart data from mterics component:", this.stockMetric);
    });

    this.apiService.get_predicted_error(this.stockTitle).subscribe(data => {
      this.stockPredictMetric = data;
      console.log("chart data from predict mterics component:", this.stockPredictMetric);
    });
  }
  constructor(private apiService: ApiStockService) { 

  }
  @Input() stockTitle: string = 'Stock Title';
  @Input() buyFlagDate: Date = new Date();
  @Input() priceAtFlag: number = 0;
  @Input() nextDayPrediction: number = 0;
  @Input() buyFlagValue: number = 0;

  positionOptions: TooltipPosition[] = ['after', 'before', 'above', 'below', 'left', 'right'];
  position = new FormControl(this.positionOptions[0]);
  selectCard(index: number): void {
    this.selectedCardIndex = index;
  }

}
