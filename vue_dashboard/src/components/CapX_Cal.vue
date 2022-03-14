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
          <v-col offset-md="1">
            <v-card-title>Calibration Parameters</v-card-title>
            <v-row>
              <v-data-table
                :headers="calHeaders"
                :items="calParams"
              >
                <template v-slot:top>
                  <v-toolbar
                    flat
                  >
                    <v-toolbar-title>My Calibration Parameters</v-toolbar-title>
                    <v-divider
                      class="mx-4"
                      inset
                      vertical
                    ></v-divider>
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
                          Add Calibration Parameter
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
                                  v-model="editCalForm.name"
                                  :items='calOptions'
                                  label="Parameter Name"
                                ></v-select>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="12"
                                md="12"
                              >
                                <v-select
                                  v-model="editCalForm.data"
                                  :items="floatInt"
                                  label="Data Type"
                                ></v-select>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="12"
                                md="12"
                              >
                                <v-text-field
                                  v-model="editCalForm.min"
                                  type="number"
                                  label="Minimum Value"
                                ></v-text-field>
                              </v-col>
                              <v-col
                                cols="12"
                                sm="12"
                                md="12"
                              >
                                <v-text-field
                                  v-model="editCalForm.max"
                                  label="Maximum Value"
                                ></v-text-field>
                              </v-col>
                            </v-row>
                          </v-container>
                        </v-card-text>

                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="calClose"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                            color="blue darken-1"
                            text
                            @click="calSave"
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
                          <v-btn color="blue darken-1" text @click="calCloseDelete">Cancel</v-btn>
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
                    @click="getMessage"
                  >
                    Reset
                  </v-btn>
                </template>
              </v-data-table>
            </v-row>
          </v-col>
          <v-row justify="center">
            <v-btn 
              align="center"
              depressed
              color="primary"
              v-on:click="sendMessage()"
            >Run Calibration</v-btn>
          </v-row>
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
    <v-row>
      <v-divider></v-divider>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Energy Star</v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-divider></v-divider>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>CapX</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default{
  name: "CapX_Cal",

  data: () => {

    return {

      calCapBool: ['CapX', 'Calibration'],
      dateInterval: ['Monthly', 'Daily', 'Hourly'],
      ynBool: ['Yes', 'No'],
      dialog: false,
      dialogDelete: false,

      max25chars: v => v.length <= 25 || 'Input too long!',
      pagination: {},
      calBool:false,
      calColor: '',
      calText: '',
      floatInt: ['Float', 'Integer'],
      calOptions: ['Heating COP',
                  'Cooling COP',
                  'Extra ventilation above fresh air supply',
                  'Heat Recovery Type',
                  'Exhaust Air Recirculation Percentage',
                  'Building air leakage level',
                  'Specific Fan Power',
                  'Fan Control Factor',
                  'DHW Generation System',
                  'Occupancy',
                  'Appliance',
                  'Lighting',
                  'Outdoor Air',
                  'DHW',
                  'Roof1 Uvalue',
                  'Roof1 Absorption coefficient',
                  'Roof1 Emissivity',
                  'Opaque1 Uvalue',
                  'Opaque1 Absorption coefficient',
                  'Opaque1 Emissivity',
                  'Window1 Uvalue',
                  'Window1 Emissivity',
                  'Window1 Solar transmittance',
                  'Window1 SRF_S',
                  'Window1 SRF_SE',
                  'Window1 SRF_E',
                  'Window1 SRF_NE',
                  'Window1 SRF_N',
                  'Window1 SRF_NW',
                  'Window1 SRF_W',
                  'Window1 SRF_SW',
                  'Retail Refri Capacity',
                  'EV Charger Power',
                  'Garage Appliance', 
                  'Garage Lighting',
                  'Lighting Dimmer Weekday',
                  'Lighting Dimmer Weekend',
                  'Occupancy Monthly',
                  'Appliance Monthly',
                  'Lighting Monthly',
                  'Window1 SRF All',
                  ],

      calHeaders: [
        {
          text: 'Calibration Parameters',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Type', value: 'data' },
        { text: 'Minimum', value: 'min' },
        { text: 'Maximum', value: 'max' },
        { text: 'Actions', value: 'actions',sortable: false },
      ],

      calParams: [],
      editedIndex: -1,

      addCalForm: {
        name: '',
        data: '',
        min: '',
        max: '',
      },

      editCalForm: {
        name: '',
        data: '',
        min: '',
        max: '',
      },
      defaultCalForm: {
        name: '',
        data: '',
        min: '',
        max: '',
      },


      monthlySchedule: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      actualData: [0,0,0,0,0,0,0,0,0,0,0,0],
      calData: [0,0,0,0,0,0,0,0,0,0,0,0],
      msg: null,
    }

  },

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },

  created() {
    this.getMessage();
  },

  mounted() {
    this.drawChartCal()
  },

  methods: {

    getMessage() {
      const path = 'http://localhost:5000/Cal';
      axios.get(path)
        .then((res) => {
          this.calParams = res.data.calData;
          console.log(this.calParams)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    sendMessage() {
      const path = 'http://127.0.0.1:5000/Cal'
      let calData = this.calParams
      axios.put(path, calData)
      .then(() => {
        this.getMessage();
      })
      .catch((error) => {
        console.error(error);
        this.getMessage();
      })
    },

    editItem(item) {
      this.editedIndex = this.calParams.indexOf(item)
      this.editCalForm = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.calParams.indexOf(item)
      this.editCalForm = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.calParams.splice(this.editedIndex, 1)
      this.calCloseDelete()
    },

    calClose() {
      this.dialog = false

      this.$nextTick(() => {
        this.editCalForm = Object.assign({}, this.defaultCalForm)
        this.editedIndex = -1
      })
    },

    calCloseDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultCalForm)
        this.editedIndex = -1
      })
    }, 

    calSave() {
      if (this.editedIndex > -1) {
        Object.assign(this.calParams[this.editedIndex], this.editCalForm)
      } else {
        this.calParams.push(this.editCalForm)
      }
      this.calClose()
    },

    save() {
      this.calBool = true
      this.calColor = 'success'
      this.calText = 'Data saved'
      console.log(this.calParams)
    },
    cancel() {
      this.calBool = true
      this.calColor = 'error'
      this.calText = 'Canceled'
    },
    open() {
      this.calBool = true
      this.calColor = 'info'
      this.calText = 'Dialog opened'
    },
    close() {
      console.log('Dialog closed')
    },

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

}
</script>



