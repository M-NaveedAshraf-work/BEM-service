<template>
  <v-container grid-list-md>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col>
            <v-btn @click="makeFiles" align="center" depressed color="primary">Download Building Project Files</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>BEM Output Graph</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="chart" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Calibration Graph</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="calchart" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Energystar Benchmark Graph</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="energystarchart" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Energystar Piechart</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="energystarpie" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Capx Graph</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="capxchart" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Uncertainty Analysis Graph 1</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="uncertain1" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Uncertainty Analysis Graph 2</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="uncertain2" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Sensitivity Analysis Graph 1</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="sens1" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Sensitivity Analysis Graph 2</v-card-title>
              <v-card-actions class="justify-center">
                <div>
                  <div id="sens2" style="width: 1000px;height:800px;"></div>
                </div>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </v-container>
</template>

<script>
import axios from 'axios';
import ecStat from 'echarts-stat';

export default {
  name: "Graphs",

  data: () => {

    return {
      filename1: null,
      filename2: null,
      filename3: null,
      filename4: null,
      zipName: null,

      // Inputs Graph Data
      inputData: [],
      allData: [],
      monthlySchedule: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      monthlyDeliveredEnergy: [],
      
      // Capx and Cal Graph Data
      dataInterval: 'Monthly',
      hourlySchedule: [],
      yaxis: [],
      actualData: [],
      capxParams: [],
      calParams: [],

      energystarGraphAxis: [],
      energystarGraphData: [],
      energystarData: [],
      subData: [],

      // UQ Graph Data
      UQData: [],
      UQInputs: [],
      firstGraphDataUA: [[
      0
      ]],
      firstGraphNamesUA: [],
      secondGraphDataUA: [],
      secondGraphNamesUA: [],
      firstGraphDataSA: [],
      firstGraphNamesSA: [],
      secondGraphDataSA: [],
      secondGraphNamesSA: [],

    }
  },

  watch: {
    calParams() {
      this.drawChart()
      this.drawChart();
      this.drawChartUncertain1();
      this.drawChartUncertain2();
      this.drawChartSens1();
      this.drawChartSens2();
      this.drawChartCal();
      this.drawChartCapx();
      this.drawChartEnergystar();
      this.drawPieEnergystar();
    }
  },

  methods: {
    makeFiles() {
      this.filename1 = this.inputData.Name + '_input_file'
      this.filename2 = this.inputData.Name + '_estar_file'
      this.filename3 = this.inputData.Name + '_cal_file'
      this.filename4 = this.inputData.Name + '_UQ_file'
      let allData = JSON.stringify(this.allData)
      let estarData = JSON.stringify(this.energystarData)
      let calData = JSON.stringify(this.calParams)
      let UQData = JSON.stringify(this.UQData)
      let blob1 = new Blob([allData], { type: 'application/json' })
      let blob2 = new Blob([estarData], { type: 'application/json' })
      let blob3 = new Blob([calData], { type: 'application/json' })
      let blob4 = new Blob([UQData], { type: 'application/json' })
      if (navigator.msSaveBlob) { // IE 10+
        navigator.msSaveBlob(blob1, this.filename1)
        navigator.msSaveBlob(blob2, this.filename2)
        navigator.msSaveBlob(blob3, this.filename3)
        navigator.msSaveBlob(blob4, this.filename4)
      } else {
        let link1 = document.createElement('a')
        let link2 = document.createElement('a')
        let link3 = document.createElement('a')
        let link4 = document.createElement('a')
        if (link1.download !== undefined) { // feature detection
          // Browsers that support HTML5 download attribute
          let url1 = URL.createObjectURL(blob1)
          link1.setAttribute('href', url1)
          link1.setAttribute('download', this.filename1)
          link1.style.visibility = 'hidden'
          document.body.appendChild(link1)
          link1.click()
          document.body.removeChild(link1)
        }
        if (link2.download !== undefined) { // feature detection
          // Browsers that support HTML5 download attribute
          let url2 = URL.createObjectURL(blob2)
          link2.setAttribute('href', url2)
          link2.setAttribute('download', this.filename2)
          link2.style.visibility = 'hidden'
          document.body.appendChild(link2)
          link2.click()
          document.body.removeChild(link2)
        }
        if (link3.download !== undefined) { // feature detection
          // Browsers that support HTML5 download attribute
          let url3 = URL.createObjectURL(blob3)
          link3.setAttribute('href', url3)
          link3.setAttribute('download', this.filename3)
          link3.style.visibility = 'hidden'
          document.body.appendChild(link3)
          link3.click()
          document.body.removeChild(link3)
        }
        if (link4.download !== undefined) { // feature detection
          // Browsers that support HTML5 download attribute
          let url4 = URL.createObjectURL(blob4)
          link4.setAttribute('href', url4)
          link4.setAttribute('download', this.filename4)
          link4.style.visibility = 'hidden'
          document.body.appendChild(link4)
          link4.click()
          document.body.removeChild(link4)
        }
      } 
    },

    getGraphData() {
      const path = 'http://localhost:5000/graph';
      axios.get(path)
        .then((res) => {
          this.inputData = res.data.inputData.jsonData
          this.allData = res.data.inputData

          this.monthlyDeliveredEnergy = res.data.monthly

          this.calParams = res.data.calData;
          this.capxParams = res.data.capxData;
          this.energystarData = res.data.estarData;
          this.energystarGraphData = res.data.estarData.benchmark
          this.energystarGraphAxis = res.data.build_index
          this.actualData = res.data.real
          this.calData = res.data.modeled
          this.dataInteval = res.data.interval
          this.subData = res.data.subs

          this.firstGraphDataUA = res.data.runUQData.firstGraphDataUA
          this.firstGraphNamesUA = res.data.runUQData.firstGraphNamesUA
          this.secondGraphDataUA = res.data.runUQData.secondGraphDataUA
          this.secondGraphNamesUA = res.data.runUQData.secondGraphNamesUA
          this.firstGraphDataSA = res.data.runUQData.firstGraphDataSA
          this.firstGraphNamesSA = res.data.runUQData.firstGraphNamesSA
          this.secondGraphDataSA = res.data.runUQData.secondGraphDataSA
          this.secondGraphNamesSA = res.data.runUQData.secondGraphNamesSA
          this.UQData = res.data.UQData
          this.UQParams = res.data.UQData.UQParams;
          this.heatParams = res.data.UQData.heatParams;
          this.UQInputs = res.data.UQData.UQInputs;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    drawChart() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("chart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Monthly Delivered Energy'
        },
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.monthlySchedule
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.monthlyDeliveredEnergy
          },
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartCal() {
      if (this.dataInterval == "Monthly") {
        this.yaxis = this.monthlySchedule
      } else if (this.dataInterval == "Hourly") {
        this.yaxis = this.hourlySchedule  
      }
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("calchart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Actual vs Calibrated Delivered Energy'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['Actual', 'Simulated'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '10%',
          containLabel: true
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          },
          {
            type: 'inside',
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          }
        ],
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.yaxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Actual Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.actualData
          },
          {
            name: 'Calibrated Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.calData
          },
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartCapx() {
      if (this.dataInterval == "Monthly") {
        this.yaxis = this.monthlySchedule
      } else if (this.dataInterval == "Hourly") {
        this.yaxis = this.hourlySchedule  
      }
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("capxchart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Actual vs CapX Technology Infused Delivered Energy'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['Actual', 'CapX'],
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '10%',
          containLabel: true
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            show: true,
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          },
          {
            type: 'inside',
            realtime: true,
            start: 0,
            end: 100,
            xAxisIndex: [0,1]
          }
        ],
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.yaxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Actual Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.actualData
          },
          {
            name: 'CapX Tech Implemented Delivered Energy',
            type: 'line',
            stack: 'Total',
            data: this.capxData
          },
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartEnergystar() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("energystarchart"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'EUI Benchmarking'
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data: this.energystarGraphAxis
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            type: 'bar',
            data: this.energystarGraphData,
            markLine: {
              data: [{name: 'Source Building EUI', yAxis: this.energystarData.score.sourceEUI,
                lineStyle: {
                  color: 'red'
                }
              }],
            }
          },
        ],
      };
      option && myChart.setOption(option);
    },

    drawPieEnergystar() {
      console.log('hello')
      console.log(this.subData)
      
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("energystarpie"));
      //Specify configuration items and data for the chart
      let option = {
        title: {
          text: 'Energy Use Break Down (kWh)',
          left: 'center'
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: this.subData[0][0], name: 'Heating' },
              { value: this.subData[1][0], name: 'Cooling' },
              { value: this.subData[2][0], name: 'Lighting' },
              { value: this.subData[3][0], name: 'Fans' },
              { value: this.subData[4][0], name: 'Pumps' },
              { value: this.subData[5][0], name: 'Plug Load' },
              { value: this.subData[6][0], name: 'DHW' },
              { value: this.subData[7][0], name: 'Electric Vehicle' },
              { value: this.subData[8][0], name: 'PV' },
              { value: this.subData[9][0], name: 'Wind' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartUncertain1() {
      console.log(this.firstGraphDataUA)
      //Initialize the echarts instance based on the prepared dom
      this.$echarts.registerTransform(ecStat.transform.histogram)
      let myChart = this.$echarts.init(document.getElementById("uncertain1"));
      //Specify configuration items and data for the chart
      let option = {
        dataset: [{
        source: this.firstGraphDataUA
        }, {
          transform: {
              type: 'ecStat:histogram'
          }
        }],
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        tooltip: {
        },
        xAxis: {
            type: 'category',
            scale: true
        },
        yAxis: {},
        series: {
            name: 'histogram',
            type: 'bar',
            barWidth: '99.3%',
            label: {
                show: true,
                position: 'top'
            },
            datasetIndex: 1
        }
      };
      option && myChart.setOption(option);
    },

    drawChartUncertain2() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("uncertain2"));
      //Specify configuration items and data for the chart
      let option = {
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          data: this.secondGraphDataUA
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: this.secondGraphNamesUA,
            type: 'line',
            smooth: true
          }
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartSens1() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("sens1"));
      //Specify configuration items and data for the chart
      const labelRight = {
        position: 'right'
      };
      let option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          top: 80,
          bottom: 30
        },
        xAxis: {
          name: 'mu',
          type: 'value',
          position: 'top',
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          }
        },
        yAxis: {
          type: 'category',
          axisLine: { show: false },
          axisLabel: { show: false },
          axisTick: { show: false },
          splitLine: { show: false },
          data: this.firstGraphNamesSA
        },
        series: [
          {
            type: 'bar',
            stack: 'Total',
            label: {
              show: true,
              formatter: '{b}'
            },
            data: this.firstGraphDataSA
          }
        ]
      };
      option && myChart.setOption(option);
    },

    drawChartSens2() {
      console.log(this.secondGraphNamesSA)
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("sens2"));
      //Specify configuration items and data for the chart
      let option = {
        xAxis: {
          name: 'mu*'
        },
        yAxis: {
          name: 'sigma'
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        series: [
          {
            symbolSize: 20,
            itemStyle: {
                normal: {
                    color: 'lightblue',
                    borderWidth: 4,
                    label : {
                        show: true,
                        position: 'inside',
                        formatter: function(data){
                            var v = data.value;
                            return v
                        }
                    }
                }
            },
            data: this.secondGraphDataSA,
            type: 'scatter'
          }
        ]
      };
      option && myChart.setOption(option);
    },
  },

  created() {
    this.getGraphData();
    this.drawChart();
    this.drawChartUncertain1();
    this.drawChartUncertain2();
    this.drawChartSens1();
    this.drawChartSens2();
    this.drawChartCal();
    this.drawChartCapx();
    this.drawChartEnergystar();
    this.drawPieEnergystar();
  },

  mounted() {
    this.drawChart();
    this.drawChart();
    this.drawChartUncertain1();
    this.drawChartUncertain2();
    this.drawChartSens1();
    this.drawChartSens2();
    this.drawChartCal();
    this.drawChartCapx();
    this.drawChartEnergystar();
    this.drawPieEnergystar();
  }
};
</script>
