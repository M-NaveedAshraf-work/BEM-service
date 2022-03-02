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
            v-model = "uploadFile"
            accept=".json, .JSON"
            label="Building File"
            chips
            prependIcon=""
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
                v-on:click="getData(); runBEM();"
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
                v-model="jsonData.Name"
                label= "Building Name"
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
                v-model="jsonData.Location"
                label="Building Location"
                outlined
                dense
                @change="Location=parsefloat(Location)"
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
                v-model="jsonData.TerrainClass"
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
                v-model="jsonData.Volume"
                label="Building Ventilated Volume (m^3)"
                outlined
                dense
                type="number"
                @change="jsonData.Volume=parseFloat(jsonData.Volume)"
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
                v-model="jsonData.Height"
                label="Building Height (m)"
                outlined
                dense
                type="number"
                @change="jsonData.Height=parseFloat(jsonData.Height)"
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
                  v-model="jsonData.panel"
                  multiple
                >
                  <v-expansion-panel>
                    <v-expansion-panel-header>Lighting</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.DaylightingFactor"
                          label="Lighting Daylight Factor"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.DayLightingFactor=parseFloat(jsonData.DayLightingFactor)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.OccupancyFactor"
                          label="Lighting Occupancy Factor"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.OccupancyFactor=parseFloat(jsonData.OccupancyFactor)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.LightingControlFactor"
                          label="Lighting Constant Illumination Factor"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.LightingControlFactor=parseFloat(jsonData.LightingControlFactor)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.ParasiticLightingEnergy"
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
                          v-model="jsonData.HeatingCOP"
                          label="Heating System COP [kW/kW]"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.HeatingCOP=parseFloat(jsonData.HeatingCOP)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.CoolingCOP"
                          label="Cooling System Full Load COP [kW/kW]"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.CoolingCOP=parseFloat(jsonData.CoolingCOP)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.COP100"
                          label="Relative COP100: for Realative Load 100%"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.COP100=parseFloat(jsonData.COP100)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.COP75"
                          label="Partial Load COP75 Relative Load 75%"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.COP75=parseFloat(jsonData.COP75)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.COP50"
                          label="Partial Load COP50 Relative Load 50%"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.COP50=parseFloat(jsonData.COP50)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.COP25"
                          label="Partial Load COP25 Relative Load 25%"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.COP25=parseFloat(jsonData.COP25)"
                        ></v-text-field>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel>
                    <v-expansion-panel-header>HVAC System</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-select
                          v-model="jsonData.HVACSystemType"
                          :items="HVAC"
                          label="HVAC System Type"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.VentilationCoolingType"
                          :items="Vent_Fan"
                          label="Ventilation Fan"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.ExtraVentilation"
                          label="Extra Ventilation Above Fresh Air Supply [liter/s]"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.ExtraVentilation=parseFloat(jsonData.ExtraVentilation)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.HeatRecoveryType"
                          :items="Heat_Recov"
                          label="Heat Recovery Type"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.ExhaustAirRecirculation"
                          :items="Exhaust"
                          label="Exhaust Air Recirculation %"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.AirLeakageLevel"
                          label="Building Air Leakage Level [m3/h]"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.AirLeakageLevel=parseFloat(jsonData.AirLeakageLevel)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.SpecificFanPower"
                          label="Specific Fan Power [W/(l/s)]"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.SpecificFanPower=parseFloat(jsonData.SpecificFanPower)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.FanControlFactor"
                          label="Fan Flow Control Factor"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.FanControlFactor=parseFloat(jsonData.FanControlFactor)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.PumpCoolingControl"
                          :items="Pump_C"
                          label="Pump Control for Cooling"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.PumpHeatingControl"
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
                          v-model="jsonData.DHWDistrinutionSystem"
                          :items="DHW_Dis"
                          label="DHW Distribution System"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.DHWGenerationSystem"
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
                          v-model="jsonData.BEMType"
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
                          v-model="jsonData.PVArea"
                          label="PV Module Surface Area (m2)"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.PVArea=parseFloat(jsonData.PVArea)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.PVOrientation"
                          :items="Orient"
                          label="PV Module Orientation"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.PVTiltAngle"
                          :items="Angle"
                          label="PV Module Angle (degrees)"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.PVPeakPower"
                          label="PV Panel Peak Power Coeff (kW/m2)"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.PVPeakPower=parseFloat(jsonData.PVPeakPower)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.PVPerformanceFactor"
                          label="PV System Performance Factor"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.PVPerformanceFactor=parseFloat(jsonData.PVPerformanceFactor)"
                        ></v-text-field>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Solar Water Heating System</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.SHWArea"
                          label="Solar Collector Surface Area (m2)"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.SHWArea=parseFloat(jsonData.SHWArea)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.SHWOrientation"
                          :items="Orient"
                          label="SHW Module Orientation"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.SHWTiltAngle"
                          :items="Angle"
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
                          v-model="jsonData.WindTurbineDiameter"
                          label="Wind Turbine Diameter (m)"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.WindTurbineDiameter=parseFloat(jsonData.WindTurbineDiameter)"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                          v-model="jsonData.WindTurbineEfficiency"
                          label="Wind Turbine Efficiency"
                          outlined
                          dense
                          type="number"
                          @change="jsonData.WindTurbineEfficiency=parseFloat(jsonData.WindTurbineEfficiency)"
                        ></v-text-field>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>Energy Sources</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-select
                          v-model="jsonData.HeatingEnergySource"
                          :items="E_Source1"
                          label="Primary Energy Source for Heating"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.DHWEnergySource"
                          :items="E_Source2"
                          label="Primary Energy Source for DHW"
                          outlined
                          dense
                        ></v-select>
                      </v-row>
                      <v-row>
                        <v-select
                          v-model="jsonData.CoolingEnergySource"
                          :items="E_Source3"
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
            <div id="chart" ref="chart" style="width: 1100px;height:700px;"></div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>

import axios from 'axios'

export default {

  data: () => {
    return {

      uploadData: null,
      uploadFile: null,

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
      BEM_Sys : [1, 2, 3, 4],
      Orient: ['S','SE','E','W','SW'],
      Angle: [0, 30, 45, 60, 90],
      E_Source1: ['Electicity', 'Natural Gas', 'Fuel'],
      E_Source2: ['Electicity', 'Natural Gas', 'Fuel'],
      E_Source3: ['Electicity', 'Natural Gas', 'Fuel'],
      lighting: ['Lighting Daylight Factor', 'Lighting Occupancy Factor', 'Lighting Constant Illumination Control Factor', 'Parasitic Lighting Energy'],
      jsonData : [],
      StateBEM : false,
      dialog: false,
    }
  },
  
  methods: {

    getData() {
      const path = 'http://127.0.0.1:5000/input'
      axios.get(path)
      .then((res) => {
        this.jsonData= res.data.jsonData;
      })
      .catch((error) => {
        console.error(error);
      })
    },

    updateData() {
      const path = 'http://127.0.0.1:5000/input'
      axios.put(path, this.jsonData)
      .then(() => {
        this.getData();
      })
      .catch((error) => {
        console.error(error);
        this.getData
      })
    },

    runBEM() {
      const path = 'http://127.0.0.1:5000/BEM'
      axios.get(path)
      .then((res) => {
        this.StateBEM = res.data
      })
      .catch((error) => {
        console.error(error);
      })
    },

    /*
    updateVar() {
      this.$store.commit("updateParams",[this.Name, this.TerrainClass, this.Volume, this.Height, this.HeatCapacity, this.DayLightingFactor, this.OccupancyFactor,
      this.LightingControlFactor, this.ParasiticLightingEnergy, this.ParasiticLightingEnergyAmount, this.HeatingCOP, this.CoolingCOP, this.COP100, this.COP75,
      this.COP50, this.COP25, this.COPWeighting100, this.COPWeighting75, this.COPWeighting50, this.COPWeighting25, this.HVACSystemType, this.VentilationCoolingType,
      this.RHThreshold, this.ExtraVentilation, this.HeatRecoveryType, this.ExhaustAirRecirculation, this.AirLeakageLevel, this.SpecificFanPower, this.FanControlFactor,
      this.PumpCoolingControl, this.PumpHeatingControl, this.DHWDistrinutionSystem, this.DHWGenerationSystem, this.BEMType, this.PVArea, this.PVOrientation, this.PVTiltAngle,
      this.PVPeakPower, this.PVPerformanceFactor, this.SHWArea, this.SHWOrientation, this.SHWTiltAngle, this.SHWEfficiency, this.WindTurbineDiameter, this.WindTurbineEfficiency,
      this.HeatingEnergySource, this.DHWEnergySource, this.CoolingEnergySource, this.Electricity, this.NaturalGas, this.Fuel, this.Zone1, this.TemperatureSetPoint,
      this.Zone1_Schedule, this.Envelope, this.Material, this.StartDay, this.NaturalVentilation, this.ElectricBattery, this.LightingDimmer, this.ElectricVehicle, 
      this.RetailRefrig, this.Garage, this.Garage_Schedule]
    )},

    downloadInput() {
      this.$store.commit(json_data,this.data.sort())
      this.updateVar
      this.$store.commit(json_data)
    },

    uploadInput() {
      let obj = this.json_data

      this.Name = obj.Name
      this.TerrainClass = obj.TerrainClass 
      this.Volume = obj.Volume 
      this.Height = obj.Height 
      this.HeatCapacity = obj.HeatCapacity 
      this.DayLightingFactor = obj.DayLightingFactor
      this.OccupancyFactor = obj.OccupancyFactor
      this.LightingControlFactor = obj.LightingControlFactor
      this.ParasiticLightingEnergy = obj.ParasiticLightingEnergy
      this.ParasiticLightingEnergyAmount = obj.ParasiticLightingEnergyAmount
      this.HeatingCOP = obj.HeatingCOP
      this.CoolingCOP = obj.CoolingCOP
      this.COP100 = obj.COP100
      this.COP75 = obj.COP75
      this.COP50 = obj.COP50
      this.COP25 = obj.COP25
      this.COPWeighting100 = obj.COPWeighting100
      this.COPWeighting75 = obj.COPWeighting75
      this.COPWeighting50 = obj.COPWeighting50
      this.COPWeighting25 = obj.COPWeighting25
      this.HVACSystemType = obj.HVACSystemType
      this.VentilationCoolingType = obj.VentilationCoolingType
      this.RHThreshold = obj.RHThreshold
      this.ExtraVentilation = obj.ExtraVentilation
      this.HeatRecoveryType = obj.HeatRecoveryType
      this.ExhaustAirRecirculation = obj.ExhaustAirRecirculation
      this.AirLeakageLevel = obj.AirLeakageLevel
      this.SpecificFanPower = obj.SpecificFanPower
      this.FanControlFactor = obj.FanControlFactor
      this.PumpCoolingControl = obj.PumpCoolingControl
      this.PumpHeatingControl = obj.PumpHeatingControl
      this.DHWDistrinutionSystem = obj.DHWDistrinutionSystem
      this.DHWGenerationSystem = obj.DHWGenerationSystem
      this.BEMType = obj.BEMType
      this.PVArea = obj.PVArea
      this.PVOrientation = obj.PVOrientation
      this.PVTiltAngle = obj.PVTiltAngle
      this.PVPeakPower = obj.PVPeakPower
      this.PVPerformanceFactor = obj.PVPerformanceFactor
      this.SHWArea = obj.SHWArea
      this.SHWOrientation = obj.SHWOrientation
      this.SHWTiltAngle = obj.SHWTiltAngle
      this.SHWEfficiency = obj.SHWEfficiency
      this.WindTurbineDiameter = obj.WindTurbineDiameter
      this.WindTurbineEfficiency = obj.WindTurbineEfficiency
      this.HeatingEnergySource = obj.HeatingEnergySource
      this.DHWEnergySource = obj.DHWEnergySource
      this.CoolingEnergySource = obj.CoolingEnergySource
      this.Electricity = obj.Electricity
      this.NaturalGas = obj.NaturalGas
      this.Fuel = obj.Fuel
      this.Zone1 = obj.Zone1
      this.TemperatureSetPoint = obj.TemperatureSetPoint
      this.Zone1_Schedule = obj.Zone1_Schedule
      this.Envelope = obj.Envelope
      this.Material = obj.Material
      this.StartDay = obj.StartDay
      this.NaturalVentilation = obj.NaturalVentilation
      this.ElectricBattery = obj.ElectricBattery
      this.LightingDimmer = obj.LightingDimmer
      this.ElectricVehicle = obj.ElectricVehicle
      this.RetailRefrig = obj.RetailRefrig
      this.Garage = obj.Garage
      this.Garage_Schedule = obj.Garage_Schedule

      this.updateVar()
      this.$store.commit(json_data)
    }, */

    async openFile(file) {
      return new Promise((resolve, reject) => {
        const fileReader = new FileReader()
        fileReader.onload = event => resolve(JSON.parse(event.target.result))
        fileReader.onerror = error => reject(error)
        fileReader.readAsText(file)
      })
    },

    drawChart() {
      //Initialize the echarts instance based on the prepared dom
      let myChart = this.$echarts.init(this.$refs.chart);
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
    this.getData();
  },

  watch: {

    jsonData(v) {
      this.Name = v
    },

    'uploadFie': async function() {
      if (this.uploadFile != null) {
        this.uploadData = await this.OpenFile(this.uploadFile)
        this.uploadInput()
      }
    }
  },
};
</script>

<style>
.container{
     max-width: 100vw;
     padding:100px;
  }
</style>

