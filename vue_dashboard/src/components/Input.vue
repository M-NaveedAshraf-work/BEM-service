<template>

  <!-- Top Portion with file inputs, building info, and running the BEM -->

  <v-container grid-list-md>
    <v-row no-gutters>
      <v-col
        md="5">
        <v-card>
          <p>{{ msg }}</p>
          <v-card-title>Input Files</v-card-title>
          <v-btn>{{ msg }}</v-btn>
          <v-card-text>Upload Weather File</v-card-text>
          <v-file-input
            accept="xls/*"
            label="Weather File"
          ></v-file-input>
          <v-card-text>Upload Building JSON File</v-card-text>
          <v-file-input
            accept="json/*"
            label="Building File"
          ></v-file-input>
        </v-card>
        <v-card outlined color="transparent">
          <v-card-title>     </v-card-title>
        </v-card>
        <v-card>
          <v-card-title>Run the BEM</v-card-title>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-select
                :items="output_period"
                label="Output Period"
                outlined
                dense
                ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
            >
              <v-btn
                align="center"
                depressed
                color="primary"
              >
              Run BEM
              </v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
      <v-col
        md="5"
        offset-md="2"
        >
        <v-card>
          <v-card-title
            align="center"
            >Building
          </v-card-title>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-text-field
                label="Building Name"
                outlined
                dense
                ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-text-field
                label="Building Location"
                outlined
                dense
                ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="10"
              offset-md="1"
              >
              <v-select
                :items="terrain_class"
                label="Terrain Class"
                outlined
                dense
                ></v-select>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="8"
              offset-md="1"
              >
              <v-text-field
                label="Building Ventilated Volume (m^3)"
                outlined
                dense
                type="number"
                ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              align="center"
              cols="12"
              md="8"
              offset-md="1"
              >
              <v-text-field
                label="Building Height (m)"
                outlined
                dense
                type="number"
                ></v-text-field>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
      md="4"
      offset-md="0"
      >
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Building Systems</v-card-title>
              <div>
                <v-expansion-panels
                  v-model="panel"
                  multiple
                >
                  <v-expansion-panel>
                    <v-expansion-panel-header>Lighting</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          label="Lighting Daylight Factor"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Lighting Occupancy Factor"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Lighting Constant Illumination Factor"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Y_N"
                          label="Is Parasitic Lighting Energy Considered?"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel>
                    <v-expansion-panel-header>Heating and Cooling Plants</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          label="Heating System COP [kW/kW]"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Cooling System Full Load COP [kW/kW]"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Relative COP100: for Realative Load 100%"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Partial Load COP75 Relative Load 75%"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Partial Load COP50 Relative Load 50%"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Partial Load COP25 Relative Load 25%"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel>
                    <v-expansion-panel-header>HVAC System</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-select
                          :items="HVAC"
                          label="HVAC System Type"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Vent_Fan"
                          label="Ventilation Fan"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Extra Ventilation Above Fresh Air Supply [liter/s]"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Heat_Recov"
                          label="Heat Recovery Type"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Exhaust"
                          label="Exhaust Air Recirculation %"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Building Air Leakage Level [m3/h]"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Specific Fan Power [W/(l/s)]"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Fan Flow Control Factor"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Pump_C"
                          label="Pump Control for Cooling"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Pump_H"
                          label="Pump Control for Heating"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Domestic Hot Water (DHW)</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-select
                          :items="DHW_Dis"
                          label="DHW Distribution System"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="DHW_Gen"
                          label="DHW Generation System"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Building Energy Management Systems</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-select
                          :items="BEM_Sys"
                          label="Type of BEM System Installed [Source: prEN 15232:2006 5.3 and 8]"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Photovoltaic System</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          label="PV Module Surface Area (m2)"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Orient"
                          label="PV Module Orientation"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Angle"
                          label="PV Module Angle (degrees)"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="PV Panel Peak Power Coeff (kW/m2)"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="PV System Performance Factor"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Solar Water Heating System</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          label="Solar Collector Surface Area (m2)"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Orient"
                          label="SHW Module Orientation"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="Orient"
                          label="SHW Module Angle (degrees)"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Wind Turbine System</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          label="Wind Turbine Diameter (m)"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          label="Wind Turbine Efficiency"
                          outlined
                          dense
                          type="number"
                        ></v-text-field>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Energy Sources</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-select
                          :items="E_Source"
                          label="Primary Energy Source for Heating"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="E_Source"
                          label="Primary Energy Source for DHW"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          :items="E_Source"
                          label="Primary Energy Source for Cooling"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <div class="text-center">
                          <v-dialog
                            v-model="dialog"
                            width="500"
                          >
                            <template v-slot:activator="{ on, attrs }">
                              <v-btn
                                color="red lighten-2"
                                dark
                                v-bind="attrs"
                                v-on="on"
                              >
                                Alter Primary and Emission Factors
                              </v-btn>
                            </template>

                            <v-card>
                              <v-card-title class="text-h5 grey lighten-2">
                                Primary and Emission Factors
                              </v-card-title>

                              <v-card-text>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                              </v-card-text>

                              <v-divider></v-divider>

                              <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                  color="primary"
                                  text
                                  @click="dialog = false"
                                >
                                  Close
                                </v-btn>
                              </v-card-actions>
                            </v-card>
                          </v-dialog>
                        </div>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </div>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Building Operation</v-card-title>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-title>Envelope</v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
      <v-col
      md="8"
      >
        <v-card>
          <div id="input">
            <div id="main" style="width: 1100px;height:700px;"></div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>

import axios from 'axios'

export default {

  name: "input",
  methods: {

    getMessage() {
      const path = 'http://127.0.0.1:5000/input'
      axios.get(path)
      .then((res) => {
        this.msg = res.data;
      })
      .catch((error) => {
        console.error(error);
      })
    },

    drawChart() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(document.getElementById("main"));
      //Specify configuration items and data for the chart
      let option = {
        legend: {},
    tooltip: {
      trigger: 'axis',
      showContent: false
    },
    dataset: {
      source: [
        ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
        ['Milk Tea', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
        ['Matcha Latte', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
        ['Cheese Cocoa', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
        ['Walnut Brownie', 25.2, 37.1, 41.2, 18, 33.9, 49.1]
      ]
    },
    xAxis: { type: 'category' },
    yAxis: { gridIndex: 0 },
    grid: { top: '55%' },
    series: [
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'pie',
        id: 'pie',
        radius: '30%',
        center: ['50%', '25%'],
        emphasis: {
          focus: 'self'
        },
        label: {
          formatter: '{b}: {@2012} ({d}%)'
        },
        encode: {
          itemName: 'product',
          value: '2012',
          tooltip: '2012'
        }
      }
    ]
      };
      //Use the configuration items and data just specified to display the chart.
      myChart.setOption(option);
    }
  },

  mounted() {
    this.drawChart();
  },

  created() {
    this.getMessage();
  },

  data: () => ({

    terrain_class: ['Open Terrain', 'Country', 'Urban / City'],
    output_period: ['Hourly', 'Daily', 'Monthly'],
    panel: [],
    Y_N: ['Yes', 'No'],
    HVAC: ['1. No airco system / Water or Water&Air / NA / Yes',
            '2. No airco system / Water or Water&Air / NA / No',
            '3. No airco system / Air / NA /  Yes',
            '4. No airco system / Air / NA /  No',
            '5. Single duct system / Water or Water&Air / Water / Yes',
            '6 .Single duct system / Water or Water&Air / Air / Yes',
            '7. Single duct system / Water or Water&Air / Air / No',
            '8. Single duct system / Air  / Air / Yes',
            '9. Single duct system / Air / Air / No',
            '10. Dual duct system / Water or Water&Air / Water / Yes',
            '11. Dual duct system / Water or Water&Air / Air / Yes',
            '12. Dual duct system  / Water or Water&Air / Air / No',
            '13. Dual duct system / Air / Water / Yes',
            '14. Single duct , Terminal reheat / Water or Water&Air / Water / Yes',
            '15. Single duct , Terminal reheat  / Water or Water&Air / Air / Yes',
            '16. Single duct , Terminal reheat / Water or Water&Air / Air / No',
            '17. Constant volume / Water or Water&Air / Water / Yes',
            '18. Constant volume / Water or Water&Air / Air / Yes',
            '19. Constant volume / Water or Water&Air / Air / No',
            '20. Constant volume / Air  / Air / Yes',
            '21. Constant volume / Air / Air / No',
            '22. Variable air volume / Water or Water&Air / Water / Yes',
            '23. Variable air volume / Water or Water&Air / Air / Yes',
            '24. Variable air volume / Water or Water&Air / Air / No',
            '25. Fan coil system, 2-pipe',
            '26. Fan coil system, 3-pipe',
            '27. Fan coil system, 4-pipe',
            '28. Induction system, 2-pipe non change over',
            '29. Induction system, 2-pipe change over',
            '30. Induction system, 3-pipe',
            '31. Induction system, 4-pipe',
            '32. 2-pipe radiant cooling panels (chilled ceilings & passive chilled beams)',
            '33. 4-pipe radiant cooling panels (chilled ceilings & passive chilled beams)',
            '34. Embedded cooling system floors, walls or ceilings',
            '35. Room units including single duct units',
            '36. Direct expansion single split system',
            '37. Direct expansion single split system including variable refrigerant flow systems'
          ],
    Vent_Fan: ['1. Mechanical system only; no provision for natural ventilation',
              '2. Mech. w/ optimal natural outside air cooling (whenever possible)',
              '3. Same as 2, with fully natural fresh air supply (always)',
              ],
    Heat_Recov: ['No heat recovery',
                'Heat exchange plates or pipes (0.65)',
                'Two-elements-system (0.6)',
                'Loading cold with air-conditioning (0.4)',
                'Heat-pipes (0.6)',
                'Slowly rotating or intermittent heat exchangers (0.7)',
                ],
    Exhaust: ['No exhaust air recirculation',
              'Exhaust air recirculation 20%',
              'Exhaust air recirculation  40%',
              'Exhaust air recirculation  60%',
              ],
    Pump_C: ['No pump for cooling',
            'Automatic control more than 50%',
            'All other cases',
            ],
    Pump_H: ['No pump for heating',
            'Automatic control more than 50%',
            'All other cases',
            ],
    DHW_Dis: ['All Taps Within 3m from Heat Generation',
              'Taps More Than 3m from Heat Generation',
              'Circulation system or Unknown',
              ],
    DHW_Gen: ['Electric (0.75)',
              'VR-Boiler (0.61)',
              'Gas Boiler, HR-Boiler (0.75)',
              'Co-Generation (0.9)',
              'District Heating (0.9)',
              'Heat Pump (1.4)',
              'Steam (0.61)',
              ],
    BEM_Sys : ['Class D', 'Class C', 'Class B', 'Class A'],
    Orient: ['S','SE','E','W','SW'],
    Angle: ['0','30','45','60','90'],
    E_Source: ['Electicity', 'Natural Gas', 'Fuel'],
    lighting: ['Lighting Daylight Factor', 'Lighting Occupancy Factor', 'Lighting Constant Illumination Control Factor', 'Parasitic Lighting Energy'],
    dialog: false,

  }),
};
</script>

<style>
.container{
     max-width: 100vw;
     padding:100px;
  }
</style>

