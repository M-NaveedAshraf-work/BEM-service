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
                :headers = "calHeaders"
                :items = "calParams"
                :items-per-page = "5"
              >
                <template v-slot:item.name="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.name"
                    large
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    {{ props.item.name }}
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        Select Calibration Parameter
                      </div>
                      <v-select
                        v-model="props.item.name"
                        :items='calOptions'
                        label="Edit"
                      ></v-select>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:item.data="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.data"
                    large
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.data }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        Update Data Type
                      </div>
                      <v-select
                        v-model="props.item.data"
                        :items="floatInt"
                        label="Edit"
                      ></v-select>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:item.min="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.min"
                    large
                    persistent
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.min }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        Update Minimum Value
                      </div>
                      <v-text-field
                        v-model="props.item.min"
                        label="Edit"
                        type="number"
                        single-line
                        counter
                        autofocus
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:item.max="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.max"
                    large
                    persistent
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close"
                  >
                    <div>{{ props.item.max }}</div>
                    <template v-slot:input>
                      <div class="mt-4 text-h6">
                        Update Maximum Value
                      </div>
                      <v-text-field
                        v-model="props.item.max"
                        label="Edit"
                        type="number"
                        single-line
                        counter
                        autofocus
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
              </v-data-table>
            </v-row>
            <v-row justify="center">
              <v-dialog
                v-model="dialog"
                persistent
                max-width="600px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="primary"
                    dark
                    v-bind="attrs"
                    v-on="on"
                  >
                    Add Calibration Parameter
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="text-h5">Calibration Parameter</span>
                  </v-card-title>
                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col
                          cols="12"
                        >
                          <v-select
                            v-model="addCalForm.name"
                            :items='calOptions'
                            type='string'
                            label="Calibration Parameter"
                          ></v-select>
                        </v-col>
                        <v-col
                          cols="12"
                        >
                          <v-select
                            v-model="addCalForm.data"
                            :items="floatInt"
                            type='string'
                            label="Calibration Parameter Data Type"
                          ></v-select>
                        </v-col>
                        <v-col cols="12">
                          <v-text-field
                            v-model="addCalForm.min"
                            label="Insert Minimum Value"
                            type="number"
                            required
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12">
                          <v-text-field
                            v-model="addCalForm.max"
                            label="Insert Maximum Value"
                            type="number"
                            required
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
                      @click="close();"
                    >
                      Close
                    </v-btn>
                    <v-btn
                      color="blue darken-1"
                      text
                      @click="save();"
                    >
                      Save
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-row>
          </v-col>
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
import axios from 'axios'

export default{
  name: "CapX_Cal",

  data: () => {

    return {

      calCapBool: ['CapX', 'Calibration'],
      dateInterval: ['Monthly', 'Daily', 'Hourly'],
      ynBool: ['Yes', 'No'],
      dialog: false,

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
      ],

      calParams: [],
      addCalForm: {
        name: '',
        data: '',
        min: '',
        max: '',
      },

      editCalForm: {
        id: '',
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

  methods: {

    getMessage() {
      const path = 'http://localhost:5000/Cal';
      axios.get(path)
        .then((res) => {
          this.calParams = res.data.calData;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    sendMessage(payload) {
      const path = 'http://localhost:5000/Cal';
      axios.post(path, payload)
        .then(() => {
          this.getMessage();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMessage();
        });
    },

    updateCal(payload, calID) {
      const path = 'http://localhost:5000/Cal/${calID}';
      axios.put(path, payload)
      .then(() => {
        console.error(error);
        this.getMessage();
      })
    },

    onResetUpdate(evt) {
      this.getMessage();
    },

    initForm() {
      this.addCalForm.name = '';
      this.addCalForm.data = '';
      this.addCalForm.min = '';
      this.addCalForm.max = '';

      this.editCalForm.id = '';
      this.editCalForm.name = '';
      this.editCalForm.data = '';
      this.editCalForm.min = '';
      this.editCalForm.max = '';
    },

    onSubmit(evt) {
      this.dialog = false

      const payload = {
        name: this.addCalForm.name,
        data: this.addCalForm.data,
        min: this.addCalForm.min,
        max: this.addCalForm.max
      };
      this.sendMessage(payload);
      this.initForm();
    },

    editCal(cal) {
      this.editCalForm = cal;
    },

    onSubmitUpdate() {
      const payload = {
        name: this.editCalForm.name,
        data: this.editCalForm.data,
        min: this.editCalForm.min,
        max: this.editCalForm.max
      };
      this.updateCal(payload, this.editForm.id);
    },

    onReset() {
      this.dialog = false
      this.initForm();
    },

    save() {
      this.calBool = true
      this.calColor = 'success'
      this.calText = 'Data saved'
      this.onSubmit()
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
      this.onReset()
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

  created() {
    this.getMessage();
  },

  mounted() {
    this.drawChartCal()
  },

}
</script>


