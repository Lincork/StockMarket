<template>
  <div>
    <div id="container"></div>
  </div>
</template>

<script>
import Highcharts from 'highcharts';
import 'highcharts/highcharts-3d';
import 'highcharts/modules/exporting';
import 'highcharts/modules/accessibility';

export default {
  data() {
    return {
      chartData: [],
    };
  },

  methods: {
    async fetchData() {
      try {
        const response = await fetch(
          'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v10.3.3/samples/data/usdeur.json'
        );

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        this.chartData = await response.json();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
  },

  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      // Highcharts code
      Highcharts.addEvent(Highcharts.Point, 'click', function () {
        if (this.series.options.className.indexOf('popup-on-click') !== -1) {
          const chart = this.series.chart;
          const date = Highcharts.dateFormat('%A, %b %e, %Y', this.x);
          const text = `<b>${date}</b><br/>${this.y} ${this.series.name}`;

          const anchorX = this.plotX + this.series.xAxis.pos;
          const anchorY = this.plotY + this.series.yAxis.pos;
          const align = anchorX < chart.chartWidth - 200 ? 'left' : 'right';
          const x = align === 'left' ? anchorX + 10 : anchorX - 10;
          const y = anchorY - 30;
          if (!chart.sticky) {
            chart.sticky = chart.renderer
              .label(text, x, y, 'callout', anchorX, anchorY)
              .attr({
                align,
                fill: 'rgba(0, 0, 0, 0.75)',
                padding: 10,
                zIndex: 7 // Above series, below tooltip
              })
              .css({
                color: 'white'
              })
              .on('click', function () {
                chart.sticky = chart.sticky.destroy();
              })
              .add();
          } else {
            chart.sticky
              .attr({ align, text })
              .animate({ anchorX, anchorY, x, y }, { duration: 250 });
          }
        }
      });

      this.chart = Highcharts.chart('container', {
        chart: {
          scrollablePlotArea: {
            minWidth: 700
          }
        },
        data: {
          csvURL: 'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/analytics.csv',
          beforeParse: function (csv) {
            return csv.replace(/\n\n/g, '\n');
          }
        },
        title: {
          text: 'Daily sessions at www.highcharts.com',
          align: 'left'
        },
        subtitle: {
          text: 'Source: Google Analytics',
          align: 'left'
        },
        xAxis: {
          tickInterval: 7 * 24 * 3600 * 1000, // one week
          tickWidth: 0,
          gridLineWidth: 1,
          labels: {
            align: 'left',
            x: 3,
            y: -3
          }
        },
        yAxis: [{ // left y axis
          title: {
            text: null
          },
          labels: {
            align: 'left',
            x: 3,
            y: 16,
            format: '{value:.,0f}'
          },
          showFirstLabel: false
        }, { // right y axis
          linkedTo: 0,
          gridLineWidth: 0,
          opposite: true,
          title: {
            text: null
          },
          labels: {
            align: 'right',
            x: -3,
            y: 16,
            format: '{value:.,0f}'
          },
          showFirstLabel: false
        }],
        legend: {
          align: 'left',
          verticalAlign: 'top',
          borderWidth: 0
        },
        tooltip: {
          shared: true,
          crosshairs: true
        },
        plotOptions: {
          series: {
            cursor: 'pointer',
            className: 'popup-on-click',
            marker: {
              lineWidth: 1
            }
          }
        },
        series: [{
          name: 'All sessions',
          lineWidth: 4,
          marker: {
            radius: 4
          }
        }, {
          name: 'New users'
        }]
      });
    }
  }
},
};
</script>

<style>
/* You can add any additional styles here if needed */
</style>
