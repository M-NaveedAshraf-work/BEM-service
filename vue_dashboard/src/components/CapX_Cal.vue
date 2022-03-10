<template>
  <v-container grid-list-md>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Genetic Algorithm Inputs</v-card-title>
          <v-col offset-md="1" md="10">
            <div>
              <v-expansion-panels multiple>
                <v-expansion-panel>
                  <v-expansion-panel-header>Edit Inputs</v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-text-field
                        label = "Population Size [ea]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Crossover Rate"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Mutation Rate"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Random Seed"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Maximum Code Execution Time [min]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-select
                        :items="calCapBool"
                        label = "Calibration or CapX?"
                        outlined
                        dense
                      ></v-select>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Top Percentage of Selection"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-select
                        :items="dateInterval"
                        label = "Calibration Data Interval"
                        outlined
                        dense
                      ></v-select>
                    </v-row>
                    <v-row>
                      <v-select
                        :items="ynBool"
                        label = "Electricity Data"
                        outlined
                        dense
                      ></v-select>
                    </v-row>
                    <v-row>
                      <v-select
                        :items="ynBool"
                        label = "Natural Gas Data"
                        outlined
                        dense
                      ></v-select>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "cvRMSE Criterion [%]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Convergence Difference"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "N Times of Convergence"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
          </v-col>
        </v-card>
      </v-col>
      <v-col>
        <v-card>
          <v-card-title>Calibration Setting Inputs</v-card-title>
          <v-col offset-md="1" md="10">
            <div>
              <v-expansion-panels>
                <v-expansion-panel>
                  <v-expansion-panel-header>Edit Inputs</v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-text-field
                        label = "Discount Rate"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Period of Analysis [years]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Energy Efficient Measure Budget Restriciton [$]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "EUI Restriction [kWh/m2/yr]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Electricity Cost [$/kWh]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Natural Gas Cost [$/kWh]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Upfront Cost Restriction [$]"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                    <v-row>
                      <v-text-field
                        label = "Max Discrete Converges"
                        outlined
                        dense
                        type="number"
                      ></v-text-field>
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
          </v-col>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Calibration Parameters</v-card-title>
        </v-card>
      </v-col>
      <v-col>
        <v-card>
          <div id="CapX_Cal">
            <div id="calchart" style="width: 800px;height:500px;"></div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import axios from 'axios'

export default{
  name: "CapX_Cal",

  data: () => {

    return {

      calCapBool: ['CapX', 'Calibration'],
      dateInterval: ['Monthly', 'Daily', 'Hourly'],
      ynBool: ['Yes', 'No'],

      monthlySchedule: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      actualData: [0,0,0,0,0,0,0,0,0,0,0,0],
      calData: [0,0,0,0,0,0,0,0,0,0,0,0],
    }

  },

  methods: {

    drawChartCal() {
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
          data: 'BEM Output'
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
  },

  mounted() {
    this.drawChartCal()
  },

}
</script>


