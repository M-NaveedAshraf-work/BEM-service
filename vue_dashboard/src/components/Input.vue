<template>

  <!-- Top Portion with file inputs, building info, and running the BEM -->

  <v-container grid-list-md>
    <v-row no-gutters>
      <v-col
        md="5">
        <v-card>
          <v-card-title>Input Files</v-card-title>
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

export default {

  name: "input",
  methods: {
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
    lighting: ['Lighting Daylight Factor', 'Lighting Occupancy Factor', 'Lighting Constant Illumination Control Factor', 'Parasitic Lighting Energy']
  }),
};
</script>

<style>
.container{
     max-width: 100vw;
     padding:100px;
  }
</style>

