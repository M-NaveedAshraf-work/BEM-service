<template>
  <v-container grid-list-md>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col md="2">
            <v-card>
              <v-card-title>Uncertainty Inputs</v-card-title>
              <v-col>
                <v-text-field
                  v-model="UQInputs.totalSamples"
                  label = "Number of Samples"
                  outlined
                  dense
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-select
                  v-model="UQInputs.energyOutput"
                  label = "SA/UA Outputs"
                  :items="UQ_Outputs"
                  outlined
                  dense
                ></v-select>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <v-col offset-md="1">
                <v-card-title>UQ Parameters</v-card-title>
                <v-row>
                  <v-data-table
                    :headers="UQHeaders"
                    :items="UQParams"
                  >
                    <template v-slot:top>
                      <v-toolbar
                        flat
                      >
                        <v-spacer></v-spacer>
                        <v-dialog
                          v-model="dialog"
                          max-width="500px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              color="primary"
                              dark
                              class="mb-2"
                              v-bind="attrs"
                              v-on="on"
                            >
                              Add Parameter
                            </v-btn>
                          </template>
                          <v-card>
                            <v-card-title>
                              <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                              <v-container>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editUQForm.param"
                                      :items='UQOptions'
                                      label="Parameter Name"
                                    ></v-select>
                                  </v-col>
                                </v-row>
                              </v-container>
                            </v-card-text>

                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="UQClose"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="UQSave"
                              >
                                Save
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDelete" max-width="500px">
                          <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue darken-1" text @click="UQCloseDelete">Cancel</v-btn>
                              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                              <v-spacer></v-spacer>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item }">
                      <v-icon
                        small
                        class="mr-2"
                        @click="editItem(item)"
                      >
                        mdi-pencil
                      </v-icon>
                      <v-icon
                        small
                        @click="deleteItem(item)"
                      >
                        mdi-delete
                      </v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-btn
                        color="primary"
                        @click="getUQ"
                      >
                        Reset
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
              <v-col offset-md="1">
                <v-card-title>Monthly Internal Heat Gain Parameters</v-card-title>
                <v-row>
                  <v-data-table
                    :headers="heatHeaders"
                    :items="heatParams"
                  >
                    <template v-slot:top>
                      <v-toolbar
                        flat
                      >
                        <v-spacer></v-spacer>
                        <v-dialog
                          v-model="dialog2"
                          max-width="500px"
                        >
                          <template v-slot:activator="{ on, attrs }">
                            <v-btn
                              color="primary"
                              dark
                              class="mb-2"
                              v-bind="attrs"
                              v-on="on"
                            >
                              Add Parameter
                            </v-btn>
                          </template>
                          <v-card>
                            <v-card-title>
                              <span class="text-h5">{{ formTitle2 }}</span>
                            </v-card-title>

                            <v-card-text>
                              <v-container>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editHeatForm.param"
                                      :items='UQOptions'
                                      label="Parameter Name"
                                    ></v-select>
                                  </v-col>
                                </v-row>
                                <v-row>
                                  <v-col
                                    cols="12"
                                    sm="12"
                                    md="12"
                                  >
                                    <v-select
                                      v-model="editHeatForm.month"
                                      :items='month'
                                      label="Month"
                                    ></v-select>
                                  </v-col>
                                </v-row>
                              </v-container>
                            </v-card-text>

                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="heatClose"
                              >
                                Cancel
                              </v-btn>
                              <v-btn
                                color="blue darken-1"
                                text
                                @click="heatSave"
                              >
                                Save
                              </v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                        <v-dialog v-model="dialogDelete2" max-width="500px">
                          <v-card>
                            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
                            <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="blue darken-1" text @click="heatCloseDelete">Cancel</v-btn>
                              <v-btn color="blue darken-1" text @click="deleteItemConfirm2">OK</v-btn>
                              <v-spacer></v-spacer>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </v-toolbar>
                    </template>
                    <template v-slot:item.actions="{ item2 }">
                      <v-icon
                        small
                        class="mr-2"
                        @click="editItem2(item2)"
                      >
                        mdi-pencil
                      </v-icon>
                      <v-icon
                        small
                        @click="deleteItem2(item2)"
                      >
                        mdi-delete
                      </v-icon>
                    </template>
                    <template v-slot:no-data>
                      <v-btn
                        color="primary"
                        @click="getUQ"
                      >
                        Reset
                      </v-btn>
                    </template>
                  </v-data-table>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Sensitivity Analysis Specific Inputs</v-card-title>
              <v-col md="12">
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="UQInputs.confidenceLevel"
                      label = "Confidence Level"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="UQInputs.numLevels"
                      label = "Number of Levels"
                      outlined
                      dense
                      type="number"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
          <v-col>
            <v-card height="155">
              <v-card-title>Run UQ Analysis</v-card-title>
              <v-row>
                <v-col>
                  <v-row justify="center">
                    <v-btn
                      :loading="loading" 
                      :disabled="loading"
                      align="center"
                      depressed
                      color="primary"
                      v-on:click="loadState(); UA(); combineData(); sendUQ(); runUQ();"
                    >Run Uncertainty Analysis</v-btn>
                  </v-row>
                </v-col>
                <v-col>
                  <v-row justify="center">
                    <v-btn 
                      :loading="loading2" 
                      :disabled="loading2"
                      align="center"
                      depressed
                      color="primary"
                      v-on:click="loadState2(); SA(); combineData(); sendUQ(); runUQ();"
                    >Run Sensitivity Analysis</v-btn>
                  </v-row>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
    <v-row>
      <v-container></v-container>
    </v-row>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Uncertainty Analysis Graphs</v-card-title>
              <v-col>
                <v-row>
                  <v-col>
                    <div id = "UQ">
                      <div id="uncertain1" style="width: 700px;height:600px;"></div>
                    </div>
                  </v-col>
                  <v-col>
                    <div id = "UQ">
                      <div id="uncertain2" style="width: 700px;height:600px;"></div>
                    </div>
                  </v-col>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
    <v-row>
      <v-container></v-container>
    </v-row>
    <v-sheet color="teal darken-4" elevation="8" rounded shaped>
      <v-container>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Sensitivity Analysis Graphs</v-card-title>
              <v-col>
                <v-row>
                  <v-col>
                    <div id = "UQ">
                      <div id="sens1" style="width: 700px;height:600px;"></div>
                    </div>
                  </v-col>
                  <v-col>
                    <div id = "UQ">
                      <div id="sens2" style="width: 700px;height:600px;"></div>
                    </div>
                  </v-col>
                </v-row>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </v-container>
</template>

<script>
import axios from 'axios';
import ecStat from 'echarts-stat'

export default {
  name: "UQ",

  data: () => {
    
    return {
      // v-select Data
      UQ_Outputs: ["Delivered Energy", "Electricity Use", "Natural Gas Use"],
      UQOptions: ["HeatingCOP",
                  "CoolingCOP",
                  "AirLeakageLevel",
                  "SpecificFanPower",
                  "FanControlFactor",
                  "Occupancy",
                  "Appliance",
                  "Lighting",
                  "OutdoorAir",
                  "Roof UValue",
                  "Roof Absorption Coefficient",
                  "Roof Emissivity",
                  "Opaque UValue",
                  "Opaque Absorption Coefficient",
                  "Opaque Emissivity",
                  "Window UValue",
                  "Window Emissivity",
                  "Window SolarTrasmittance",
                  "Retail Refri Capacity",
                  "EV Charger Power",
                  "Garage Appliance",
                  "Garage Lighting",
                  "Lighting Dimmer Weekday",
                  "Lighting Dimmer Weekend",
                  "Occupancy Monthly",
                  "Appliance Monthly",
                  "Lighting Monthly"
                  ],
      month: ["Jan",
              "Feb",
              "Mar",
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
              "Oct",
              "Nov",
              "Dec"
              ],

      // Parameter Selection Interface Variables
      combine: [],
      UQInputs: [],

      dialog: false,
      dialogDelete: false,
      loading: false,
      calBool:false,

      UQParams: [],
      UQHeaders: [
        {
          test: 'Calibration Parameters',
          align: 'start',
          sortable: false,
          value: 'param',
        },
        { text: 'Actions', value: 'actions', sortable: false}
      ],
      editedIndex: -1,

      editUQForm: {
        param: '',
      },
      defaultUQForm: {
        param: '',
      },

      dialog2: false,
      dialogDelete2: false,
      loading2: false,
      heatBool:false,

      heatParams: [],
      heatHeaders: [
        {
          test: 'Calibration Parameters',
          align: 'start',
          sortable: false,
          value: 'param',
        },
        { text: 'Month', value: 'month', sortable: false},
        { text: 'Actions', value: 'actions', sortable: false}
      ],
      editedIndex2: -1,

      editHeatForm: {
        month: '',
        param: '',
      },
      defaultHeatForm: {
        month: '',
        param: '',
      },
      // Graph Data
      firstGraphDataUA: [[
      0
      ]],
      firstGraphNamesUA: ['blank'],
      secondGraphDataUA: [0],
      secondGraphNamesUA: [0],

      firstGraphDataSA: [0],
      firstGraphNamesSA: ['blank'],
      secondGraphDataSA: [0, 0, 'null'],
      secondGraphNamesSA: ['blank'],
    }
  },

  mounted() {
    this.drawChartUncertain1()
    this.drawChartUncertain2()
    this.drawChartSens1()
    this.drawChartSens2()
  },

  created() {
    this.getUQ();
  },

  watch: {
    firstGraphDataUA() {
      this.loading = false
      this.drawChartUncertain1()
      this.drawChartUncertain2()
    },
    firstGraphDataSA() {
      this.loading2 = false
      this.drawChartSens1()
      this.drawChartSens2()
    },
    UQInputs(){
    },
    loading() {
    },
    loading2(){
    },
    // UQInputs() {
    //   this.sendUQ()
    // }
  },

  methods: {
    loadState() {
      this.loading = "loading"
    },

    loadState2() {
      this.loading2 = "loading2"
    },

    UA() {
      this.UQInputs.UQMode = "Uncertainty Analysis"
    },

    SA() {
      this.UQInputs.UQMode = "Sensitivity Analysis"
    },

    combineData() {
      let UQParams = this.UQParams
      let UQInputs = this.UQInputs
      let heatParams = this.heatParams
      let merged = {UQParams, UQInputs, heatParams}

      this.combine = JSON.stringify(merged)
      console.log(this.combine)
    },

    getUQ() {
      const path = 'http://localhost:5000/UQ';
      axios.get(path)
        .then((res) => {
          this.UQParams = res.data.UQData.UQParams;
          this.heatParams = res.data.UQData.heatParams;
          this.UQInputs = res.data.UQData.UQInputs;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    sendUQ() {
      const path = 'http://127.0.0.1:5000/UQ'
      axios.put(path, this.combine)
      .then(() => {
        this.getUQ();
      })
      .catch((error) => {
        console.error(error);
        this.getUQ();
      })
    },

    runUQ() {
      const path = 'http://localhost:5000/runUQ';
      axios.get(path)
        .then((res) => {
          this.sendUQ()
          let status = this.UQInputs.UQMode
          if (status == 'Uncertainty Analysis') {
            console.log('uploaded UA')
            this.firstGraphDataUA = res.data.firstGraphDataUA
            this.firstGraphNamesUA = res.data.firstGraphNamesUA
            this.secondGraphDataUA = res.data.secondGraphDataUA
            this.secondGraphNamesUA = res.data.secondGraphNamesUA
          } else if (status == 'Sensitivity Analysis') {
            console.log('uploaded SA')
            this.firstGraphDataSA = res.data.firstGraphDataSA
            this.firstGraphNamesSA = res.data.firstGraphNamesSA
            this.secondGraphDataSA = res.data.secondGraphDataSA
            this.secondGraphNamesSA = res.data.secondGraphNamesSA
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    // getHeat() {
    //   const path = 'http://localhost:5000/UQ';
    //   axios.get(path)
    //     .then((res) => {
    //       this.heatParams = res.data.heatData;
    //     })
    //     .catch((error) => {
    //       // eslint-disable-next-line
    //       console.error(error);
    //     });
    // },

    // sendHeat() {
    //   const path = 'http://127.0.0.1:5000/UQ'
    //   let heatData = this.heatParams
    //   axios.put(path, heatData)
    //   .then(() => {
    //     this.getHeat();
    //   })
    //   .catch((error) => {
    //     console.error(error);
    //     this.getHeat();
    //   })
    // },

    editItem(item) {
      this.editedIndex = this.UQParams.indexOf(item)
      this.editUQForm = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.UQParams.indexOf(item)
      this.editUQForm = Object.assign({}, item)
      // this.dialogDelete = true
      this.deleteItemConfirm()
    },

    deleteItemConfirm() {
      this.UQParams.splice(this.editedIndex, 1)
      this.UQCloseDelete()
    },

    UQClose() {
      this.dialog = false

      this.$nextTick(() => {
        this.editUQForm = Object.assign({}, this.defaultUQForm)
        this.editedIndex = -1
      })
    },

    UQCloseDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultUQForm)
        this.editedIndex = -1
      })
    }, 

    UQSave() {
      if (this.editedIndex > -1) {
        Object.assign(this.UQParams[this.editedIndex], this.editUQForm)
      } else {
        this.UQParams.push(this.editUQForm)
      }
      this.UQClose()
    },

    loadState() {
      this.loading = "loading"
    },

    editItem2(item2) {
      this.editedIndex2 = this.heatParams.indexOf(item2)
      this.editHeatForm = Object.assign({}, item2)
      this.dialog2 = true
    },

    deleteItem2 (item2) {
      this.editedIndex2 = this.heatParams.indexOf(item2)
      this.editHeatForm = Object.assign({}, item2)
      // this.dialogDelete2 = true
      this.deleteItemConfirm2()
    },

    deleteItemConfirm2() {
      this.heatParams.splice(this.editedIndex2, 1)
      this.heatCloseDelete()
    },

    heatClose() {
      this.dialog2 = false

      this.$nextTick(() => {
        this.editHeatForm = Object.assign({}, this.defaultHeatForm)
        this.editedIndex2 = -1
      })
    },

    heatCloseDelete() {
      this.dialogDelete2 = false
      this.$nextTick(() => {
        this.editedItem2 = Object.assign({}, this.defaultHeatForm)
        this.editedIndex2 = -1
      })
    }, 

    heatSave() {
      if (this.editedIndex2 > -1) {
        Object.assign(this.heatParams[this.editedIndex2], this.editHeatForm)
      } else {
        this.heatParams.push(this.editHeatForm)
      }
      this.heatClose()
    },

    loadState2() {
      this.loading2 = "loading2"
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

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New UQ Item' : 'Edit UQ Item'
    },
    formTitle2 () {
      return this.editedIndex2 === -1 ? 'New Heat Item' : 'Edit Heat Item'
    },
  },
}

</script>

