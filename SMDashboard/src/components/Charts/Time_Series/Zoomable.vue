<template>
  <div>
    <div id="container"></div>
  </div>
</template>

<script>
import Highcharts from 'highcharts'
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

    createChart() {
      Highcharts.chart('container', {
        chart: {
          zoomType: 'x',
        },
        title: {
          text: 'USD to EUR exchange rate over time',
          align: 'left',
        },
        subtitle: {
          text:
            document.ontouchstart === undefined
              ? 'Click and drag in the plot area to zoom in'
              : 'Pinch the chart to zoom in',
          align: 'left',
        },
        xAxis: {
          type: 'datetime',
        },
        yAxis: {
          title: {
            text: 'Exchange rate',
          },
        },
        legend: {
          enabled: false,
        },
        plotOptions: {
          area: {
            fillColor: {
              linearGradient: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 1,
              },
              stops: [
                [0, Highcharts.getOptions().colors[0]],
                [
                  1,
                  Highcharts.color(Highcharts.getOptions().colors[0])
                    .setOpacity(0)
                    .get('rgba'),
                ],
              ],
            },
            marker: {
              radius: 2,
            },
            lineWidth: 1,
            states: {
              hover: {
                lineWidth: 1,
              },
            },
            threshold: null,
          },
        },
        series: [
          {
            type: 'area',
            name: 'USD to EUR',
            data: this.chartData,
          },
        ],
      });
    },
  },

  mounted() {
    this.fetchData().then(() => {
      this.createChart();
    });
  },
};
</script>

<style>
/* Your component styles go here */
</style>
