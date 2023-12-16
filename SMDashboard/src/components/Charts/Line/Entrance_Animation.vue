<template>
  <div>
    <figure class="highcharts-figure">
      <div ref="chartContainer"></div>
      <p class="highcharts-description">
        This line chart demo shows how to create a custom entrance animation presenting
        the statistics related to the United States of America's Inflation.
      </p>
    </figure>
  </div>
</template>

<script>
import Highcharts from 'highcharts';
import HighchartsBoost from 'highcharts/modules/boost';
import axios from 'axios';
import Papa from 'papaparse';

HighchartsBoost(Highcharts);

export default {
  name: 'InflationChart',
  data() {
    return {
      csvData: null,
    };
  },
  mounted() {
    this.loadCSV();
  },
  methods: {
    async loadCSV() {
      try {
        const csvFilePath = 'data.csv'; // Update with the correct path to your CSV file
        const response = await axios.get(csvFilePath);

        Papa.parse(response.data, {
          header: true,
          dynamicTyping: true,
          delimiter: ",",
          complete: (result) => {
            this.csvData = result.data;
            this.renderChart();
          },
        });
      } catch (error) {
        console.error('Error loading CSV file:', error);
      }
    },
    renderChart() {
      if (this.csvData) {
        Highcharts.chart(this.$refs.chartContainer, {
          chart: {
            type: 'spline'
          },
          title: {
            text: 'United States of America\'s Inflation-related statistics',
            align: 'left'
          },
          subtitle: {
            text: 'Source: <a href="https://www.worldbank.org/en/home">The World Bank</a>',
            align: 'left'
          },
          data: {
            csv: this.convertToCSVFormat(this.csvData)
          },

          yAxis: [{
              title: {
                  text: 'Inflation'
              },
              plotLines: [{
                  color: 'black',
                  width: 2,
                  value: 13.5492019749684,
                  animation: {
                      duration: 1000,
                      defer: 4000
                  },
                  label: {
                      text: 'Max Inflation',
                      align: 'right',
                      x: -20
                  }
              }]
          }, {
              title: {
                  text: 'Claims on central government, etc.'
              }
          }, {
              opposite: true,
              title: {
                  text: 'Net foreign assets'
              }
          }, {
              opposite: true,
              title: {
                  text: 'Net domestic credit'
              }
          }],

          plotOptions: {
              series: {
                  animation: {
                      duration: 1000
                  },
                  marker: {
                      enabled: false
                  },
                  lineWidth: 2
              }
          },

          series: [{
              yAxis: 0
          }, {
              yAxis: 1,
              animation: {
                  defer: 1000
              }
          }, {
              yAxis: 2,
              animation: {
                  defer: 2000
              }
          }, {
              yAxis: 3,
              animation: {
                  defer: 3000
              }
          }],
          responsive: {
            rules: [{
              condition: {
                maxWidth: 500
              },
              chartOptions: {
                yAxis: [{
                  tickAmount: 2,
                  title: {
                    x: 15,
                    reserveSpace: false
                  }
                }, {
                  tickAmount: 2,
                  title: {
                    x: 20,
                    reserveSpace: false
                  }
                }, {
                  tickAmount: 2,
                  title: {
                    x: -20,
                    reserveSpace: false
                  }
                }, {
                  tickAmount: 2,
                  title: {
                    x: -20,
                    reserveSpace: false
                  }
                }]
              }
            }]
          }
        })
      }
    },
    convertToCSVFormat(data) {
      // Convert data to CSV format
      return data.map(item => {
        return Object.values(item).join(';');
      }).join('\n');
    },
  },
};
</script>

<style scoped>
/* Add any necessary styles here */
</style>
