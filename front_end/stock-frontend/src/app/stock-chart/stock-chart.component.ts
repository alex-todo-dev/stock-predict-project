import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgxChartsModule,Color, ScaleType } from '@swimlane/ngx-charts'; 
import { ChartDataService } from '../services/chart-data.service';
import { TrackedStock } from '../models/tracked-stocks.interface';
import { chartDataLine, chartPoint } from '../models/chart-data';

@Component({
    selector: 'app-stock-chart',
    standalone: true,
    imports: [CommonModule, NgxChartsModule],
    templateUrl: './stock-chart.component.html',
    styleUrl: './stock-chart.component.css'
})
export class StockChartComponent implements OnInit {
    charTitle = 'Line Chart';
    chartData:chartDataLine[] = []
    private cardData: TrackedStock | null = null;
    constructor(private chartDataService: ChartDataService) { }
    ngOnInit(): void {
        this.chartDataService.chartData$.subscribe(data => {
          if (data){
            this.chartData = [];
            this.cardData! = data;
            console.log("chart update:", this.cardData);
            // Gneretaing array from the recived data
            this.charTitle = this.cardData.stock_title;
            let actualPricLine = this.cardData.days_tracking.map(
              obj => ({
                name: new Date(obj.date),
                value: obj.closing_price
              })
            );
            let predictedPriceLine = this.cardData.next_day_predictions.map(
              obj => ({
                name: new Date(obj.date),
                value: obj.closing_price
              })
            );
            this.chartData.push({ name: 'Actual Price', series: actualPricLine });
            this.chartData.push({ name: 'Predicted Price', series: predictedPriceLine });
          }
          console.log("chart data:", this.chartData);
        });
    }
    lineChartData = [
        {
          name: 'Sales 2024',
          series: [
            { name: 'Jan', value: 5000 },
            { name: 'Feb', value: 7200 },
            { name: 'Mar', value: 6100 },
            { name: 'Apr', value: 2 }
          ]
        },
        {
          name: 'Sales 2023',
          series: [
            { name: 'Jan', value: 4800 },
            { name: 'Feb', value: 6800 },
            { name: 'Mar', value: 5900 },
            { name: 'Apr', value: 8000 }
          ]
        }
      ];
    
      // colorScheme = 'vivid'; // or 'cool', 'natural', etc.
      colorScheme: Color = {
        name: 'custom',
        selectable: true,
        group: ScaleType.Ordinal,
        domain: ['#e6194b', '#3cb44b'] // red, green
      };

}
